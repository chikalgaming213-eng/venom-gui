#!/bin/bash
echo "[*] installing dependencies..."
sudo apt update
sudo apt install -y python3 python3-tk nmap sqlmap gobuster sublist3r whatweb hydra netcat-traditional curl tor
sudo apt install -y python3-requests python3-pil
mkdir -p wordlists results
chmod +x *.py 2>/dev/null
echo "[+] done. run: python3 venom_gui.py"
