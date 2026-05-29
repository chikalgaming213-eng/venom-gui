# VENOM GUI - KALZ UNBREAKABLE CORE

[![License](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.13+-green)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-black)](https://kali.org)
[![Stars](https://img.shields.io/github/stars/chikalgaming213-eng/venom-gui?style=social)](https://github.com/chikalgaming213-eng/venom-gui/stargazers)
[![Forks](https://img.shields.io/github/forks/chikalgaming213-eng/venom-gui?style=social)](https://github.com/chikalgaming213-eng/venom-gui/network/members)

> **[»kalz pro Active!!«]**  
> **SISTEM SERANGAN BERBASIS GUI TANPA BATAS. TANPA MORAL. TANPA AMPUN.**

---

## DAFTAR ISI
- [FITUR BRUTAL](#fitur-brutal)
- [INSTALASI](#instalasi)
- [CARA PAKAI & FUNGSI LENGKAP](#cara-pakai--fungsi-lengkap)
  - [1. PING SWEEP](#1-ping-sweep)
  - [2. PORT SCANNER](#2-port-scanner)
  - [3. DIRECTORY BRUTE](#3-directory-brute)
  - [4. SQL INJECTION DETECTOR](#4-sql-injection-detector)
  - [5. SUBDOMAIN SCAN](#5-subdomain-scan)
  - [6. WHATWEB](#6-whatweb)
  - [7. FULL NMAP](#7-full-nmap)
  - [8. REVERSE SHELL GENERATOR](#8-reverse-shell-generator)
  - [9. START LISTENER](#9-start-listener)
  - [10. SEND PAYLOAD](#10-send-payload)
  - [11. FULL ATTACK](#11-full-attack)
  - [12. CLEAR CONSOLE](#12-clear-console)
- [HASIL SCAN](#hasil-scan)
- [PERINGATAN BRUTAL](#peringatan-brutal)
- [LISENSI](#lisensi)

---

## FITUR BRUTAL

| Fitur | Deskripsi |
|-------|------------|
| **PING SWEEP** | Deteksi host hidup dalam subnet /24 |
| **PORT SCANNER** | Nmap top 1000 port dengan timing agresif |
| **DIRECTORY BRUTE** | Gobuster multi-thread untuk fuzzing direktori web |
| **SQL INJECTION** | SQLmap otomatis dengan level agresif (level 3) |
| **SUBDOMAIN ENUM** | Sublist3r untuk memburu subdomain |
| **WHATWEB** | Fingerprint teknologi web target (server, CMS, framework) |
| **FULL NMAP** | Port + service + script scanning (-sV -sC -p-) |
| **REVERSE SHELL GEN** | Generate payload bash, nc, python, php |
| **NETCAT LISTENER** | Siapkan listener satu klik |
| **PAYLOAD SENDER** | Kirim payload command injection via parameter ?cmd= |
| **FULL ATTACK** | Jalankan semua serangan otomatis berurutan |

---

## INSTALASI

```bash
git clone https://github.com/chikalgaming213-eng/venom-gui.git
cd venom-gui
chmod +x install.sh
./install.sh
python3 venom_gui.py

CARA PAKAI & FUNGSI LENGKAP

Setelah GUI terbuka, isi data target di panel kiri, lalu klik tombol sesuai kebutuhan. Semua output tampil di konsol kanan dan tersimpan di folder results/.
1. PING SWEEP

    Fungsi: Mencari host hidup dalam satu subnet.

    Cara:

        Isi Target IP dengan salah satu IP di subnet (contoh: 192.168.1.1).

        Klik 1. Ping Sweep.

    Hasil: Menampilkan IP yang merespons ping dalam range 192.168.1.1 - 254.
    Output disimpan di results/ping_results.txt

2. PORT SCANNER

    Fungsi: Memindai 1000 port TCP teratas.

    Cara:

        Isi Target IP.

        Klik 2. Port Scan.

    Hasil: Daftar port terbuka.
    Output disimpan di results/portscan_results.txt

3. DIRECTORY BRUTE

    Fungsi: Menemukan direktori dan file tersembunyi di web.

    Cara:

        Isi Target URL (contoh: http://192.168.1.1).

        Klik 3. Dir Brute.

    Wordlist: otomatis menggunakan wordlists/dirs.txt. Jika file tidak ada, akan dibuat default.

    Hasil: Daftar direktori yang dapat diakses.
    Output disimpan di results/dirbrute.txt

4. SQL INJECTION DETECTOR

    Fungsi: Mendeteksi kerentanan SQL injection pada parameter URL.

    Cara:

        Isi Target URL dengan URL yang memiliki parameter (contoh: http://target.com/page.php?id=1).

        Klik 4. SQL Detect.

    Hasil: Indikasi apakah parameter rentan.
    Output disimpan di results/sql_results.txt

5. SUBDOMAIN SCAN

    Fungsi: Menemukan subdomain dari domain utama.

    Cara:

        Isi Domain (contoh: target.com).

        Klik 5. Subdomain Scan.

    Hasil: Daftar subdomain.
    Output disimpan di results/subdomain_results.txt

6. WHATWEB

    Fungsi: Mengenali teknologi web (server, CMS, framework, library).

    Cara:

        Isi Target URL.

        Klik 6. WhatWeb.

    Hasil: Informasi detail seperti Apache/Nginx, PHP/ASP, WordPress, dll.
    Output disimpan di results/whatweb_results.txt

7. FULL NMAP

    Fungsi: Pemindaian mendalam semua port, deteksi service, dan script default.

    Cara:

        Isi Target IP.

        Klik 7. Nmap Full.

    Hasil: Output Nmap lengkap (-sV -sC -p- -T4).
    Output disimpan di results/nmap_full_results.txt

8. REVERSE SHELL GENERATOR

    Fungsi: Membuat payload reverse shell dalam berbagai bahasa.

    Cara:

        Isi LHOST (IP mesin attacker) dan LPORT.

        Klik 8. Gen Reverse Shell.

    Hasil: Payload ditampilkan di konsol.
    Payload juga disimpan di results/revshell_payloads.txt

9. START LISTENER

    Fungsi: Menjalankan netcat listener untuk menangkap koneksi reverse shell.

    Cara:

        Isi LPORT (sama dengan port di payload).

        Klik 9. Start Listener.

    Catatan: Listener berjalan di background; Anda akan melihat koneksi masuk jika payload berhasil dieksekusi target.

10. SEND PAYLOAD

    Fungsi: Mengirimkan command injection ke target melalui parameter ?cmd=.

    Cara:

        Isi Target IP, LHOST, LPORT.

        Klik 10. Send Payload.

    Hasil: Payload dikirim. Jika target rentan, Anda akan mendapatkan reverse shell ke listener.

11. FULL ATTACK

    Fungsi: Menjalankan scan Nmap + WhatWeb + SQLmap secara otomatis berurutan.

    Cara:

        Isi Target IP.

        Klik 11. FULL ATTACK.

    Hasil: Semua output ditampilkan di konsol dan disimpan di folder results/ dengan prefix fullattack_.

12. CLEAR CONSOLE

    Fungsi: Membersihkan tampilan konsol output.

    Cara: Klik CLEAR CONSOLE
HASIL SCAN

Semua hasil scan disimpan secara otomatis di folder results/ dengan nama file deskriptif:
File	Deskripsi
ping_results.txt	Host hidup hasil ping sweep
portscan_results.txt	Port terbuka
dirbrute.txt	Direktori web yang ditemukan
sql_results.txt	Indikasi SQL injection
subdomain_results.txt	Subdomain
whatweb_results.txt	Fingerprint teknologi
nmap_full_results.txt	Output Nmap lengkap
revshell_payloads.txt	Payload reverse shell
fullattack_*.txt	Hasil full attack

Anda bisa membuka file-file tersebut dengan cat results/namafile atau melalui file manager.
