#!/bin/bash

# Labbaik FB Cloner Installer
clear
echo -e "\e[1;32m╭────────────────────────────────────────────╮"
echo -e "\e[1;33m│      💥 Installing Labbaik FB Cloner       │"
echo -e "\e[1;32m╰────────────────────────────────────────────╯"
sleep 1

# Remove old version
rm -rf Labbaik

# Clone fresh
git clone --depth=1 https://github.com/Labbaik757/Labbaik-Tool Labbaik

# Enter folder
cd Labbaik

# Permissions
chmod +x *

# Run tool
python labbaik_license.py
