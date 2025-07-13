#!/data/data/com.termux/files/usr/bin/bash

clear
echo -e "\e[92m"
echo "🚀 Cloning Labbaik Tool from GitHub..."
sleep 1

# Clone only if not already cloned
if [ ! -d "Labbaik-Tool" ]; then
    git clone https://github.com/Labbaik757/Labbaik-Tool.git
fi

# Enter the folder (Only once)
cd Labbaik-Tool || { echo -e "\n❌ Folder not found! Installation failed."; exit 1; }

echo -e "\n📦 Installing required modules...\n"
pkg install python -y
pip install requests rich

echo -e "\n🔗 Redirecting to WhatsApp Group (Press Ctrl+C to skip)..."
xdg-open "https://wa.me/923000000000"
sleep 3

# Final Run
echo -e "\n✅ Starting Labbaik Tool...\n"
python maaz_license.py
