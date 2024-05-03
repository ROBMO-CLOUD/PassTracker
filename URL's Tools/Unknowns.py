import os
import subprocess
import re
import time
import sys
import shutil
import requests
import ctypes
import getpass
import concurrent.futures
import signal
from colorama import *
from tkinter import filedialog, Tk
from datetime import datetime
from pystyle import *
from pathlib import Path
import urllib.request

init()
os.system("cls")

user = os.getlogin()

passtracker = Path(f'C:/Users/{user}/Desktop/𝐏𝐚𝐬𝐬𝐓𝐫𝐚𝐜𝐤𝐞𝐫 ™')

if not passtracker.exists():
    passtracker.mkdir()

ignore = (
    "██████╗░░█████╗░██████╗░███╗░░░███╗░█████╗░",
    "██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔══██╗",
    "██████╔╝██║░░██║██████╦╝██╔████╔██║██║░░██║",
    "██╔══██╗██║░░██║██╔══██╗██║╚██╔╝██║██║░░██║",
    "██║░░██║╚█████╔╝██████╦╝██║░╚═╝░██║╚█████╔╝",
    "╚═╝░░╚═╝░╚════╝░╚═════╝░╚═╝░░░░░╚═╝░╚════╝░"
)

os.system("title URL's Tools" if os.name=='nt' else None)

os.system('cls' if os.name=='nt' else 'clear')

def center(text, color):
    terminal_width = shutil.get_terminal_size().columns
    for line in text.split('\n'):
        centered_text = line.center(terminal_width)
        sys.stdout.write(color + centered_text + Fore.RESET + '\n')

def Banner():
    os.system('cls' if os.name=='nt' else 'clear')
    banner_text = f"""{Fore.RED}



██████╗░███████╗███╗░░░███╗░█████╗░██╗░░░██╗███████╗
██╔══██╗██╔════╝████╗░████║██╔══██╗██║░░░██║██╔════╝
██████╔╝█████╗░░██╔████╔██║██║░░██║╚██╗░██╔╝█████╗░░
██╔══██╗██╔══╝░░██║╚██╔╝██║██║░░██║░╚████╔╝░██╔══╝░░
██║░░██║███████╗██║░╚═╝░██║╚█████╔╝░░╚██╔╝░░███████╗
╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝

██╗░░░██╗███╗░░██╗██╗░░██╗███╗░░██╗░█████╗░░██╗░░░░░░░██╗░██████╗
██║░░░██║████╗░██║██║░██╔╝████╗░██║██╔══██╗░██║░░██╗░░██║██╔════╝
██║░░░██║██╔██╗██║█████═╝░██╔██╗██║██║░░██║░╚██╗████╗██╔╝╚█████╗░
██║░░░██║██║╚████║██╔═██╗░██║╚████║██║░░██║░░████╔═████║░░╚═══██╗
╚██████╔╝██║░╚███║██║░╚██╗██║░╚███║╚█████╔╝░░╚██╔╝░╚██╔╝░██████╔╝
░╚═════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═════╝░ 


    """

    os.system('cls' if os.name=='nt' else 'clear')
    center(banner_text, Fore.RED)

Banner()

def select_file():
    root = Tk()
    root.withdraw()  

    file_path = filedialog.askopenfilename(title="Select Combo File", filetypes=[("Text Files", "*.txt")])
    if not file_path:
        os.system('cls' if os.name=='nt' else 'clear')
        Write.Print("\n\n     [•]  Selected File: FALSE", Colors.red)
        time.sleep(2)
        os.system('cls' if os.name=='nt' else 'clear')
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

def Unknowns(file_path):

    os.system('cls' if os.name == 'nt' else 'clear')

    output_folder = passtracker / "𝐔𝐑𝐋❜𝐬 𝐓𝐨𝐨𝐥𝐬"
    output_folder.mkdir(parents=True, exist_ok=True)  

    output_file = output_folder / f"ROBMOCLOUD[NOUNKNOWNS]-{datetime.now().strftime('[%H%M%S]')}.txt"

    lines_to_keep = []

    with open(file_path, 'r', encoding='latin') as file:
        for line in file:
            if re.match(r'^(https?://|android://)', line.strip()) and 'UNKNOWN' not in line.upper():
                lines_to_keep.append(line.strip())

    if not lines_to_keep:
        Write.Print("\n\n     [!]  No lines found that meet the filtering criteria.", Colors.red_to_green)
        time.sleep(3)
        return

    with open(output_file, 'w', encoding='latin') as file:
        for line in lines_to_keep:
            file.write(line + '\n')

    total_lines = sum(1 for _ in open(file_path, 'r', encoding='latin-1'))
    removed_lines = total_lines - len(lines_to_keep)

    Banner()
    Write.Print(f"\n\n     [•]  Total lines: {total_lines}", Colors.red_to_green)
    Write.Print(f"\n\n     [•]  Removed lines: {removed_lines}", Colors.red_to_green)
    Write.Print(f"\n\n     [•]  Remaining lines: {len(lines_to_keep)}", Colors.red_to_green)
    Write.Print("\n\n     [•]  Lines containing 'Unknown' have been removed.\n\n     [•]  Check the folder.", Colors.red_to_green)
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')        
    time.sleep(5)

file_path = select_file()
Unknowns(file_path)