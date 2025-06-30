#!/usr/bin/env python3
from __future__ import annotations
"""AI Terminal Assistant

Now supports **Gemini** (Google Generative AI) as a free/cheap backend in
addition to OpenAI.

Features:
- Process scanning (LLM‑aided)
- Project health check
- File search
- Chat assistant (`ait chat`) with either OpenAI **or** Gemini
- Basic system diagnostics (battery, CPU, memory)
- Optional web search integration

Configuration (any of the following in **~/.ait.yml**):
```yaml
# ---- choose ONE backend ----
# For OpenAI
openai_api_key: "sk-..."
openai_model: "gpt-4o-mini"

# For Gemini (Google Generative AI)
gemini_api_key: "AIza..."
gemini_model: "gemini-1.5-flash"
```
If both keys exist, **Gemini takes priority** (cheaper / free tier).

Author: Abhi Singh
License: MIT
"""

import argparse
import pathlib
from dataclasses import dataclass
from typing import Any, Dict, List

import psutil
import requests
import yaml
from bs4 import BeautifulSoup
from rich.console import Console

# ---------------------------------------------------------------------------
# Optional LLM back‑ends
# ---------------------------------------------------------------------------
try:
    import google.generativeai as genai  # type: ignore
except ImportError:
    genai = None

try:
    from openai import OpenAI  # type: ignore[attr-defined]
except ImportError:
    OpenAI = None  # type: ignore

# ---------------------------------------------------------------------------
# Globals & config
# ---------------------------------------------------------------------------
CONFIG_PATH = pathlib.Path.home() / ".ait.yml"
console = Console()


def load_config() -> Dict[str, Any]:
    if CONFIG_PATH.exists():
        return yaml.safe_load(CONFIG_PATH.read_text()) or {}
    return {}

CONFIG = load_config()

# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class ProcessInfo:
    pid: int
    name: str
    cmdline: str
    path: str
    user: str
    suspicious: bool | None = None

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_llm_client():
    if genai and CONFIG.get("gemini_api_key"):
        genai.configure(api_key=CONFIG["gemini_api_key"])
        return "gemini", genai, CONFIG.get("gemini_model", "gemini-1.5-flash")
    if OpenAI and CONFIG.get("openai_api_key"):
        client = OpenAI(api_key=CONFIG["openai_api_key"], base_url=CONFIG.get("openai_base_url"))
        return "openai", client, CONFIG.get("openai_model", "gpt-3.5-turbo")
    return None, None, None

# ---------------------------------------------------------------------------
# ASCII banner
# ---------------------------------------------------------------------------

def print_banner() -> None:
    banner = r'''           ,..-,
         ,;;f^^"""""-._
        ;;'          `-.
       ;/               `.
       ||  _______________\_______________________
       ||  |AI TERMINAL by anodeus @github.com    |
       ||  |--------------------------------------|
        |  |OSINT | SEC TOOLS | CHAT | SCANS |    |
        |  |Custom GPT + Gemini CLI Assistant     |
        `| |______________________________________|
         \ |--------------------------------------|
           |____ ASCII SHELL INITIALIZED _________|
           |  System ready. Modules loaded.       |
           |  Type `ait chat` to start assistant. |
           |______________________________________|

[---]           AI Terminal Assistant: anodeus         [---]
[---]           Created by: Abhi Singh (anodeus)        [---]
[---]       Intelligence & Recon CLI Utility            [---]
             Powered by OpenAI + Gemini Models
    One interface. Many capabilities. Your command.

     github.com/anodeus | linuxbox.local | v1.0.0'''
    console.print(banner, style="bold green")

# ---------------------------------------------------------------------------
# System health
# ---------------------------------------------------------------------------

def sys_health() -> None:
    console.print("[cyan]System Health[/cyan]")
    bat = psutil.sensors_battery()
    if bat:
        console.print(f"Battery: {bat.percent}% {'(Charging)' if bat.power_plugged else '(Discharging)'}")
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    console.print(f"CPU {cpu}% | MEM {mem.percent}% | DISK {disk.percent}%")

# ---------------------------------------------------------------------------
# Web search
# ---------------------------------------------------------------------------

def web_search(q: str) -> str:
    try:
        url = "https://duckduckgo.com/html/?q=" + requests.utils.quote(q)
        html = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10).text
        soup = BeautifulSoup(html, "html.parser")
        res = soup.find("a", class_="result__a")
        return res.text.strip() if res else "No result found."
    except Exception as e:
        return f"Search error: {e}"

# ---------------------------------------------------------------------------
# File finder
# ---------------------------------------------------------------------------

def find_file(pattern: str, root: pathlib.Path = pathlib.Path.home()) -> List[pathlib.Path]:
    """Recursively search for files matching pattern under root."""
    return list(root.rglob(pattern))

# ---------------------------------------------------------------------------
# Chat loop
# ---------------------------------------------------------------------------

def chat() -> None:
    print_banner()
    backend, client, model = get_llm_client()
    if backend is None:
        console.print("[red]No LLM configured in ~/.ait.yml[/red]")
        return

    console.print(f"[green]Chatting via {backend.upper()} ({model})[/green]")
    if backend == "gemini":
        chat_session = client.GenerativeModel(model).start_chat()
    history: List[Dict[str, str]] = []

    while True:
        try:
            user = input("[abhi] > ").strip()
        except KeyboardInterrupt:
            break
        if user.lower() in {"exit", "quit"}: break

        # Handle built‑in commands
        if user.startswith("file find "):
            pattern = user[len("file find "):].strip()
            console.print(f"[yellow]Searching for '{pattern}' ...[/yellow]")
            matches = find_file(pattern)
            if matches:
                for p in matches[:100]:  # limit output
                    console.print(str(p))
                if len(matches) > 100:
                    console.print(f"[grey70]...and {len(matches)-100} more[/grey70]")
            else:
                console.print("[red]No files found.[/red]")
            continue
        if "health" in user or "battery" in user:
            sys_health(); continue
        if user.startswith("search"):
            console.print("[yellow]Searching web...[/yellow]")
            console.print("[green]Web:[/green] " + web_search(user[6:].strip()))
            continue

        # AI interaction
        if backend == "gemini":
            reply = chat_session.send_message(user).text.strip()
        else:
            history.append({"role": "user", "content": user})
            resp = client.chat.completions.create(model=model, messages=history)
            reply = resp.choices[0].message.content.strip()
            history.append({"role": "assistant", "content": reply})
        console.print(f"[blue]AI:[/blue] {reply}")
# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("cmd", choices=["chat"])
    args = p.parse_args()
    if args.cmd == "chat":
        chat()

if __name__ == "__main__":
    main()
