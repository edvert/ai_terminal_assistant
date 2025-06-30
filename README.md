# 🧠 AI Terminal Assistant

**AI Terminal** is a command-line AI utility developed by **Abhi Singh** (`@anodeus`).  
It acts as a lightweight assistant powered by OpenAI and Google Gemini — bundled with system tools like process scanning, diagnostics, file search, and optional web search.

## 🚀 Features

- ✨ Chat assistant using OpenAI or Gemini LLMs  
- 📂 Recursive file finder  
- 🔍 Web search via DuckDuckGo  
- 🧪 System health monitor (CPU, memory, battery, disk)  
- 🧠 Process scanner (with command-line inspection)  
- 💡 Smart shell commands like `file find`, `ps scan`, `health`, etc.  
- 👨‍💻 Fully offline-friendly (unless chat/web features are used)

## 📦 Installation

```bash
git clone https://github.com/anodeus/ai-terminal.git
cd ai-terminal
./install.sh

This script will:

    Create a virtual environment (aienv/)

    Install all dependencies from requirements.txt

⚙️ Configuration: ~/.ait.yml

Create a config file in your home directory to store your API keys:

gemini_api_key: your-gemini-api-key
gemini_model: gemini-1.5-flash

openai_api_key: your-openai-api-key
openai_model: gpt-3.5-turbo

    🛡️ Keep this file secret. Add .ait.yml to your .gitignore.

💬 Usage

source aienv/bin/activate
./ait.py chat

Quick tools:

./ait.py health
./ait.py ps
./ait.py find password.txt
./ait.py search "Kali Linux tips"

📁 Project Structure

ai-terminal/
├── ait.py
├── config.py
├── modules/
│   ├── diagnostics.py
│   ├── file_search.py
│   ├── process_scan.py
│   └── web_search.py
├── ascii/
│   └── banner.txt
├── install.sh
├── requirements.txt
├── README.md
└── LICENSE

📜 License

MIT License
© 2025 Abhi Singh (@anodeus)


Let me know if you'd like this as a downloadable `README.md` file or also want `.ait.yml.example`
