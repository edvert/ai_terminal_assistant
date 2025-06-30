# AI Terminal Assistant
* © 2025  
* Written by: Abhi Singh (anodeus)  
* Project: [AI Terminal](https://github.com/anodeus/ai-terminal)

<br/>

## Description
AI Terminal is an open-source command-line assistant designed for security researchers, ethical hackers, and developers. It combines the power of modern LLMs (OpenAI and Gemini) with practical system tools like file search, system diagnostics, process scanning, and web search — all in a terminal-first workflow.

AI Terminal is developed as a personal project and learning tool by Abhi Singh. It aims to provide a flexible, scriptable interface for rapid automation and interaction with LLMs.

DISCLAIMER: This is *only* for educational and research purposes. Do not use this for malicious or unauthorized activities.  
Please refer to the LICENSE file for licensing details.

#### Supported platforms:
* Linux (Kali, Ubuntu, etc.)
* macOS (with Python 3.8+ and `venv`)
* WSL2 (Windows Subsystem for Linux)

<br/>

# Installation

## Install via install.sh (Recommended)

```bash
git clone https://github.com/anodeus/ai-terminal.git
cd ai-terminal
./install.sh

This script:

    Creates a virtual environment named aienv/

    Installs all dependencies from requirements.txt

<br/>
Manual Setup

python3 -m venv aienv
source aienv/bin/activate
pip install -r requirements.txt

To run the assistant:

./ait.py chat

<br/>
Configuration

Create a file in your home directory named .ait.yml:

# ~/.ait.yml

gemini_api_key: your-gemini-api-key
gemini_model: gemini-1.5-flash

openai_api_key: your-openai-api-key
openai_model: gpt-3.5-turbo

    ⚠️ Warning: Keep this file secret. Do not upload it to GitHub.

<br/>
Basic Usage

./ait.py chat             # start chat assistant
./ait.py health           # system diagnostics
./ait.py ps               # process scanner
./ait.py find notes.txt   # search files by name
./ait.py search "best VPN for Kali Linux"

<br/>
AI Terminal Tools

    chat – OpenAI or Gemini-based assistant

    health – CPU, battery, memory, and disk status

    ps – List and inspect system processes

    find – Search for files recursively

    search – DuckDuckGo-based quick search

<br/>
Bugs and Suggestions

Please open an issue on GitHub if you encounter bugs or have suggestions for improvement.
<br/>
License

AI Terminal is released under the MIT License.
See the LICENSE file for more detail.
