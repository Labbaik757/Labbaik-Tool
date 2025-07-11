#!/bin/bash

# 💠 Labbaik Facebook Cloner Tool Auto Installer
# 👑 Developer: Mohammad Maaz

echo "🔁 Downloading Labbaik Tool..."
rm -rf Labbaik

git clone --depth=1 https://github.com/Labbaik757/Labbaik-Tool Labbaik
cd Labbaik

echo "📦 Installing required Python libraries..."
pip install requests > /dev/null 2>&1

echo "🚀 Starting License System..."
python labbaik_license.py
