import unittest
from unittest.mock import patch
import tkinter as tk
import chatbot

class TestChatbot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = tk.Tk()
        cls.root.withdraw()

    @classmethod
    def tearDownClass(cls):
        cls.root.destroy()

    @patch('tkinter.messagebox.askquestion')
    @patch('tkinter.messagebox.showinfo')
    def test_display_response_with_yes_answer(self, mock_showinfo, mock_askquestion):
        mock_askquestion.return_value = 'yes'
        entry = tk.Entry(self.root)
        chatbot.entry = entry

        chatbot.display_response()

        mock_showinfo.assert_called_once_with(
            "Kontaktinformationen IT-Support",
            "\n\nTelefon: 123456789\n\nE-Mail: support@win.de"
        )
        mock_askquestion.assert_called_once_with("Whoops!", mock_askquestion.call_args[0][1])

    @patch('tkinter.messagebox.askquestion')
    @patch('tkinter.messagebox.showinfo')
    def test_display_response_with_no_answer(self, mock_showinfo, mock_askquestion):
        mock_askquestion.return_value = 'no'
        entry = tk.Entry(self.root)
        chatbot.entry = entry

        chatbot.display_response()

        mock_showinfo.assert_called_once_with(
            "Chatbot",
            mock_showinfo.call_args[0][1]
        )
        mock_askquestion.assert_called_once_with("Whoops!", mock_askquestion.call_args[0][1])

    @patch('tkinter.messagebox.showwarning')
    def test_proceed_with_missing_information(self, mock_showwarning):
        name_entry = tk.Entry(self.root)
        id_entry = tk.Entry(self.root)
        proceed_button = tk.Button(self.root)

        chatbot.name_entry = name_entry
        chatbot.id_entry = id_entry
        chatbot.proceed_button = proceed_button

        chatbot.proceed()

        mock_showwarning.assert_called_once_with(
            "Fehlende Informationen",
            "Bitte gib deinen Namen und deine ID ein."
        )

if __name__ == '__main__':
    unittest.main()

