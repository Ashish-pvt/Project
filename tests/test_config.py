import os

from app.config import Settings, load_env_file


def test_api_key_enables_ai(monkeypatch):
    monkeypatch.delenv("GOOGLE_CLOUD_PROJECT", raising=False)
    monkeypatch.delenv("AI_ENABLED", raising=False)
    monkeypatch.setenv("GEMINI_API_KEY", "test-key")
    settings = Settings.from_env()
    assert settings.ai_enabled
    assert settings.gemini_api_key == "test-key"


def test_env_file_does_not_override_real_environment(tmp_path, monkeypatch):
    env = tmp_path / ".env"
    env.write_text("# comment\nFS_TEST_A=from-file\nFS_TEST_B='quoted'\n", encoding="utf-8")
    monkeypatch.setenv("FS_TEST_A", "from-env")
    monkeypatch.delenv("FS_TEST_B", raising=False)
    load_env_file(env)
    assert os.environ["FS_TEST_A"] == "from-env"
    assert os.environ["FS_TEST_B"] == "quoted"
    monkeypatch.delenv("FS_TEST_B")
