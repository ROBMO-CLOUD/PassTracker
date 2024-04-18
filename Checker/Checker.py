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

def Banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = """
██████╗░░█████╗░██████╗░███╗░░░███╗░█████╗░  ░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██████╗░
██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔══██╗  ██╔══██╗██║░░░░░██╔══██╗██║░░░██║██╔══██╗
██████╔╝██║░░██║██████╦╝██╔████╔██║██║░░██║  ██║░░╚═╝██║░░░░░██║░░██║██║░░░██║██║░░██║
██╔══██╗██║░░██║██╔══██╗██║╚██╔╝██║██║░░██║  ██║░░██╗██║░░░░░██║░░██║██║░░░██║██║░░██║
██║░░██║╚█████╔╝██████╦╝██║░╚═╝░██║╚█████╔╝  ╚█████╔╝███████╗╚█████╔╝╚██████╔╝██████╔╝
╚═╝░░╚═╝░╚════╝░╚═════╝░╚═╝░░░░░╚═╝░╚════╝░  ░╚════╝░╚══════╝░╚════╝░░╚═════╝░╚═════╝░

                        

>> Press Enter                                         

"""

    Anime.Fade(Center.Center(banner), Colors.black_to_red, Colorate.Vertical, interval=0.035, enter=True)

Banner()

def center(text, color):
    terminal_width = shutil.get_terminal_size().columns
    for line in text.split('\n'):
        centered_text = line.center(terminal_width)
        sys.stdout.write(color + centered_text + Fore.RESET + '\n')

def MainBanner():
    os.system('cls' if os.name=='nt' else 'clear')
    banner_text = f"""{Fore.RED}
    
     $$$$$$\  $$\   $$\ $$$$$$$$\  $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$\  
    $$  __$$\ $$ |  $$ |$$  _____|$$  __$$\ $$ | $$  |$$  _____|$$  __$$\ 
    $$ /  \__|$$ |  $$ |$$ |      $$ /  \__|$$ |$$  / $$ |      $$ |  $$ |
    $$ |      $$$$$$$$ |$$$$$\    $$ |      $$$$$  /  $$$$$\    $$$$$$$  |
    $$ |      $$  __$$ |$$  __|   $$ |      $$  $$<   $$  __|   $$  __$$< 
    $$ |  $$\ $$ |  $$ |$$ |      $$ |  $$\ $$ |\$$\  $$ |      $$ |  $$ |
    \$$$$$$  |$$ |  $$ |$$$$$$$$\ \$$$$$$  |$$ | \$$\ $$$$$$$$\ $$ |  $$ |
     \______/ \__|  \__|\________| \______/ \__|  \__|\________|\__|  \__|
                                                                      
                                                               
    """

    os.system('cls' if os.name=='nt' else 'clear')
    center(banner_text, Fore.RED)

MainBanner()

Options = (Fore.GREEN+"""

                                                Please Select Your Option:



                                                [1] TLauncher (Gaming).

                                                [2] TunnelBear (VPN).

                                                [3] Virustotal (SCANNER).

                                                [4] Netflix.

                                                [5] Steam (Gaming).

                                                [6] MAX.

""")

print(Options)

def create_folders():
    os.system('cls' if os.name == 'nt' else 'clear')
    username = getpass.getuser()
    
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    
    parent_folder_name = "𝐏𝐚𝐬𝐬𝐓𝐫𝐚𝐜𝐤𝐞𝐫 ™"
    sub_folder_name = "𝐂𝐡𝐞𝐜𝐤𝐞𝐫"
    
    parent_folder_path = os.path.join(desktop_path, parent_folder_name)
    
    sub_folder_path = os.path.join(parent_folder_path, sub_folder_name)
    
    if not os.path.exists(parent_folder_path):
        try:
            os.makedirs(parent_folder_path)
            Write.Print(f"\n\n     The folder has been created on {username}'s desktop.", Colors.blue)
        except Exception as e:
            Write.Print(f"\n\n     Error creating the folder: {e}", Colors.blue)

    else:
        Write.Print(f"\n\n     The folder already exists on {username}'s desktop.", Colors.blue)
    
    if not os.path.exists(sub_folder_path):
        os.makedirs(sub_folder_path)
    else:
        pass
    return sub_folder_path

def download(url, folder_path, file_name):
    file_path = os.path.join(folder_path, file_name)

    try:
        urllib.request.urlretrieve(url, file_path)
        Write.Print("\n\n     File downloaded successfully.", Colors.blue)

    except Exception as e:
        Write.Print(f"\n\n      Error downloading the file: {e}", Colors.blue)

def VirusTotal():
    folder_path = create_folders()

    url = "https://raw.githubusercontent.com/ROBMO-CLOUD/TXT-TOOLS/main/URL's%20Tools/VirusTotal.py"
    file_name = "VirusTotal.py"

    download(url, folder_path, file_name)

    try:
        if os.name == 'nt':
            os.system(f'python "{os.path.join(folder_path, file_name)}"')
        else:
            os.system(f'python3 "{os.path.join(folder_path, file_name)}"')
    except Exception as e:
        Write.Print(f"\n\n      Error executing the script: {e}", Colors.blue)

    
def TunnelBear():
    folder_path = create_folders()

    url = "https://raw.githubusercontent.com/ROBMO-CLOUD/TXT-TOOLS/main/URL's%20Tools/TunnelBear.py"
    file_name = "Virustotal.py"

    download(url, folder_path, file_name)

    try:
        if os.name == 'nt':
            os.system(f'python "{os.path.join(folder_path, file_name)}"')
        else:
            os.system(f'python3 "{os.path.join(folder_path, file_name)}"')
    except Exception as e:
        Write.Print(f"\n\n      Error executing the script: {e}", Colors.blue)

def Netflix():
    Netflix()

def Steam():
    Steam()

def Max():        
    Max()

def USERCHOICE():
    User_Option = input(Fore.WHITE+"                                                >>  ")
    if User_Option == "1":
        os.system('python TLauncher.py')
    if User_Option == "2":
        TunnelBear()
    if User_Option=="3":
        VirusTotal()
    if User_Option=="4":
        os.system('python Netflix.py')
    if User_Option=="5":
        os.system('python Steam.py')
    if User_Option=="6":
        os.system('python MAX.py')


USERCHOICE()
