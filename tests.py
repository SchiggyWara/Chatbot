
from nltk.chat.util import Chat, reflections
from main import pairs


def test_chatbot_responses():
    chatbot = Chat(pairs, reflections)

    test_cases = [
        # Begrüßung
        ("Wie geht es dir?", "Mir geht es gut, danke! Wie kann ich dir behilflich sein?"),

        # verabschieden
        ("auf Wiedersehen",
         "Auf Wiedersehen!"),
        ("Tschüss",
         "Auf Wiedersehen!"),
        ("Bye",
         "Auf Wiedersehen!"),

        # Problem
        ("Ich habe ein Problem",
         "Kein Problem, ich helfe gerne bei IT-Fragen. Kannst du das Problem genauer beschreiben?"),
        ("Ein Fehler ist aufgetreten",
         "Es tut mir leid zu hören, dass du Probleme hast. Kannst du weitere Details zu dem Problem geben?"),

        # Internet, WLAN
        ("Mein WLAN will nicht",
         "Es könnte ein Problem mit deiner Internetverbindung geben. Versuche, den Router neu zu starten und prüfe, ob alle Kabel richtig angeschlossen sind."),
        ("Internet",
         "Es könnte ein Problem mit deiner Internetverbindung geben. Versuche, den Router neu zu starten und prüfe, ob alle Kabel richtig angeschlossen sind."),

        # Drucker
        ("Drucker",
         "Stelle sicher, dass der Drucker eingeschaltet ist und die neuesten Treiber installiert sind. Überprüfe auch die Druckwarteschlange und starte sie gegebenenfalls neu."),
        ("ausdrucken",
         "Stelle sicher, dass der Drucker eingeschaltet ist und die neuesten Treiber installiert sind. Überprüfe auch die Druckwarteschlange und starte sie gegebenenfalls neu."),

        # Email, outlook
        ("E-Mail funzt nicht",
         "Überprüfe deine E-Mail-Kontoeinstellungen in Outlook und stellen sicher, dass du mit dem Internet verbunden bist. Wenn das Problem weiterhin besteht, kontaktiere bitte unseren IT-Support."),
        ("outlook funzt nicht",
         "Überprüfe deine E-Mail-Kontoeinstellungen in Outlook und stellen sicher, dass du mit dem Internet verbunden bist. Wenn das Problem weiterhin besteht, kontaktiere bitte unseren IT-Support."),

        # Passwort
        ("Passwort macht Sorgen",
         "Wenn du Probleme mit deinem Passwort oder bei der Anmeldung hast, kontaktiere bitte unseren IT-Support. Sie werden dir gerne weiterhelfen."),
        ("Anmeldung klappt net",
         "Wenn du Probleme mit deinem Passwort oder bei der Anmeldung hast, kontaktiere bitte unseren IT-Support. Sie werden dir gerne weiterhelfen."),

        #Datei-Probleme
        ("Datei klappt net",
         "In einigen Fällen können gelöschte Dateien wiederhergestellt werden. Bitte überprüfen Sie den Papierkorb auf Ihrem Computer, ob die Datei dort abgelegt wurde. Wenn nicht, könnten wir versuchen, Datenwiederherstellungssoftware zu verwenden, um die Datei wiederherzustellen."),
        ("habe sie gelöscht",
         "In einigen Fällen können gelöschte Dateien wiederhergestellt werden. Bitte überprüfen Sie den Papierkorb auf Ihrem Computer, ob die Datei dort abgelegt wurde. Wenn nicht, könnten wir versuchen, Datenwiederherstellungssoftware zu verwenden, um die Datei wiederherzustellen."),
        ("kann ich sie wiederherstellen?",
         "In einigen Fällen können gelöschte Dateien wiederhergestellt werden. Bitte überprüfen Sie den Papierkorb auf Ihrem Computer, ob die Datei dort abgelegt wurde. Wenn nicht, könnten wir versuchen, Datenwiederherstellungssoftware zu verwenden, um die Datei wiederherzustellen."),

        # Probleme beim Hochfahren
        ("Rechner startet nicht",
         "Bitte überprüfen Sie zunächst, ob der Computer ordnungsgemäß mit Strom versorgt wird. Stellen Sie sicher, dass alle Kabel richtig angeschlossen sind. Versuchen Sie, den Computer neu zu starten und beobachten Sie, ob Fehlermeldungen angezeigt werden. Wenn das Problem weiterhin besteht, wenden Sie sich bitte an unseren IT-Support."),
        ("Hochfahren macht Schwierigkeiten",
         "Bitte überprüfen Sie zunächst, ob der Computer ordnungsgemäß mit Strom versorgt wird. Stellen Sie sicher, dass alle Kabel richtig angeschlossen sind. Versuchen Sie, den Computer neu zu starten und beobachten Sie, ob Fehlermeldungen angezeigt werden. Wenn das Problem weiterhin besteht, wenden Sie sich bitte an unseren IT-Support."),

         # Random input (jeder weitere Input)
        ("Random input",
         "Ich kann leider keine direkte Antwort auf deine Frage finden. \n\nEventuell hast du dich verschrieben? \n\nVersuch deine Frage anders zu formuliere, möglicherweise helfen dir Stichworte wie 'Drucker', 'WLAN', 'Internet' oder 'E-Mail' weiter. \n\nBesteht dein Problem weiterhin? Klicke auf Yes um dir die Kontakdaten eines Mitarbeiters anzuzeigen.")

    ]

    for user_input, expected_response in test_cases:
        response = chatbot.respond(user_input)
        print(f"User input: {user_input}")
        print(f"Expected response: {expected_response}")
        print(f"Actual response  : {response}")
        print()
        assert response == expected_response


test_chatbot_responses()
