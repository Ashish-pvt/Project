# LinkedIn post draft

> Replace `<CLOUD_RUN_URL>` before posting. Keep the three-part structure the submission guide asks for: Problem → Build → Solution fit.

---

**The problem.** Millions of construction workers, hospital staff and factory operators in India still have their shifts tracked on paper registers and WhatsApp groups. Overtime goes uncounted, payslips are unclear, and many workers stay silent about hazards or harassment because they fear being identified. Managers only hear about burnout and unsafe conditions once someone is injured or quits.

**What I built: FairShift** 🛠️, for #PromptWars2026 with SRM ACM Student Chapter (UN SDG 8: Decent Work).

👷 **Worker app** (Hindi, Tamil, English; works on cheap phones)
• Check in by typing a rotating 4-digit site code, so no QR or camera is needed. Supervisors can mark workers without phones present.
• Payslip with basic pay, overtime and night allowance, read aloud in the worker's language
• Fatigue alerts for long days, short rest and too many days in a row
• SafeVoice: hold a button and report a hazard in any language. Reports are anonymous by default.

📊 **Manager dashboard**
• Team health score with plain-language reasons, as an early warning for burnout and attrition (team-level only, for privacy)
• Safety board where Gemini translates and triages each report, and unacknowledged critical issues escalate automatically
• Attendance trends and roll call

**How it fits the problem.** Every pain point in the brief maps to a feature: clear pay → spoken payslip; fear of identification → anonymous reports and team-level metrics; ignored hazards → triage and escalation deadlines; attrition → team health signals; low literacy and cheap phones → voice, icons and no camera. Industry rules are config files, and the demo runs a construction site and a hospital side by side.

**Tech:** Python FastAPI · vanilla JS installable web app · Gemini on Vertex AI · Google Cloud Run · 74 unit and API tests · strict CSP, no API keys in code.

🔗 Live demo: <CLOUD_RUN_URL>
💻 Code: https://github.com/Ashish-pvt/Project.git

#SDG8 #DecentWork #GoogleCloud #Gemini #CloudRun #BuildWithAI #ACM #SRM
