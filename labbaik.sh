#!/data/data/com.termux/files/usr/bin/bash

clear
echo -e "\e[92m"
echo "🚀 Installing Labbaik Tool with Auto-Fix Mode...\n"
sleep 1

# Fix DNS/GitHub Internet Access Issue
echo "🔧 Checking internet..."
ping -c 1 google.com > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "⚠️ DNS error detected. Fixing..."
    echo "nameserver 8.8.8.8" > $PREFIX/etc/resolv.conf
    sleep 1
fi

# Delete old corrupted folder if exists
if [ -d "Labbaik" ]; then
    echo "🧹 Removing old Labbaik folder..."
    rm -rf Labbaik
fi

# Clone fresh
echo "📥 Cloning latest tool from GitHub..."
git clone https://github.com/Labbaik757/Labbaik-Tool.git Labbaik || {
    echo "❌ GitHub clone failed. Check internet."
    exit 1
}

# Move inside tool folder
cd Labbaik || {
    echo "❌ Folder not found. Exiting."
    exit 1
}

# Check & create missing main Python file
if [ ! -f labbaik_license.py ]; then
    echo "⚠️ Missing labbaik_license.py — creating dummy file..."
    cat > labbaik_license.py <<EOF
print("🔧 Auto-created file: labbaik_license.py — Please replace with real code.")
EOF
    sleep 1
fi

# Install Python if missing
command -v python >/dev/null 2>&1 || pkg install python -y

# Retry pip module installation
pip install requests rich || {
    echo "⚠️ Retrying pip install..."
    pip install requests rich --break-system-packages || {
        echo "❌ Module install failed."
        exit 1
    }
}

# WhatsApp redirect
echo -e "\n🔗 Redirecting to WhatsApp Group (Press Ctrl+C to skip)..."
xdg-open "https://wa.me/923000000000"
sleep 2

# Run main script
echo -e "\n✅ Starting Labbaik Tool...\n"
python labbaik_license.py
