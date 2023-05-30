#Import der Pyhton Bibliothek "NLTK" - muss vorher mit dem Befehl "pip install nltk" installiert werden
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
        r"auf Wiedersehen",
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

# Begrüßungsnachricht und Vorschläge
print("Chatbot: Hallo, wie kann ich dir helfen?")
print("Chatbot: Wenn du dir nicht sicher bist sind hier einige mögliche Vorschläge: WLAN, Internet, E-Mail, Drucker.")

# Starte die Chat-Schleife
while True:
    user_input = input("Du: ")
    if user_input.lower() == "quit":
        break
    else:
        print("Chatbot:", chatbot.respond(user_input))

