#!/usr/bin/env python3
# -- coding: utf-8 --

import os
import sys
import time
import uuid
import json
import requests
import base64
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

# GitHub Raw Key File & Logs Config
APPROVED_KEYS_URL = "https://raw.githubusercontent.com/Labbaik757/Labbaik-Official/main/keys/approved_keys.txt"
LOG_UPLOAD_REPO = "Labbaik757/labbaik-logs"
LOG_UPLOAD_PATH = "logs.txt"
GITHUB_TOKEN = "ghp_xxxREPLACEMExxx"

# Banner
BANNER = """[bold cyan]
███████╗ █████╗ ███████╗███████╗
██╔════╝██╔══██╗╚══███╔╝██╔════╝
█████╗  ███████║  ███╔╝ █████╗  
██╔══╝  ██╔══██║ ███╔╝  ██╔══╝  
██║     ██║  ██║███████╗███████╗
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
     🔰 MAAZ TOOL 🔰
[/bold cyan]"""

def show_banner():
    console.print(Panel(BANNER, style="bold cyan"))

def fetch_approved_keys():
    try:
        response = requests.get(APPROVED_KEYS_URL)
        if response.status_code == 200:
            return response.text.splitlines()
        return []
    except:
        return []

def is_key_valid(user_key):
    approved_keys = fetch_approved_keys()
    for line in approved_keys:
        if line.strip() == user_key.strip():
            return True
    return False

def upload_log(username, key):
    try:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ip = requests.get("https://api.ipify.org").text.strip()
        log_line = f"[{now}] USERNAME: {username} | IP: {ip} | KEY: {key}\n"

        url = f"https://api.github.com/repos/{LOG_UPLOAD_REPO}/contents/{LOG_UPLOAD_PATH}"
        headers = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        }

        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            sha = res.json()['sha']
            old_content = requests.get(res.json()['download_url']).text
            updated_content = old_content + log_line
        else:
            sha = None
            updated_content = log_line

        encoded = base64.b64encode(updated_content.encode()).decode()

        data = {
            "message": "Update logs.txt",
            "content": encoded,
            "branch": "main"
        }
        if sha:
            data["sha"] = sha

        requests.put(url, headers=headers, json=data)
    except:
        pass

def get_env_or_warn(env_var, prompt_text):
    value = os.environ.get(env_var)
    if value is not None:
        return value.strip()
    else:
        console.print(f"[bold yellow]⚠️ Environment variable '{env_var}' not found. Skipping input in non-interactive environment.[/bold yellow]")
        return None

def dashboard(username, key):
    os.system('clear' if os.name == 'posix' else 'cls')
    show_banner()
    console.print(f"[bold green]\U0001f9d1 User:[/bold green] [yellow]{username}[/yellow]")
    console.print(f"[bold green]\U0001f510 Your Key:[/bold green] [yellow]{key}[/yellow]")
    console.print("\n[bold magenta]Choose Cloning Method:[/bold magenta]\n")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Option")
    table.add_column("Method")
    table.add_row("1", "OLD METHOD")
    table.add_row("2", "SERIES METHOD")
    table.add_row("3", "RANDOM METHOD")
    table.add_row("4", "COMBO GENERATOR")
    table.add_row("5", "UID DUMP")
    table.add_row("0", "Exit")
    console.print(table)

    opt = os.environ.get("CLONE_OPTION")
    if opt is None:
        console.print("[bold yellow]⚠️ Environment variable 'CLONE_OPTION' not set. Defaulting to '0' (exit).[/bold yellow]")
        opt = "0"

    opt = opt.strip()
    if opt == "0":
        console.print("[bold red]👋 Exiting...[/bold red]")
        return
    elif opt in ["1", "2", "3", "4", "5"]:
        os.system(f"python clone_module.py {opt}")
    else:
        console.print("[bold red]❌ Invalid option selected.[/bold red]")

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    show_banner()
    console.print("[bold green]\U0001f511 Enter your license key to continue...[/bold green]")

    user_key = get_env_or_warn("MAAZ_LICENSE_KEY", "🔐 Enter License Key: ")
    if not user_key:
        console.print("[bold red]❌ No license key provided. Exiting.[/bold red]")
        return

    if is_key_valid(user_key):
        username = os.getenv("USERNAME") or os.getenv("USER") or "User"
        upload_log(username, user_key)
        dashboard(username, user_key)
    else:
        console.print("[bold red]❌ Invalid or unapproved key! Contact admin.[/bold red]")
        console.print("\n[bold yellow]📞 Contact:[/bold yellow] WhatsApp +923079741690 or Telegram @LabbaikSupport")

if __name__ == "__main__":
    main()
