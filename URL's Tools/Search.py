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



░██████╗███████╗░█████╗░██████╗░░█████╗░██╗░░██╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║
╚█████╗░█████╗░░███████║██████╔╝██║░░╚═╝███████║
░╚═══██╗██╔══╝░░██╔══██║██╔══██╗██║░░██╗██╔══██║
██████╔╝███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║
╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

██╗░░░██╗██████╗░██╗░░░░░
██║░░░██║██╔══██╗██║░░░░░
██║░░░██║██████╔╝██║░░░░░
██║░░░██║██╔══██╗██║░░░░░
╚██████╔╝██║░░██║███████╗
░╚═════╝░╚═╝░░╚═╝╚══════╝


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
        Banner()
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
    
def Search():
    Banner()
    Write.Print("\n\n     Write the URL of the platform you want to search", Colors.red_to_yellow)
    Write.Print("\n\n     For example:", Colors.red_to_yellow)
    Write.Print("\n\n     ▪ https://www.paypal.com/", Colors.red_to_yellow)
    Write.Print("\n\n     ▪ Or: www.paypal.com/", Colors.red_to_yellow)


    search_term = input("\n\n     >> ")
    
    url_regex = re.compile(
        r'^(?:http|ftp)s?://'  
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  
        r'localhost|'  
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  
        r'(?::\d+)?'  
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if not re.match(url_regex, search_term):
        os.system('cls' if os.name=='nt' else 'clear')
        Banner()
        Write.Print("\n\n     [!]  Only URLs are allowed. Please enter a valid URL.", Colors.red_to_yellow)
        time.sleep(2)
        search_term = input("\n\n     >> ")

    file_path = select_file()  
    file_name = os.path.basename(file_path)
    
    os.system('cls' if os.name=='nt' else 'clear')
    Banner()
    os.system('cls' if os.name == 'nt' else 'clear')
    Write.Print("\n\n     Updating...", Colors.red_to_yellow)
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

    Banner()
    Write.Print(f"\n\n     Searching for '{search_term}'...", Colors.red_to_yellow)
    os.system('cls' if os.name == 'nt' else 'clear')

    search_results = []

    output_folder = passtracker / "𝐔𝐑𝐋❜𝐬 𝐓𝐨𝐨𝐥𝐬"
    output_folder.mkdir(parents=True, exist_ok=True)  

    output_file = output_folder / f"ROBMOCLOUD[SEARCH]-{datetime.now().strftime('[%H%M%S]')}.txt"

    with open(file_path, 'r', encoding='latin') as file:
        for line in file:
            if line.strip().startswith(("http", "https", "android")):
                if search_term.lower() in line.lower():
                    search_results.append(line.strip())
    
    if search_results:
        with open(output_file, 'w', encoding='latin') as output_file:
            for result in search_results:
                output_file.write(result + '\n')

        os.system('cls' if os.name=='nt' else 'clear')
        Banner()
        Write.Print(f"\n\n     ▪   Process completed successfully...", Colors.red_to_yellow)
        Write.Print(f"\n\n     ▪   Total lines found: {len(search_results)}", Colors.red_to_yellow)        
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        os.system('cls' if os.name=='nt' else 'clear')
        Banner()
        Write.Print(f"\n\n     [!]  No results found for '{search_term}'.", Colors.red_to_yellow)
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')

    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')

Search()
