#!/bin/bash

clear figlet -f slant "LABBAIK" | lolcat sleep 1 echo -e "\e[1;32m🔄 Installing Required Packages...\e[0m" pkg update -y &> /dev/null pkg install python -y &> /dev/null pkg install git -y &> /dev/null pip install requests tqdm pycurl lolcat rich &> /dev/null

clear echo -e "\e[1;34m🚀 Cloning Labbaik Tool...\e[0m" rm -rf Labbaik-Tool

git clone --depth=1 https://github.com/Labbaik757/Labbaik-Tool.git cd Labbaik-Tool

clear figlet "Maaz Tool" | lolcat sleep 1 echo -e "\e[1;32m⚡ Tool Installed Successfully!\e[0m" sleep 1 xdg-open "https://wa.me/923079741690" sleep 2

clear python labbaik_license.py

