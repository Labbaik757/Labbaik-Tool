#!/usr/bin/env python3

========== MAAZ TOOL LICENSE SCRIPT (labbaik_license.py) ==========

import os, requests, time, base64, subprocess from datetime import datetime from rich.console import Console from rich.panel import Panel

console = Console()

Display Banner

BANNER = """[bold cyan] ███████╗ █████╗ ███████╗███████╗ ██╔════╝██╔══██╗╚══███╔╝██╔════╝ █████╗  ███████║  ███╔╝ █████╗
██╔══╝  ██╔══██║ ███╔╝  ██╔══╝
██║     ██║  ██║███████╗███████╗ ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ 🔰 MAAZ TOOL 🔰 """ console.print(Panel.fit(BANNER, title="License Verification", border_style="cyan"))

GitHub Config

GITHUB_USER = "Labbaik757" REPO_NAME = "Labbaik-Official" FILE_PATH = "keys/approved_keys.txt" RAW_KEYS_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/main/{FILE_PATH}" GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/contents/{FILE_PATH}" GITHUB_TOKEN = "ghp_yourGitHubTokenHere"  # 🔐 Replace with actual token HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

KEY_FILE = ".maaz_key.txt" LOG_FILE = "maaz_logs.txt" CLONE_SCRIPT = "clone_module.py"

========== License System Functions ==========

def fetch_key_list(): try: res = requests.get(RAW_KEYS_URL) if res.status_code == 404: print("❌ GitHub key file missing. Auto-creating...") create_github_file(FILE_PATH, "") return [] return res.text.strip().splitlines() if res.status_code == 200 else [] except Exception as e: print("❌ Error loading keys:", e) return []

def create_github_file(path, content): try: api_path = f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/contents/{path}" encoded = base64.b64encode(content.encode()).decode() payload = { "message": f"🆕 Auto-created missing file: {path}", "content": encoded } res = requests.put(api_path, headers=HEADERS, json=payload) if res.status_code in [200, 201]: print(f"✅ Created '{path}' on GitHub.") else: print("⚠️ Could not create GitHub file:", res.text) except Exception as e: print("❌ Error creating GitHub file:", e)

def clean_expired_keys(lines): valid = [] today = datetime.today().date() for line in lines: try: key, expiry = line.strip().split("|") if datetime.strptime(expiry.strip(), "%Y-%m-%d").date() >= today: valid.append(f"{key.strip()}|{expiry.strip()}") except: continue return valid

def get_file_sha(): try: res = requests.get(GITHUB_API_URL, headers=HEADERS) return res.json().get("sha") except: return None

def update_github_key_file(new_lines, sha): try: content = "\n".join(new_lines) encoded = base64.b64encode(content.encode()).decode() payload = { "message": "🔁 Auto-remove expired keys - MAAZ Tool", "content": encoded, "sha": sha } res = requests.put(GITHUB_API_URL, headers=HEADERS, json=payload) if res.status_code == 200: print("✅ Expired keys removed from GitHub.") else: print("⚠️ GitHub update failed:", res.text) except Exception as e: print("❌ Failed to push cleaned keys:", e)

def auto_remove_expired_keys(): key_lines = fetch_key_list() valid_keys = clean_expired_keys(key_lines) if len(valid_keys) < len(key_lines): sha = get_file_sha() if sha: update_github_key_file(valid_keys, sha)

def check_key_approval(local_key, key_list): today = datetime.today().date() for line in key_list: try: key, expiry = line.strip().split("|") if key.strip() == local_key: exp_date = datetime.strptime(expiry.strip(), "%Y-%m-%d").date() return exp_date >= today except: continue return False

def ensure_required_files(): if not os.path.exists(KEY_FILE): print("⚠️ Missing key file, generating...") key = f"MAAZ-{str(int(time.time()))[-4:]}" with open(KEY_FILE, "w") as f: f.write(key) if not os.path.exists(LOG_FILE): with open(LOG_FILE, "w") as f: f.write("") if not os.path.exists(CLONE_SCRIPT): with open(CLONE_SCRIPT, "w") as f: f.write("print('🔁 Placeholder: clone_module.py is missing.')") print("⚠️ Created placeholder for clone_module.py")

def get_ip(): try: return requests.get("https://api.ipify.org").text.strip() except: return "UNKNOWN"

def log_user_data(key): ip = get_ip() now = datetime.now().strftime("%Y-%m-%d %H:%M:%S") log_line = f"{key} | {ip} | {now}\n" with open(LOG_FILE, "a") as f: f.write(log_line)

========== Main Logic ==========

def main(): ensure_required_files() key = open(KEY_FILE).read().strip()

if not key:
    print("❌ License key missing. Please contact admin.")
    return

print("🧹 Cleaning expired license keys from GitHub...")
auto_remove_expired_keys()

print(f"\n🔐 Verifying Your License Key: {key}")
while True:
    approved_keys = fetch_key_list()
    if check_key_approval(key, approved_keys):
        print("✅ Key Approved! Welcome to 💥 MAAZ TOOL 💥")
        log_user_data(key)

        # ✅ Automatically Run Cloning Module
        if os.path.exists(CLONE_SCRIPT):
            print("🚀 Starting Cloning Module...\n")
            subprocess.run(["python", CLONE_SCRIPT])
        else:
            print("❌ clone_module.py not found! Please place it in the same folder.")
        break
    else:
        print("⏳ Waiting for approval... Retrying in 20 seconds.")
        time.sleep(20)

if name == "main": main()

