import tkinter as tk
from tkinter import messagebox
import nltk
from nltk.chat.util import Chat, reflections

# Definierte Muster und Antworten für den Chatbot
pairs = [
    [
        r"wie geht es dir?",
        ["Mir geht es gut, danke! Wie kann ich dir behilflich sein?"]
    ],
    [
        r"(.*)(verfügbar|frei)",
        ["Ja, ich bin verfügbar. Wie kann ich dir helfen?"]
    ],
    [
        r"auf Wiedersehen|Tschüss|Bye",
        ["Auf Wiedersehen!"]
    ],
    [
        r"ich habe ein Problem",
        ["Kein Problem, ich helfe gerne bei IT-Fragen. Kannst du das Problem genauer beschreiben?"]
    ],
    [
        r"(.*)(Problem|Fehler)",
        ["Es tut mir leid zu hören, dass du Probleme hast. Kannst du weitere Details zu dem Problem geben?"]
    ],
    [
        r"(.*)(Internet|WLAN)",
        ["Es könnte ein Problem mit deiner Internetverbindung geben. Versuche, den Router neu zu starten und prüfe, ob alle Kabel richtig angeschlossen sind."]
    ],
    [
        r"(.*)(Drucker|ausdrucken)",
        ["Stelle sicher, dass der Drucker eingeschaltet ist und die neuesten Treiber installiert sind. Überprüfe auch die Druckwarteschlange und starte sie gegebenenfalls neu."]
    ],
    [
        r"(.*)(E-Mail|Outlook)",
        ["Überprüfe deine E-Mail-Kontoeinstellungen in Outlook und stellen sicher, dass du mit dem Internet verbunden bist. Wenn das Problem weiterhin besteht, kontaktiere bitte unseren IT-Support."]
    ],
    [
        r"(.*)(Passwort|Anmeldung)",
        ["Wenn du Probleme mit deinem Passwort oder bei der Anmeldung hast, kontaktiere bitte unseren IT-Support. Sie werden dir gerne weiterhelfen."]
    ],
    [
        r".*",
        ["Ich kann leider keine direkte Antwort auf deine Frage finden. Möglicherweise helfen dir Stichworte wie 'Drucker', 'WLAN', 'Internet' oder 'E-Mail' weiter."]
    ]
]

# Initialisiere den Chatbot
chatbot = Chat(pairs, reflections)

# Funktion zum Anzeigen der Chatbot-Antworten
def display_response():
    user_input = entry.get()  # Benutzereingabe abrufen

    if user_input.lower() in ["tschüss", "auf wiedersehen", "bye"]:
        messagebox.showinfo("Chatbot", "Auf Wiedersehen!")
        root.quit()
    else:
        response = chatbot.respond(user_input)
        if response.startswith("Ich kann leider keine direkte Antwort auf deine Frage finden"):
            messagebox.showinfo("Chatbot", response)
            messagebox.showinfo("Kontaktinformationen IT-Support", "Telefon: 123456789\nE-Mail: support@win.de")
        else:
            messagebox.showinfo("Chatbot", response)

# Erstellen der GUI
root = tk.Tk()
root.title("IT-Support Chatbot")

# Willkommensnachricht
welcome_label = tk.Label(root, text="Willkommen beim IT-Support Chatbot!")
welcome_label.pack(pady=10)

welcome_label = tk.Label(root, text="Wie kann ich dir helfen?")
welcome_label.pack(pady=10)

# Eingabefeld für Benutzerfrage
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Antwort-Button
response_button = tk.Button(root, text="Antwort anzeigen", command=display_response)
response_button.pack(pady=5)

# Beenden-Button
quit_button = tk.Button(root, text="Beenden", command=root.quit)
quit_button.pack(pady=5)

# GUI starten
root.mainloop()

