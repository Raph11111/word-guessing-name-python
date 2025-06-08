# Wortrate-Spiel (Word Guessing Game)

Dieses Projekt ist ein interaktives Wortrate-Spiel, entwickelt in Python mit einer grafischen Benutzeroberfläche (GUI) unter Verwendung von `customtkinter`. Es demonstriert meine Fähigkeiten in der Softwareentwicklung, objektorientierter Programmierung und der Erstellung benutzerfreundlicher Anwendungen.

## Inhaltsverzeichnis
- [Über das Projekt](#über-das-projekt)
- [Funktionen](#funktionen)
- [Technologien](#technologien)
- [Installation und Ausführung](#installation-und-ausführung)
- [Struktur des Projekts](#struktur-des-projekts)
- [Beispiel-Screenshots](#beispiel-screenshots)
- [Bezug zur Stellenausschreibung](#bezug-zur-stellenausschreibung)
- [Kontakt](#kontakt)

## Über das Projekt

Dieses Wortrate-Spiel ist eine Anwendung, bei der Spieler Wörter erraten müssen. Die Anwendung verfügt über eine grafische Benutzeroberfläche, die es dem Benutzer ermöglicht, seinen Namen einzugeben, das Spiel zu spielen und seinen Punktestand auf einer Bestenliste zu verfolgen. Die Wörter werden aus einer JSON-Datei geladen, und die Spielergebnisse werden gespeichert.

## Funktionen

* **Interaktive GUI**: Entwickelt mit `customtkinter` für eine moderne und intuitive Benutzeroberfläche.
* **Spielerprofil**: Erfassung und Verwaltung des Spielernamens.
* **Wortverwaltung**: Laden von Wörtern aus einer `sample_wordles.json`-Datei.
* **Raten-Historie**: Visuelle Darstellung der bisherigen Rateversuche mit Farbcodierung (Grün für richtigen Buchstaben an richtiger Stelle, Gold für richtigen Buchstaben an falscher Stelle, Grau für nicht gefunden).
* **Punktesystem**: Spieler erhalten Punkte basierend auf der Anzahl der verbleibenden Versuche.
* **Bestenliste (Scoreboard)**: Speicherung und Anzeige der Top-Scores in einer JSON-Datei.
* **Fehlerbehandlung**: Robuste Eingabevalidierung und Fehlerbehandlung.
* **Modulare Architektur**: Klares OOP-Design mit separaten Klassen für Game UI, Game Logic, Player, Score, Word, Guess, Scoreboard, etc.

## Technologien

* **Python 3.x**
* **CustomTkinter**: Für die GUI-Entwicklung.
* **JSON**: Zum Speichern und Laden von Wörtern und Bestenlisten.

## Installation und Ausführung

Befolgen Sie diese Schritte, um das Spiel lokal auszuführen:

1.  **Klonen Sie das Repository:**
    ```bash
    git clone [https://github.com/IhrBenutzername/word-guessing-game.git](https://github.com/IhrBenutzername/word-guessing-game.git)
    cd word-guessing-game
    ```

2.  **Erstellen Sie eine virtuelle Umgebung (empfohlen):**
    ```bash
    python -m venv venv
    # Auf Windows:
    # .\venv\Scripts\activate
    # Auf macOS/Linux:
    # source venv/bin/activate
    ```

3.  **Installieren Sie die Abhängigkeiten:**
    ```bash
    pip install -r requirements.txt
    ```
    (Stellen Sie sicher, dass `customtkinter` in Ihrer `requirements.txt` enthalten ist.)

4.  **Führen Sie das Spiel aus:**
    ```bash
    python src/main.py
    ```

Das Spiel wird sich in einem neuen Fenster öffnen.

## Struktur des Projekts

Das Projekt ist modular aufgebaut, um die Wartbarkeit und Erweiterbarkeit zu gewährleisten:

word-guessing-game/
├── assets/                  # Enthält die JSON-Datei mit den Wörtern
│ └── sample_wordles.json
├── docs/                    # Dokumentation (z.B. Screenshots)
│ └── screenshots/
├── src/                     # Quellcode-Dateien
│ ├── game.py                # Konsolenbasierte Spiellogik (alternative Version)
│ ├── game_ui.py             # Hauptklasse für die grafische Benutzeroberfläche
│ ├── guess.py               # Logik für einen Rateversuch
│ ├── guess_entry.py         # Repräsentiert einen geratenen Buchstaben und dessen Status
│ ├── guess_history.py       # Verwaltet die Historie der Rateversuche
│ ├── main.py                # Startpunkt der Anwendung (initialisiert GameUI)
│ ├── name.py                # Kapselt die Namenslogik des Spielers
│ ├── player.py              # Repräsentiert einen Spieler (Name und Punktestand)
│ ├── score.py               # Verwaltet den Punktestand eines Spielers
│ ├── scoreboard.py          # Verwaltet das Speichern und Laden der Bestenliste
│ ├── word.py                # Repräsentiert das zu erratende Wort
│ ├── word_list_factory.py   # Abstrakte Basisklasse für Wortlisten
│ └── word_list_from_json_file.py # Implementierung zum Laden von Wörtern aus JSON
├── .gitignore               # Dateien, die von Git ignoriert werden sollen
├── LICENSE                  # Lizenzinformationen
└── README.md                # Diese README-Datei
└── requirements.txt         # Projekt-Abhängigkeiten
