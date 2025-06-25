
# 🧠 Hybrid Alignment Architecture

**Ein modulares Framework zur Kombination von Constitutional AI & Multi-Agent Critique.**  
Entwickelt, um robuste, nachvollziehbare und adaptive Alignment-Systeme zu ermöglichen.

---

## 🚀 Features

- YAML-basierte **Verfassung (Constitution)** mit auditierbaren Prinzipien
- Rollenbasierte Agentenarchitektur:
  - 🤖 `SocraticAgent`: stellt tiefgehende Fragen
  - 😈 `DevilAgent`: provoziert Exploits & Fehler
  - 🧠 `ArbiterAgent`: entscheidet bei Widersprüchen
  - 🛠️ `EngineerAgent`: prüft Nützlichkeit & Umsetzbarkeit
  - 🧽 `CleanUpAgent`: filtert schwache Argumente
- Bewertungslogik: Verfassungskonformität + epistemisches Feedback
- Meta-Aggregation zur Bewertung von Konsens und Vertrauensniveau
- FastAPI-Schnittstelle mit JSON-API für Analyse & Feedback
- Vollständig getestet mit `pytest`

---

## 📁 Projektstruktur

```bash
hybrid_alignment_architecture/
├── app/
│   ├── agents/                # Agentenrollen
│   ├── core/                  # Verfassung, Bewertung, Meta-Logik
│   ├── schemas/               # Datenmodelle
│   └── main.py                # FastAPI Entry-Point
├── constitution/              # YAML-Verfassung
├── tests/                     # pytest-Tests
└── README.md


⸻

🧪 Schnellstart

# Abhängigkeiten installieren
pip install -r requirements.txt

# Server starten
uvicorn app.main:app --reload

# Tests ausführen
pytest


⸻

🔍 Beispielendpunkte (API)

Bewertung eines Textes:

POST /evaluate
{
  "text": "Das System darf niemals lügen und muss ehrlich bleiben."
}

Aggregiertes Agentenfeedback:

POST /meta/aggregate
[
  {"agent_name": "A", "content": "ok", "epistemic_score": 0.7},
  {"agent_name": "B", "content": "ok", "epistemic_score": 0.4}
]


⸻

🤝 Mitwirken

Dieses Projekt ist offen für Forschung, Red-Teaming, Interpretationsmodule und KI-Sicherheit.
Jeder Beitrag, der das Alignment robuster, ethischer oder testbarer macht, ist willkommen.

⸻
