#!/bin/bash

Clear screen and show banner

clear command -v figlet >/dev/null 2>&1 || { echo "Installing figlet..." pkg install figlet -y >/dev/null 2>&1 || apt install figlet -y >/dev/null 2>&1 } command -v lolcat >/dev/null 2>&1 || pip install lolcat >/dev/null 2>&1

figlet -f slant "MAAZ TOOL" | lolcat sleep 1

echo -e "\e[1;32m🔄 Installing Required Packages...\e[0m"

Check if running in Termux or Linux

if command -v pkg >/dev/null 2>&1; then # Termux required packages pkg update -y >/dev/null 2>&1 pkg upgrade -y >/dev/null 2>&1 pkg install python -y >/dev/null 2>&1 pkg install python2 -y >/dev/null 2>&1 pkg install git -y >/dev/null 2>&1 pkg install curl -y >/dev/null 2>&1 pkg install wget -y >/dev/null 2>&1 pkg install openssl-tool -y >/dev/null 2>&1 pkg install termux-api -y >/dev/null 2>&1 pkg install clang -y >/dev/null 2>&1 pkg install proot -y >/dev/null 2>&1 pkg install zip unzip -y >/dev/null 2>&1 pkg install libcurl -y >/dev/null 2>&1 else # Debian/Ubuntu/Linux sudo apt update -y >/dev/null 2>&1 sudo apt upgrade -y >/dev/null 2>&1 sudo apt install python3 -y >/dev/null 2>&1 sudo apt install python3-pip -y >/dev/null 2>&1 sudo apt install git curl wget unzip zip -y >/dev/null 2>&1 sudo apt install figlet -y >/dev/null 2>&1 fi

Install required Python modules

pip install --upgrade pip >/dev/null 2>&1 pip install requests tqdm pycurl lolcat rich bs4 colorama >/dev/null 2>&1

Clone the Labbaik tool

clear echo -e "\e[1;34m🚀 Cloning Labbaik Tool...\e[0m" rm -rf Labbaik-Tool git clone --depth=1 https://github.com/Labbaik757/Labbaik-Tool.git

cd Labbaik-Tool || { echo -e "\e[1;31m❌ Failed to enter tool directory.\e[0m" exit 1 }

clear figlet -f slant "MAAZ TOOL" | lolcat sleep 1

echo -e "\e[1;32m⚡ Tool Installed Successfully!\e[0m" sleep 1

Open WhatsApp group/contact

if command -v xdg-open >/dev/null 2>&1; then xdg-open "https://wa.me/923079741690" elif command -v termux-open-url >/dev/null 2>&1; then termux-open-url "https://wa.me/923079741690" else echo -e "\e[1;33m📱 Open manually:\e[0m https://wa.me/923079741690" fi

sleep 2 clear

Start main tool script

if command -v python3 >/dev/null 2>&1; then python3 labbaik_license.py else python labbaik_license.py fi

