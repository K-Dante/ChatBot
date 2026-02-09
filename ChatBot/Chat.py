import sys
from queue import Queue
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QIcon, QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QTextEdit, QPushButton, QLabel
from PyQt6.QtCore import QThread, pyqtSignal
from openai import OpenAI

class ChatGPT(QThread):
    message_received = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.queue = Queue()
        self.openai_api_key = " "
        self.conversation = []

    def run(self):
        while True:
            user_input = self.queue.get()
            self.message_received.emit("You: " + user_input)  
            self.conversation.append({"role": "system", "content": "You are a helpful assistant."})
            self.conversation.append({"role": "user", "content": user_input})

            response = self.get_chatbot_response()
            self.message_received.emit("Kartiar: " + response)
            self.conversation.append({"role": "assistant", "content": response})

    def get_chatbot_response(self):
        client = OpenAI(api_key=self.openai_api_key)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.conversation,
            max_tokens=50,
            temperature=0.7
        )

        return response.choices[0].message.content.strip()

class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("__Kartiar__")
        self.setWindowIcon(QIcon("AU.png"))
        window_width = 820
        window_height = 350
        self.setGeometry(100, 100, window_width, window_height)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QHBoxLayout(self.central_widget)

        self.chat_layout = QVBoxLayout()
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_layout.addWidget(self.chat_display)

        self.user_input = QLineEdit()
        self.chat_layout.addWidget(self.user_input)

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)
        self.chat_layout.addWidget(self.send_button)

        self.layout.addLayout(self.chat_layout)

        self.logo_widget = QWidget()
        logo_layout = QVBoxLayout(self.logo_widget)
        self.logo_label = QLabel()
        self.logo_label.setPixmap(QPixmap("AU.png"))
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo_layout.addWidget(self.logo_label)

        self.title_label = QLabel("\n___Kartiar___\n____________")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setPointSize(22)
        font.setItalic(True)
        self.title_label.setFont(font)
        logo_layout.addWidget(self.title_label)

        self.layout.addWidget(self.logo_widget)

        self.chat_gpt = ChatGPT()
        self.chat_gpt.message_received.connect(self.display_message)
        self.chat_gpt.start()

    def send_message(self):
        user_input = self.user_input.text()  
        self.chat_gpt.queue.put(user_input)

    def display_message(self, message):
        self.chat_display.append(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chat_window = ChatWindow()
    chat_window.show()
    sys.exit(app.exec())

