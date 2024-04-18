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

██████╗░██╗░░░██╗██████╗░██╗░░░░░██╗░█████╗░░█████╗░████████╗███████╗░██████╗
██╔══██╗██║░░░██║██╔══██╗██║░░░░░██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔════╝
██║░░██║██║░░░██║██████╔╝██║░░░░░██║██║░░╚═╝███████║░░░██║░░░█████╗░░╚█████╗░
██║░░██║██║░░░██║██╔═══╝░██║░░░░░██║██║░░██╗██╔══██║░░░██║░░░██╔══╝░░░╚═══██╗
██████╔╝╚██████╔╝██║░░░░░███████╗██║╚█████╔╝██║░░██║░░░██║░░░███████╗██████╔╝
╚═════╝░░╚═════╝░╚═╝░░░░░╚══════╝╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░
          
                               
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

def Duplicates(file_path):

    os.system('cls' if os.name == 'nt' else 'clear')

    output_folder = passtracker / "𝐔𝐑𝐋❜𝐬 𝐓𝐨𝐨𝐥𝐬"
    output_folder.mkdir(parents=True, exist_ok=True)  

    output_file = output_folder / f"ROBMOCLOUD[NODUPLICATES]-{datetime.now().strftime('[%H][%M][%S]')}.txt"

    unique_lines = set()

    with open(file_path, 'r', encoding='latin') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip().startswith(("http", "https", "android")):
                if not any(line.startswith(ignore_line) for ignore_line in ignore):
                    unique_lines.add(line.strip())

    with open(output_file, 'w', encoding='latin') as file:  
        for line in unique_lines:
            file.write(line + '\n')

    total_lines = len(lines)
    removed_duplicates = total_lines - len(unique_lines)
    remaining_lines = len(unique_lines)

    Banner()
    Write.Print(f"\n\n     [•]  Total lines: {total_lines}", Colors.blue_to_white)
    Write.Print(f"\n\n     [•]  Removed duplicates: {removed_duplicates}", Colors.blue_to_white)
    Write.Print(f"\n\n     [•]  Remaining lines: {remaining_lines}", Colors.blue_to_white)
    Write.Print("\n\n     [•]  Duplicates have been removed. \n\n     [•]  Check the folder.", Colors.blue_to_white)
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')

file_path = select_file()
Duplicates(file_path)

time.sleep(5000)
