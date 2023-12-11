from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.setMinimumSize(700, 500)

        # Add Chat Area
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Add input field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)

        # Add Button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)

        self.show()

class Chatbot:
    pass

app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())