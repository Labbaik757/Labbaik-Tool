#!/data/data/com.termux/files/usr/bin/bash

clear

Banner

echo -e "\e[96m" echo "███████╗ █████╗ ███████╗███████╗" echo "██╔════╝██╔══██╗╚══███╔╝██╔════╝" echo "█████╗  ███████║  ███╔╝ █████╗  " echo "██╔══╝  ██╔══██║ ███╔╝  ██╔══╝  " echo "██║     ██║  ██║███████╗███████╗" echo "╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝" echo "     🔰 MAAZ TOOL 🔰" echo -e "\e[0m" sleep 1

Clone or update the tool

echo -e "\n🚀 Checking for Labbaik-Tool folder..." if [ -d "Labbaik-Tool" ]; then echo "🔁 Updating existing folder..." cd Labbaik-Tool && git pull else echo "📥 Cloning Labbaik-Tool from GitHub..." git clone https://github.com/Labbaik757/Labbaik-Tool.git || { echo -e "\n❌ Git clone failed. Creating folder manually..." mkdir Labbaik-Tool && cd Labbaik-Tool || { echo "❌ Could not enter fallback folder. Exiting."; exit 1; } } cd Labbaik-Tool fi

Ensure required files exist

echo -e "\n🛠 Checking required files..." REQUIRED_FILES=("labbaik_license.py" "clone_module.py" ".maaz_key.txt" "maaz_logs.txt")

for FILE in "${REQUIRED_FILES[@]}"; do if [ ! -f "$FILE" ]; then echo "⚠️ File missing: $FILE — auto-creating." case $FILE in "labbaik_license.py") echo -e "print('🔒 Placeholder: license script missing.')" > "$FILE" ;; "clone_module.py") echo -e "print('🔁 Placeholder: clone module missing.')" > "$FILE" ;; ".maaz_key.txt") echo "MAAZ-$(shuf -i 100-999 -n 1)" > "$FILE" ;; "maaz_logs.txt") echo "" > "$FILE" ;; esac fi sleep 0.2 done

Install Python & pip if missing

echo -e "\n📦 Ensuring Python is installed..." if ! command -v python &>/dev/null; then pkg install python -y fi

if ! command -v pip &>/dev/null; then pkg install python-pip -y fi

Install Python modules

echo -e "\n📦 Installing Python modules: requests, rich..." pip install requests rich --quiet || { echo "⚠️ Pip issue detected. Trying fix..." python -m ensurepip --default-pip pip install requests rich --quiet }

Optional: WhatsApp redirect

echo -e "\n🔗 Redirecting to WhatsApp Group (Ctrl+C to skip)..." sleep 2 xdg-open "https://chat.whatsapp.com/CFGuz089SUe5npFZDS8iTh" || echo "(Skip or link blocked)"

Run license system

echo -e "\n✅ Launching MAAZ Tool...\n" python labbaik_license.py || { echo "❌ Error in license script. Applying fix..." chmod +x labbaik_license.py python labbaik_license.py }

