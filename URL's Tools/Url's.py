try:
    import os, subprocess, re, time, sys, shutil, requests, ctypes, concurrent.futures, signal, urllib.request, getpass
    from colorama import *
    from tkinter import filedialog, Tk
    from datetime import datetime
    from pystyle import *
    from pathlib import Path
    init()

except:
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("pip install pystyle")

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


Options = (Fore.BLUE+"""

                                                Please Select Your Option:


                                                [1] Remove Duplicates.

                                                [2] Remove UNKNOWN.

                                                [3] Search URL's

                                                [4] URL's to Combo

""")

print(Options)


def create_folders():
    os.system('cls' if os.name == 'nt' else 'clear')
    username = getpass.getuser()
    
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    
    parent_folder_name = "𝐏𝐚𝐬𝐬𝐓𝐫𝐚𝐜𝐤𝐞𝐫 ™"
    sub_folder_name = "𝐔𝐑𝐋❜𝐬 𝐓𝐨𝐨𝐥𝐬"
    
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
        Write.Print(f"\n\n     Error downloading the file: {e}", Colors.blue)

def Duplicates():
    folder = create_folders()
    url = "https://raw.githubusercontent.com/ROBMO-CLOUD/PassTracker/main/URL's%20Tools/Duplicates.py"
    file_name = "Duplicates.py"

    download(url, folder, file_name)

    try:
        if os.name == 'nt':
            os.system(f'python "{os.path.join(folder, file_name)}"')
        else:
            os.system(f'python3 "{os.path.join(folder, file_name)}"')
    except Exception as e:
        Write.Print(f"\n\n     Error executing the script: {e}", Colors.blue_to_cyan)

def Unknown():
    folder = create_folders()
    url = "https://raw.githubusercontent.com/ROBMO-CLOUD/PassTracker/main/URL's%20Tools/Unknowns.py"
    file_name = "Unknowns.py"

    download(url, folder, file_name)

    try:
        if os.name == 'nt':
            os.system(f'python "{os.path.join(folder, file_name)}"')
        else:
            os.system(f'python3 "{os.path.join(folder, file_name)}"')
    except Exception as e:
        Write.Print(f"\n\n     Error executing the script: {e}", Colors.blue_to_cyan)

def Search():
    folder = create_folders()
    url = "https://raw.githubusercontent.com/ROBMO-CLOUD/PassTracker/main/URL's%20Tools/Search.py"
    file_name = "Search.py"

    download(url, folder, file_name)

    try:
        if os.name == 'nt':
            os.system(f'python "{os.path.join(folder, file_name)}"')
        else:
            os.system(f'python3 "{os.path.join(folder, file_name)}"')
    except Exception as e:
        Write.Print(f"\n\n     Error executing the script: {e}", Colors.blue_to_cyan)

def Combo():
    folder = create_folders()
    url = "https://raw.githubusercontent.com/ROBMO-CLOUD/PassTracker/main/URL's%20Tools/Combos.py"
    file_name = "Combos.py"

    download(url, folder, file_name)

    try:
        if os.name == 'nt':
            os.system(f'python "{os.path.join(folder, file_name)}"')
        else:
            os.system(f'python3 "{os.path.join(folder, file_name)}"')
    except Exception as e:
        Write.Print(f"\n\n     Error executing the script: {e}", Colors.blue_to_cyan)
    
def USERCHOICE():
    User_Option = input(Fore.WHITE+"                                                >>   ")
    
    if User_Option == "1":
        os.system('cls' if os.name=='nt' else 'clear')
        Duplicates()

    elif User_Option == "2":
        os.system('cls' if os.name=='nt' else 'clear')
        Unknown() 

    elif User_Option == "3":
        os.system('cls' if os.name=='nt' else 'clear')
        Search()

    elif User_Option == "4":
        os.system('cls' if os.name=='nt' else 'clear')
        Combo()

USERCHOICE()
