

"""
constitution.py – Datenmodell für einzelne Prinzipien der Verfassung

Dieses Schema definiert die Struktur eines Verfassungsprinzips für Typprüfung, Validierung und Klarheit.
"""

from pydantic import BaseModel

class VerfassungsPrinzip(BaseModel):
    name: str
    beschreibung: str