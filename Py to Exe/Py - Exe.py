from pystyle import *
import os
import subprocess
from colorama import *
import time
import sys
from tkinter import filedialog, Tk
import requests
import ctypes
import shutil
import tk
import tkinter

os.system('cls' if os.name == 'nt' else 'clear')



def center(text, color):
    terminal_width = shutil.get_terminal_size().columns
    for line in text.split('\n'):
        centered_text = line.center(terminal_width)
        sys.stdout.write(color + centered_text + Fore.RESET + '\n')

def MainBanner():
    os.system('cls' if os.name=='nt' else 'clear')
    banner_text = f"""{Fore.RED}



██████╗░░█████╗░██████╗░███╗░░░███╗░█████╗░     ░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██████╗░
██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔══██╗     ██╔══██╗██║░░░░░██╔══██╗██║░░░██║██╔══██╗
██████╔╝██║░░██║██████╦╝██╔████╔██║██║░░██║     ██║░░╚═╝██║░░░░░██║░░██║██║░░░██║██║░░██║
██╔══██╗██║░░██║██╔══██╗██║╚██╔╝██║██║░░██║     ██║░░██╗██║░░░░░██║░░██║██║░░░██║██║░░██║
██║░░██║╚█████╔╝██████╦╝██║░╚═╝░██║╚█████╔╝     ╚█████╔╝███████╗╚█████╔╝╚██████╔╝██████╔╝
╚═╝░░╚═╝░╚════╝░╚═════╝░╚═╝░░░░░╚═╝░╚════╝░     ░╚════╝░╚══════╝░╚════╝░░╚═════╝░╚═════╝░


"""

    os.system('cls' if os.name=='nt' else 'clear')
    center(banner_text, Fore.RED)

MainBanner()

def download_icon(icon_url, save_path):
    try:
        response = requests.get(icon_url, stream=True)
        response.raise_for_status()
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        return save_path
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the icon: {e}")
        return None
    
while True:
    Write.Print("\nWhich option do you want to choose: ", Colors.light_blue)
    Write.Print("\n", Colors.light_blue)
    Write.Print("\n1. Build Exe", Colors.light_blue)
    Write.Print("\n2. Close", Colors.light_blue)
    Write.Print("\n", Colors.light_blue)
    Write.Print("\nMake your selection: ", Colors.light_blue, end="")
    choice = input()

    if choice == "1":
        os.system("cls || clear")

        def select_python_file():
            root = tk.Tk()
            root.withdraw()  
            file_py = filedialog.askopenfilename(title="Select the .py file", filetypes=(("Python Files", "*.py"), ("All files", "*.*")))
            return file_py
        
        def convert(file_py, icon_url):
            if not file_py:
                Write.Print("No file selected.", Colors.light_red)
                return
            
            if not os.path.exists(file_py):
                Write.Print(f"The file {file_py} does not exist.", Colors.light_red)
                return
            
            icon_path = "icon.ico"

            if not os.path.exists(icon_path):
                Write.Print("\n\nDownloading the icon...\n\n", Colors.light_blue)
            
                if download_icon(icon_url, icon_path):
                    Write.Print("\n\nIcon downloaded successfully.\n\n", Colors.light_blue)
                else:
                    Write.Print("Error downloading the icon. Default icon will be used.", Colors.light_red)

            command = f'pyinstaller --onefile --icon "{icon_path}" "{file_py}"'
            print(f"Executing: {command}\n\n", Colors.light_blue)
    
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            
            for line in iter(process.stdout.readline, b''):
                try:
                    decoded_line = line.decode('unicode_escape').strip()
                    print(f"{decoded_line}", Colors.light_blue)
                except UnicodeDecodeError:
                    pass

        icon_url = "https://raw.githubusercontent.com/ROBMO-CLOUD/PassTracker/main/Img/Logo.ico"

        MainBanner()

        file_py = "Tools.py"

        if os.path.exists(file_py):
            response = input("\n\nDo you want to convert the Tools.py file to Tools.exe? (Yes/No): ").strip().lower()

            if response == "yes":
                Write.Print(f"\nAutomatically selecting the file {file_py}...\n\n", Colors.light_blue)
                convert(file_py, icon_url)
                os.system("cls || clear")

            elif response == "no":
                Write.Print("\n\nConversion will not be performed.\n\n", Colors.light_red)
            else:
                Write.Print("\n\nUnrecognized response. Conversion will not be performed.\n\n", Colors.light_red)
        else:
            Write.Print(f"\n\nThe file {file_py} does not exist.\n\n", Colors.light_red)  
            time.sleep(5)   
            os.system("cls || clear")


    elif choice == "2":
        Write.Print("\n\nExiting the program...\n\n", Colors.light_red)
        time.sleep(2)
        sys.exit()
        break  
    else:
        Write.Print("\n\nYou have entered an invalid option. Please try again.\n\n", Colors.purple)
