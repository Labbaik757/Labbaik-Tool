#!/data/data/com.termux/files/usr/bin/bash

clear echo -e "\e[92m" echo "🚀 Cloning MAAZ Tool from GitHub..." sleep 1

Clone or update the tool

if [ -d "Labbaik-Tool" ]; then echo "🔁 Updating existing folder..." cd Labbaik-Tool && git pull else git clone https://github.com/Labbaik757/Labbaik-Tool.git || { echo -e "\n❌ Failed to clone. Attempting to create folder manually..." mkdir Labbaik-Tool && cd Labbaik-Tool || { echo "❌ Could not create or enter fallback folder. Exiting."; exit 1; } } cd Labbaik-Tool fi

Ensure required files exist

echo -e "\n🛠 Checking essential files..." REQUIRED_FILES=("labbaik_license.py" "clone_module.py" ".maaz_key.txt" "maaz_logs.txt")

for FILE in "${REQUIRED_FILES[@]}"; do if [ ! -f "$FILE" ]; then echo "⚠️ Missing file: $FILE — creating placeholder." case $FILE in "labbaik_license.py") echo -e "print('🔒 Placeholder: License script missing.')" > "$FILE" ;; "clone_module.py") echo -e "print('🔁 Placeholder: Cloning module missing.')" > "$FILE" ;; ".maaz_key.txt") echo "MAAZ-$(shuf -i 100-999 -n 1)" > "$FILE" ;; "maaz_logs.txt") echo "" > "$FILE" ;; esac fi sleep 0.3 done

Auto fix Python if missing

if ! command -v python &>/dev/null; then echo "⚙️ Python not found. Installing Python..." pkg install python -y fi

Auto fix pip if missing

if ! command -v pip &>/dev/null; then echo "⚙️ Pip not found. Installing pip..." pkg install python-pip -y fi

Install required modules

echo -e "\n📦 Installing Python modules (requests, rich)...\n" pip install requests rich --quiet || { echo "❌ Failed to install modules. Trying pip fix..." python -m ensurepip --default-pip pip install requests rich --quiet }

Optional: WhatsApp redirect

echo -e "\n🔗 Redirecting to WhatsApp Group (Press Ctrl+C to skip)..." sleep 2 xdg-open "https://chat.whatsapp.com/CFGuz089SUe5npFZDS8iTh" || echo "(WhatsApp skipped)"

Run the license system script

echo -e "\n✅ Starting MAAZ Tool...\n" python labbaik_license.py || { echo "❌ Error running labbaik_license.py. Attempting auto-fix..." chmod +x labbaik_license.py python labbaik_license.py }

