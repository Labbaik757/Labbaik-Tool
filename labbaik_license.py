#!/usr/bin/env python3

# ========================== MAAZ TOOL LICENSE SCRIPT (labbaik_license.py) ==========================

import os
import sys
import time
import base64
import requests
import subprocess
from datetime import datetime

# --- Dependency Check ---
try:
    from rich.console import Console
    from rich.panel import Panel
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    print("="*70)
    print("🚨 WARNING: The 'rich' library is not installed. Visual formatting will be basic.")
    print("To install it, run: pip install rich")
    print("="*70)
    class Console:
        def print(self, *args, **kwargs):
            print(" ".join(str(a) for a in args))
        def rule(self, *args, **kwargs):
            print("-" * 70)
    class Panel:
        @staticmethod
        def fit(content, title=None, border_style=None):
            return f"\n--- {title} ---\n{content}\n" if title else f"\n{content}\n"

console = Console()

# --- Banner ---
BANNER = """[bold cyan]
 ███████╗ █████╗ ███████╗███████╗
 ██╔════╝██╔══██╗╚══███╔╝██╔════╝
 █████╗  ███████║  ███╔╝ █████╗
 ██╔══╝  ██╔══██║ ███╔╝  ██╔══╝
 ██║     ██║  ██║███████╗███████╗
 ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
 🔰 MAAZ TOOL 🔰
[/bold cyan]"""

if RICH_AVAILABLE:
    console.print(Panel.fit(BANNER, title="License Verification", border_style="cyan"))
else:
    print("="*70)
    print("MAAZ TOOL - License Verification")
    print(BANNER.replace("[bold cyan]", "").replace("[/bold cyan]", ""))
    print("="*70)

# --- GitHub Config ---
GITHUB_USER = "Labbaik757"
REPO_NAME = "Labbaik-Official"
FILE_PATH = "keys/approved_keys.txt"
RAW_KEYS_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/main/{FILE_PATH}"
GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/contents/{FILE_PATH}"
GITHUB_TOKEN = "ghp_yourGitHubTokenHere"  # Replace this before running
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

# --- Local Files ---
KEY_FILE = ".maaz_key.txt"
LOG_FILE = "maaz_logs.txt"
CLONE_SCRIPT = "clone_module.py"

# ========================== FUNCTIONS ==========================

def fetch_key_list():
    try:
        res = requests.get(RAW_KEYS_URL)
        if res.status_code == 404:
            print("❌ Key file not found on GitHub. Creating it...")
            create_github_file(FILE_PATH, "")
            return []
        elif res.ok:
            return res.text.strip().splitlines()
        else:
            print(f"⚠️ GitHub fetch error {res.status_code}: {res.text}")
            return []
    except Exception as e:
        print(f"❌ Error fetching keys: {e}")
        return []

def create_github_file(path, content):
    try:
        encoded = base64.b64encode(content.encode()).decode()
        payload = {
            "message": f"Auto-created: {path}",
            "content": encoded
        }
        res = requests.put(f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/contents/{path}", headers=HEADERS, json=payload)
        if res.status_code in [200, 201]:
            print(f"✅ Created file '{path}' on GitHub.")
        else:
            print(f"⚠️ Failed to create file. GitHub says: {res.status_code} - {res.text}")
    except Exception as e:
        print(f"❌ Error creating file on GitHub: {e}")

def clean_expired_keys(lines):
    today = datetime.today().date()
    valid = []
    for line in lines:
        try:
            key, exp = line.strip().split("|")
            if datetime.strptime(exp, "%Y-%m-%d").date() >= today:
                valid.append(f"{key.strip()}|{exp.strip()}")
        except Exception:
            continue
    return valid

def get_file_sha():
    try:
        res = requests.get(GITHUB_API_URL, headers=HEADERS)
        res.raise_for_status()
        return res.json().get("sha")
    except Exception as e:
        print(f"❌ Failed to get SHA: {e}")
        return None

def update_github_key_file(valid_keys, sha):
    try:
        content = "\n".join(valid_keys)
        encoded = base64.b64encode(content.encode()).decode()
        payload = {
            "message": "Auto-clean expired keys",
            "content": encoded,
            "sha": sha
        }
        res = requests.put(GITHUB_API_URL, headers=HEADERS, json=payload)
        if res.status_code == 200:
            print("✅ Updated approved_keys.txt with valid keys.")
        else:
            print(f"⚠️ Failed to update file: {res.status_code} - {res.text}")
    except Exception as e:
        print(f"❌ Error updating GitHub file: {e}")

def auto_remove_expired_keys():
    keys = fetch_key_list()
    valid_keys = clean_expired_keys(keys)
    if len(valid_keys) < len(keys):
        sha = get_file_sha()
        if sha:
            update_github_key_file(valid_keys, sha)

def ensure_required_files():
    if not os.path.exists(KEY_FILE):
        key = f"MAAZ-{str(int(time.time()))[-6:]}"
        with open(KEY_FILE, "w") as f:
            f.write(key)
        print(f"✅ Generated new key: {key}")

    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("")
        print(f"✅ Created log file: {LOG_FILE}")

    if not os.path.exists(CLONE_SCRIPT):
        with open(CLONE_SCRIPT, "w") as f:
            f.write("print('Placeholder for clone_module.py')\n")
        print(f"✅ Created placeholder: {CLONE_SCRIPT}")

def check_key_approval(local_key, key_list):
    today = datetime.today().date()
    for line in key_list:
        try:
            key, exp = line.strip().split("|")
            if key.strip() == local_key:
                return datetime.strptime(exp.strip(), "%Y-%m-%d").date() >= today
        except:
            continue
    return False

def get_ip():
    try:
        return requests.get("https://api.ipify.org").text.strip()
    except:
        return "UNKNOWN_IP"

def log_user_data(key):
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"{key} | {get_ip()} | {datetime.now()}\n")
        print(f"✅ Logged usage for key: {key}")
    except Exception as e:
        print(f"❌ Logging failed: {e}")

# ========================== MAIN ==========================

def main():
    ensure_required_files()

    try:
        with open(KEY_FILE, "r") as f:
            key = f.read().strip()
    except Exception as e:
        print(f"❌ Cannot read key file: {e}")
        return

    if not key:
        print("❌ No license key found. Delete the file and restart to regenerate.")
        return

    if "yourGitHubTokenHere" in GITHUB_TOKEN:
        console.print("[bold red]❌ GitHub Token is not set. Please add your token in the script.[/bold red]" if RICH_AVAILABLE else "❌ GitHub token missing!")
        return

    print("🧹 Checking for expired keys...")
    auto_remove_expired_keys()

    print(f"🔐 Verifying license: {key}")
    while True:
        approved = fetch_key_list()
        if check_key_approval(key, approved):
            print("✅ License Approved! Access Granted.")
            log_user_data(key)
            if os.path.exists(CLONE_SCRIPT):
                print("🚀 Launching Cloning Module...")
                try:
                    subprocess.run([sys.executable, CLONE_SCRIPT], check=True)
                except Exception as e:
                    print(f"❌ Failed to run cloning module: {e}")
            break
        else:
            print("⏳ Key not yet approved or expired. Retrying in 20 seconds...")
            time.sleep(20)

if __name__ == "__main__":
    main()
