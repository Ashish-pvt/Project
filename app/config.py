"""Runtime settings, read from environment variables. No secrets live in code."""

from __future__ import annotations

import os
import secrets
from dataclasses import dataclass


def _flag(name: str, default: bool) -> bool:
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Settings:
    session_secret: str
    site_code_secret: str
    demo_mode: bool
    secure_cookies: bool
    ai_enabled: bool
    gcp_project: str | None
    gcp_location: str
    gemini_model: str
    max_audio_bytes: int

    @classmethod
    def from_env(cls) -> Settings:
        project = os.environ.get("GOOGLE_CLOUD_PROJECT")
        return cls(
            # Random per-process fallbacks keep local dev working without leaking a fixed key.
            session_secret=os.environ.get("SESSION_SECRET") or secrets.token_urlsafe(32),
            site_code_secret=os.environ.get("SITE_CODE_SECRET") or secrets.token_urlsafe(32),
            demo_mode=_flag("DEMO_MODE", True),
            secure_cookies=_flag("SECURE_COOKIES", False),
            ai_enabled=_flag("AI_ENABLED", bool(project)),
            gcp_project=project,
            gcp_location=os.environ.get("GOOGLE_CLOUD_LOCATION", "asia-south1"),
            gemini_model=os.environ.get("GEMINI_MODEL", "gemini-2.5-flash"),
            max_audio_bytes=int(os.environ.get("MAX_AUDIO_BYTES", str(2 * 1024 * 1024))),
        )
