Kartiar: Desktop AI Assistant
Kartiar is a sleek, Python-based desktop application that provides a graphical user interface (GUI) for interacting with OpenAI's GPT models. Built with PyQt6, it features a multi-threaded architecture to ensure the UI remains responsive while the AI generates responses.

🚀 Features

Real-time Chat: Interactive chat interface with message history.

Asynchronous Processing: Uses QThread and Queue to handle API calls in the background, preventing the window from freezing.

Persistent Context: Maintains conversation history for the duration of the session to allow for follow-up questions.

Custom Branding: Integrated logo and stylized titles for a unique desktop experience.

🛠️ Prerequisites

Before running the application, ensure you have the following installed:

Python 3.8 or higher

An OpenAI API Key

📦 Installation

1.**Clone the repository:**

git clone https://github.com/yourusername/kartiar.git

cd kartiar

2.**Install dependencies:**

pip install PyQt6 openai

3.**Setup Assets:** Ensure you have an image file named AU.png in the root directory for the window icon and logo to display correctly.

**🚦 How to Use**
  1.Open the main script and replace the self.openai_api_key value with your actual API key (or better yet, use an environment variable).

  2.Run the application:

  python main.py

  3.Type your message in the text box at the bottom and click Send.

  4.Wait for Kartiar to respond!








