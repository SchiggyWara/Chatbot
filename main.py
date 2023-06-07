import tkinter as tk
from tkinter import messagebox
import nltk
import mysql.connector
from datetime import date
from datetime import datetime
from nltk.chat.util import Chat, reflections
 

# Verbindung zur MySQL-Datenbank herstellen
def create_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='passwort',
        database='chatbot'
    )
    return connection

# MySQL-Insert-Funktion
def insert_data(name, user_id, anfrage):
    connection = create_connection()
    cursor = connection.cursor()

    # Aktuelles Datum abrufen
    now = datetime.now()

    # SQL-Statement für den Insert erstellen
    sql = "INSERT INTO anfrage (name, id, anfrage, datum) VALUES (%s, %s, %s, %s)"
    values = (name, user_id, anfrage, now)

    try:
        # Insert ausführen
        cursor.execute(sql, values)
        connection.commit()
        print("Datensatz erfolgreich eingefügt!")
    except Exception as e:
        print(f"Fehler beim Einfügen des Datensatzes: {str(e)}")

    # Verbindung schließen
    cursor.close()
    connection.close()

# Definierte Muster und Antworten für den Chatbot
pairs = [
    [
        r"wie geht es dir?",
        ["Mir geht es gut, danke! Wie kann ich dir behilflich sein?"]
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
        r"(.*)\b(Problem|Fehler)\b",
        ["Es tut mir leid zu hören, dass du Probleme hast. Kannst du weitere Details zu dem Problem geben?"]
    ],
    [
        r"(.*)\b(Internet|WLAN)\b",
        ["Es könnte ein Problem mit deiner Internetverbindung geben. Versuche, den Router neu zu starten und prüfe, ob alle Kabel richtig angeschlossen sind."]
    ],
    [
        r"(.*)\b(Drucker|ausdrucken)\b",
        ["Stelle sicher, dass der Drucker eingeschaltet ist und die neuesten Treiber installiert sind. Überprüfe auch die Druckwarteschlange und starte sie gegebenenfalls neu."]
    ],
    [
        r"(.*)\b(E-Mail|Outlook)\b",
        ["Überprüfe deine E-Mail-Kontoeinstellungen in Outlook und stellen sicher, dass du mit dem Internet verbunden bist. Wenn das Problem weiterhin besteht, kontaktiere bitte unseren IT-Support."]
    ],
    [
        r"(.*)\b(Passwort|Anmeldung)\b",
        ["Wenn du Probleme mit deinem Passwort oder bei der Anmeldung hast, kontaktiere bitte unseren IT-Support. Sie werden dir gerne weiterhelfen."]
    ],
    [
        r"(.*)\b(Datei|gelöscht|wiederherstellen)\b",
        ["In einigen Fällen können gelöschte Dateien wiederhergestellt werden. Bitte überprüfen Sie den Papierkorb auf Ihrem Computer, ob die Datei dort abgelegt wurde. Wenn nicht, könnten wir versuchen, Datenwiederherstellungssoftware zu verwenden, um die Datei wiederherzustellen."]
    ],
    [
        r"(.*)\b(startet|starten|hochfahren|Hochfahren)\b",
        ["Bitte überprüfen Sie zunächst, ob der Computer ordnungsgemäß mit Strom versorgt wird. Stellen Sie sicher, dass alle Kabel richtig angeschlossen sind. Versuchen Sie, den Computer neu zu starten und beobachten Sie, ob Fehlermeldungen angezeigt werden. Wenn das Problem weiterhin besteht, wenden Sie sich bitte an unseren IT-Support."]
    ],
    [
        r".*",
        ["Ich kann leider keine direkte Antwort auf deine Frage finden. \n\nEventuell hast du dich verschrieben? \n\nVersuch deine Frage anders zu formuliere, möglicherweise helfen dir Stichworte wie 'Drucker', 'WLAN', 'Internet' oder 'E-Mail' weiter. \n\nBesteht dein Problem weiterhin? Klicke auf Yes um dir die Kontakdaten eines Mitarbeiters anzuzeigen."]
    ]
]

# Initialisiere den Chatbot
chatbot = Chat(pairs, reflections)

# Funktion zum Anzeigen der Chatbot-Antworten
def display_response():
    global entry  # Zugriff auf die globale Variable entry
    user_input = entry.get()  # Benutzereingabe abrufen

    if user_input.lower() in ["tschüss", "auf wiedersehen", "bye"]:
        messagebox.showinfo("Chatbot", "Auf Wiedersehen!")
        root.quit()
    else:
        response = chatbot.respond(user_input)
        if response.startswith("Ich kann leider keine direkte Antwort auf deine Frage finden"):
            answer = messagebox.askquestion("Whoops!", response)
            if answer == 'yes':
                messagebox.showinfo("Kontaktinformationen IT-Support", "\n\nTelefon: 123456789\n\nE-Mail: support@win.de")
            insert_data(user_name, user_id, user_input)
        else:
            messagebox.showinfo("Chatbot", response)
            
# Funktion zum Fortfahren nach der Eingabe von Namen und ID
def proceed():
    global welcome_label  # Zugriff auf die globale Variable welcome_label
    global user_name
    user_name = name_entry.get()
    global user_id
    user_id = id_entry.get()
    
    if user_name == "" or user_id == "": # Hinweisfenster wenn die Namens und ID Eingabe falsch ist
        messagebox.showwarning("Fehlende Informationen", "Bitte gib deinen Namen und deine ID ein.")
        return
    
    # Entferne Eingabefelder für Name und ID
    name_label.destroy()
    name_entry.destroy()
    id_label.destroy()
    id_entry.destroy()
    proceed_button.destroy()

    welcome_message = "\nHallo, " + user_name + "! Wie kann ich dir helfen?\n"
    welcome_label.config(text=welcome_message)

    # Eingabefeld für Benutzerfrage
    global entry  # Zugriff auf die globale Variable entry
    entry = tk.Entry(root, width=50)
    entry.pack(pady=5)

    # Antwort-Button
    antwort_button = tk.Button(root, text="Antwort anzeigen", command=display_response)
    antwort_button.pack(pady=5)

# Erstellen der GUI
root = tk.Tk()
root.title("IT-Support Chatbot")

# Willkommensnachricht
welcome_label = tk.Label(root, text="\nWillkommen beim Support-Chatbot der Solutions IT!\n")
welcome_label.pack(pady=10)

# Eingabefeld für den Namen
name_label = tk.Label(root, text="Bitte gib deinen Namen ein:")
name_label.pack()
name_entry = tk.Entry(root, width=50)
name_entry.pack(pady=5)

# Eingabefeld für die ID
id_label = tk.Label(root, text="Bitte gib deine ID ein:")
id_label.pack()
id_entry = tk.Entry(root, width=50)
id_entry.pack(pady=5)

# Weiter-Button nach Eingabe von Namen und ID
proceed_button = tk.Button(root, text="Weiter", command=proceed)
proceed_button.pack(pady=5)

# Beenden-Button
quit_button = tk.Button(root, text="Beenden", command=root.destroy)
quit_button.pack(pady=5)

# GUI starten
root.mainloop()


