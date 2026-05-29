#!/bin/bash

echo "[*] installing dependencies for VENOM GUI + SEEKER..."
sudo apt update

# Core tools untuk VENOM GUI
sudo apt install -y python3 python3-tk nmap sqlmap gobuster sublist3r whatweb hydra netcat-traditional curl tor

# Python packages via apt
sudo apt install -y python3-requests python3-pil

# Untuk Seeker (GPS tracker)
echo "[*] installing Seeker dependencies..."
sudo apt install -y php-cli git
pip3 install requests packaging psutil --break-system-packages

# Clone Seeker repository (jika belum ada)
if [ -d "seeker" ]; then
    echo "[!] Seeker folder already exists, updating..."
    cd seeker && git pull && cd ..
else
    git clone https://github.com/thewhiteh4t/seeker.git
fi

if [ -d "seeker" ]; then
    echo "[+] Seeker cloned successfully."
    chmod +x seeker/seeker.py seeker/install.sh
    # Jalankan installer seeker (opsional, aman)
    cd seeker && ./install.sh && cd ..
else
    echo "[-] Failed to clone Seeker. Install manually later."
fi

# Buat folder wordlists dan results
mkdir -p wordlists results
chmod +x *.py 2>/dev/null

echo "[+] ALL DEPENDENCIES INSTALLED."
echo "[*] Run: python3 venom_gui.py"
echo "[*] Seeker available in 'seeker' folder and integrated in GUI."
