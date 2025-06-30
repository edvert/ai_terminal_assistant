🤖 AI Terminal Assistant

Note: This project is superseded by boukeversteegh/ai-terminal-assistant-go.

AI Terminal Assistant is a powerful command-line tool that revolutionizes your terminal interactions by allowing you to use natural language to generate and execute shell commands. Leveraging the capabilities of OpenAI's GPT-3.5-turbo model, it translates your everyday instructions into precise Bash or PowerShell commands, making complex terminal tasks simple and intuitive.
✨ Features

    Natural Language to Shell Commands: Transform your natural language instructions into executable Bash or PowerShell commands.

    Human-Friendly Explanations: Get clear, concise explanations for generated commands in the form of comments, helping you understand what each command does.

    Automatic Command Typing: The generated commands are automatically typed into your terminal, ready for execution.

    Pre-execution Review: You have the flexibility to edit the command before executing it or cancel with Ctrl+C.

    Seamless Terminal Integration: Suggested commands are fully integrated with terminal features like Bash expansion, history, and pipes.

    Cross-Platform Support: Works flawlessly on both Bash (Linux/macOS) and PowerShell (Windows).

    Contextual Understanding: Pipe additional context to the AI using stdin for more intelligent and relevant command suggestions.

🚀 Examples
Bash

$ ai find files containing the text hello world
# 🤖 Search for files containing the text "hello world" recursively in the current directory.
$ grep -rli "hello world" .

$ ai list files by size
# 🤖 List all files in the current directory sorted by size (largest to smallest).
$ ls -lS

$ ai compress all png files in the current directory
# 🤖 Compress all PNG files in the current directory using tar and gzip.
$ tar -czf png_files.tar.gz *.png



PowerShell

PS C:\Users\jdoe> ai how much free disk space in mb?
# 🤖 Show free disk space for all drives in megabytes (MB).
PS C:\Users\jdoe> Get-PSDrive -PSProvider FileSystem | Select-Object Name, @{Name="FreeSpaceMB"; Expression={$_.Free / 1MB -as [int]}}



Contextual Usage with Pipes

$ ls | ai organize these files semantically
# 🤖 Based on the file names, I suggest the following directory structure:
# mkdir Documents Media Pictures Programs
# mkdir Documents/Work Documents/Personal
# mkdir Media/Movies Media/TV\ Shows Media/Videos Media/Music
# mkdir Pictures/Family Pictures/Vacation Pictures/Wedding
# mkdir



🛠️ Setup

To get started with AI Terminal Assistant, follow these simple steps:

    Clone the repository:

    git clone https://github.com/edvert/ai_terminal_assistant.git
    cd ai_terminal_assistant



    Install dependencies:

    pip install -r requirements.txt



    Set up your OpenAI API Key:
    You need an OpenAI API key to use this tool. Set it as an environment variable:

    For Bash/Zsh (Linux/macOS):

    export OPENAI_API_KEY="your_api_key_here"



    For PowerShell (Windows):

    $env:OPENAI_API_KEY = "your_api_key_here"



    Replace "your_api_key_here" with your actual OpenAI API key.

💡 Usage

To use the AI Terminal Assistant, simply type the ai command followed by your natural language instruction:

$ ai list all files in the current directory



The AI Terminal Assistant will generate a shell command based on your instruction and automatically type it into your terminal. You can then press Enter to execute it, edit it, or press Ctrl+C to cancel.
⚠️ Limitations

While AI Terminal Assistant strives to provide accurate and useful shell commands, it relies on an AI model that may occasionally produce incorrect or unexpected output. Always review the generated commands and comments before executing them, especially when using commands that could modify or delete important data.
🤝 Contributing

We welcome contributions to improve the AI Terminal Assistant! Here are some ways you can contribute:

    Report bugs and issues: If you find any bugs or encounter unexpected behavior, please open an issue on GitHub.

    Suggest improvements or new features: Have an idea for a new feature or a way to improve existing ones? Let us know by opening an issue.

    Contribute to the codebase: Feel free to fork the repository, make your changes, and submit a pull request.

    Help with testing and documentation: Assist in testing new features or improving the project's documentation.

    Share your feedback and experiences: Your feedback is valuable! Share how you're using the AI Terminal Assistant and any suggestions you have.

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
📧 Contact

If you have any questions or suggestions, feel free to open an issue on this repository.
