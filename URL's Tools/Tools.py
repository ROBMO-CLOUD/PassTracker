try:
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

os.system("title URL's Tools - ROBMO CLOUD" if os.name=='nt' else None)

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


def Duplicates():
    os.system('cls' if os.name=='nt' else 'clear')

    banner = f"""{Fore.RED}


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

    def center(text, color):
        terminal_width = shutil.get_terminal_size().columns
        for line in text.split('\n'):
            centered_text = line.center(terminal_width)
            sys.stdout.write(color + centered_text + Fore.RESET + '\n')
    
    os.system('cls' if os.name=='nt' else 'clear')
    center(banner, Fore.RED) 

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
            os.system('cls' if os.name=='nt' else 'clear')
            center(banner, Fore.RED) 
            Write.Print("\n\n     [•]  Selected File: TRUE", Colors.light_blue)
            time.sleep(2)
            Write.Print(f"\n\n     [•]  File Name: {file_name}", Colors.light_blue)
            time.sleep(2)
            Write.Print(f"\n\n     [•]  Total Lines: {total_lines}", Colors.light_blue)
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            return file_path
    
    def dup(file_path):
        os.system('cls' if os.name == 'nt' else 'clear')

        output_folder = passtracker / "𝐑𝐞𝐬𝐮𝐥𝐭"
        output_folder.mkdir(parents=True, exist_ok=True)  

        unique_lines = set()

        with open(file_path, 'r', encoding='latin') as file:
            lines = file.readlines()
            for line in lines:
                if line.strip().startswith(("http", "https", "android")):
                    if not any(line.startswith(ignore_line) for ignore_line in ignore):
                        unique_lines.add(line.strip())

        total_lines = len(lines)
        removed_duplicates = total_lines - len(unique_lines)
        remaining_lines = len(unique_lines)

        output_file = output_folder / f"ROBMOCLOUD[NODUPLICATES]-[{remaining_lines}].txt"

        with open(output_file, 'w', encoding='latin') as file:  
            for line in unique_lines:
                file.write(line + '\n')

        center(banner, Fore.RED) 
        Write.Print(f"\n\n     [•]  Total lines: {total_lines}", Colors.light_blue)
        Write.Print(f"\n\n     [•]  Removed duplicates: {removed_duplicates}", Colors.light_blue)
        Write.Print(f"\n\n     [•]  Remaining lines: {remaining_lines}", Colors.light_blue)
        Write.Print("\n\n     [•]  Duplicates have been removed. \n\n     [•]  Check the folder.", Colors.light_blue)
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')

    file_path = select_file()
    dup(file_path)
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
    MainBanner();print(Options);USERCHOICE()

def Unknown():
    os.system('cls' if os.name == 'nt' else 'clear')        

    banner = f"""{Fore.RED}



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

    def center(text, color):
        terminal_width = shutil.get_terminal_size().columns
        for line in text.split('\n'):
            centered_text = line.center(terminal_width)
            sys.stdout.write(color + centered_text + Fore.RESET + '\n')
    os.system('cls' if os.name=='nt' else 'clear')
    center(banner, Fore.RED) 

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
            os.system('cls' if os.name=='nt' else 'clear')

            with open(file_path, "r", encoding="latin") as file:
                total_lines = len(file.readlines())
            os.system('cls' if os.name=='nt' else 'clear')
            center(banner, Fore.RED)
            Write.Print("\n\n     [•]  Selected File: TRUE", Colors.light_blue)
            time.sleep(2)
            Write.Print(f"\n\n     [•]  File Name: {file_name}", Colors.light_blue)
            time.sleep(2)
            Write.Print(f"\n\n     [•]  Total Lines: {total_lines}", Colors.light_blue)
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            return file_path
    
    def Unknowns(file_path):

        os.system('cls' if os.name == 'nt' else 'clear')

        output_folder = passtracker / "𝐑𝐞𝐬𝐮𝐥𝐭"
        output_folder.mkdir(parents=True, exist_ok=True)  

        lines_to_keep = []

        with open(file_path, 'r', encoding='latin') as file:
            for line in file:
                if re.match(r'^(https?://|android://)', line.strip()) and 'UNKNOWN' not in line.upper():
                    lines_to_keep.append(line.strip())

        if not lines_to_keep:
            Write.Print("\n\n     [!]  No lines found that meet the filtering criteria.", Colors.red)
            time.sleep(3)
            return
        
       

        total_lines = sum(1 for _ in open(file_path, 'r', encoding='latin-1'))
        removed_lines = total_lines - len(lines_to_keep)

        output_file = output_folder / f"ROBMOCLOUD[NOUNKNOWNS]-[{len(lines_to_keep)}].txt"

        with open(output_file, 'w', encoding='latin') as file:
            for line in lines_to_keep:
                file.write(line + '\n')

        center(banner, Fore.RED) 
        Write.Print(f"\n\n     [•]  Total lines: {total_lines}", Colors.light_blue)
        Write.Print(f"\n\n     [•]  Removed lines: {removed_lines}", Colors.light_blue)
        Write.Print(f"\n\n     [•]  Remaining lines: {len(lines_to_keep)}", Colors.light_blue)
        Write.Print("\n\n     [•]  Lines containing 'Unknown' have been removed.\n\n     [•]  Check the folder.", Colors.light_blue)
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')        
        time.sleep(5)

    file_path = select_file()
    Unknowns(file_path)

    os.system('cls' if os.name == 'nt' else 'clear')        
    time.sleep(5)
    MainBanner();print(Options);USERCHOICE()

def Search():
    os.system('cls' if os.name=='nt' else 'clear')

    banner =  f"""{Fore.RED}



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
    def center(text, color):
        terminal_width = shutil.get_terminal_size().columns
        for line in text.split('\n'):
            centered_text = line.center(terminal_width)
            sys.stdout.write(color + centered_text + Fore.RESET + '\n')

    os.system('cls' if os.name=='nt' else 'clear')


    def select_file():
        root = Tk()
        root.withdraw()  

        file_path = filedialog.askopenfilename(title="Select Combo File", filetypes=[("Text Files", "*.txt")])
        if not file_path:
            os.system('cls' if os.name=='nt' else 'clear')
            center(banner, Fore.RED) 
            Write.Print("\n\n     [•]  Selected File: FALSE", Colors.red)
            time.sleep(2)
            os.system('cls' if os.name=='nt' else 'clear')
            return select_file()
        else:
            file_name = os.path.basename(file_path)
        
            with open(file_path, "r", encoding="latin") as file:
                total_lines = len(file.readlines())
            os.system('cls' if os.name=='nt' else 'clear')
            center(banner, Fore.RED) 
            Write.Print("\n\n     [•]  Selected File: TRUE", Colors.light_blue)
            time.sleep(2)
            Write.Print(f"\n\n     [•]  File Name: {file_name}", Colors.light_blue)
            time.sleep(2)
            Write.Print(f"\n\n     [•]  Total Lines: {total_lines}", Colors.light_blue)
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            return file_path

    def searchurls():
        os.system('cls' if os.name == 'nt' else 'clear')
        center(banner, Fore.RED) 
        Write.Print("\n\n     Write the URL of the platform you want to search", Colors.light_blue)
        Write.Print("\n\n     For example:", Colors.light_blue)
        Write.Print("\n\n     ▪ https://www.paypal.com/", Colors.light_blue)
        Write.Print("\n\n     ▪ Or: www.paypal.com/", Colors.light_blue)


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
            center(banner, Fore.RED) 
            Write.Print("\n\n     [!]  Only URLs are allowed. Please enter a valid URL.", Colors.red)
            time.sleep(2)
            search_term = input("\n\n     >> ")

        file_path = select_file()  
        file_name = os.path.basename(file_path)
    
        os.system('cls' if os.name=='nt' else 'clear')
        center(banner, Fore.RED) 
        os.system('cls' if os.name == 'nt' else 'clear')
        Write.Print("\n\n     Updating...", Colors.red)
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

        center(banner, Fore.RED) 
        Write.Print(f"\n\n     [•]  Searching for '{search_term}'...", Colors.red)
        os.system('cls' if os.name == 'nt' else 'clear')

        search_results = []

        output_folder = passtracker / "𝐑𝐞𝐬𝐮𝐥𝐭"
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
            center(banner, Fore.RED) 
            Write.Print(f"\n\n     [▪]  Process completed successfully...", Colors.light_blue)
            Write.Print(f"\n\n     [▪]  Total lines found: {len(search_results)}", Colors.light_blue)        
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            os.system('cls' if os.name=='nt' else 'clear')
            center(banner, Fore.RED) 
            Write.Print(f"\n\n     [!]  No results found for '{search_term}'.", Colors.red)
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
    searchurls()      
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
    MainBanner();print(Options);USERCHOICE()

def Combos():
    os.system('cls' if os.name=='nt' else 'clear')

    banner = f"""{Fore.RED}



░█████╗░░█████╗░███╗░░░███╗██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗██╔════╝
██║░░╚═╝██║░░██║██╔████╔██║██████╦╝██║░░██║╚█████╗░
██║░░██╗██║░░██║██║╚██╔╝██║██╔══██╗██║░░██║░╚═══██╗
╚█████╔╝╚█████╔╝██║░╚═╝░██║██████╦╝╚█████╔╝██████╔╝
░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░░╚════╝░╚═════╝░


    """
    def center(text, color):
        terminal_width = shutil.get_terminal_size().columns
        for line in text.split('\n'):
            centered_text = line.center(terminal_width)
            sys.stdout.write(color + centered_text + Fore.RESET + '\n')

    os.system('cls' if os.name=='nt' else 'clear')

    center(banner, Fore.RED) 

    def select_file():
        root = Tk()
        root.withdraw()  

        file_path = filedialog.askopenfilename(title="Select Combo File", filetypes=[("Text Files", "*.txt")])
        if not file_path:
            os.system('cls' if os.name=='nt' else 'clear')
            center(banner, Fore.RED) 
            Write.Print("\n\n     [•]  Selected File: FALSE", Colors.red)
            time.sleep(2)
            os.system('cls' if os.name=='nt' else 'clear')
            return select_file()
        else:
            file_name = os.path.basename(file_path)
        
            with open(file_path, "r", encoding="latin") as file:
                total_lines = len(file.readlines())

            os.system('cls' if os.name=='nt' else 'clear')
            center(banner, Fore.RED) 
            Write.Print("\n\n     [•]  Selected File: TRUE", Colors.light_blue)
            time.sleep(2)
            Write.Print(f"\n\n     [•]  File Name: {file_name}", Colors.light_blue)
            time.sleep(2)
            Write.Print(f"\n\n     [•]  Total Lines: {total_lines}", Colors.light_blue)
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            return file_path

    def Combo():
        file_path = select_file()
        if not file_path:
            Combo()
            return  
        tempfile = passtracker / f"COMBOS.txt"
        os.system('cls' if os.name == 'nt' else 'clear')
        center(banner, Fore.RED) 
        Write.Print("\n\n     Write the URL of the platform you want to search", Colors.light_blue)
        Write.Print("\n\n     For example:", Colors.light_blue)
        Write.Print("\n\n     ▪ https://www.paypal.com/", Colors.light_blue)
        Write.Print("\n\n     ▪ Or: www.paypal.com/", Colors.light_blue)
 
        search_term = input("\n\n     >> ")
    
        url_regex = re.compile(
            r'^(?:http|ftp)s?://'  
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  
            r'localhost|'  
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  
            r'(?::\d+)?'  
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if not re.match(url_regex, search_term):
            os.system('cls' if os.name == 'nt' else 'clear')
            center(banner, Fore.RED) 
            Write.Print("\n\n     [!]  Only URLs are allowed. Please enter a valid URL.", Colors.light_blue)
            time.sleep(2)
            search_term = input("\n\n     >> ")

        os.system('cls' if os.name == 'nt' else 'clear')
        Write.Print("\n\n     Updating...", Colors.red)
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        center(banner, Fore.RED) 
        Write.Print(f"\n\n     Searching for '{search_term}'...", Colors.red)
        os.system('cls' if os.name == 'nt' else 'clear')

        search_results = []

        with open(file_path, 'r', encoding='latin') as file:
            for line in file:
                if line.strip().startswith(("http", "https", "android")):
                    if search_term.lower() in line.lower():
                        search_results.append(line.strip())
    
        if search_results:
            with open(tempfile, 'w', encoding='latin') as output_file:
                for result in search_results:
                    output_file.write(result + '\n')
            center(banner, Fore.RED) 
            Write.Print(f"\n\n     ▪   Process completed successfully...", Colors.light_blue)
            Write.Print(f"\n\n     ▪   Total lines found: {len(search_results)}", Colors.light_blue)
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            center(banner, Fore.RED) 
            Write.Print(f"\n\n     [!]  No results found for '{search_term}'.", Colors.red)
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')

        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')

        Emails(tempfile)
        Numbers(tempfile)

    def Emails(tempfile):
        result_list = []
        with open(tempfile, 'r', encoding='latin') as input_file:
            lines = input_file.readlines()
    
        for line in lines:
            matches = re.findall(r'[\w.-]+@[\w.-]+:\S+', line)
            if matches:
                result_list.extend(matches)
    
        output_folder = passtracker / "𝐑𝐞𝐬𝐮𝐥𝐭"  
        output_folder.mkdir(parents=True, exist_ok=True)  

        output_file_path = output_folder / f"Emails-{datetime.now().strftime('[%H%M%S]')}.txt"
        with open(output_file_path, 'w', encoding='latin') as output_file:
            for result in result_list:
                output_file.write(f'{result}\n')
            center(banner, Fore.RED) 
        Write.Print("\n\n     ▪   File: Emails - Process Completed Successfully", Colors.light_blue)
        time.sleep(3)

    def Numbers(tempfile):
        result_list = []
        with open(tempfile, 'r', encoding='latin') as input_file:
            lines = input_file.readlines()

        for line in lines:
            matches = re.match(r'^.*?(\d{9,}):(.+)$', line)
            if matches:
                number, password = matches.groups()
                result_list.append(f'{number}:{password}')

        output_folder = passtracker / "𝐑𝐞𝐬𝐮𝐥𝐭" 
        output_folder.mkdir(parents=True, exist_ok=True) 

        output_file_path = output_folder / f"Numbers-{datetime.now().strftime('[%H%M%S]')}.txt"
        with open(output_file_path, 'w', encoding='latin') as output_file:
            for result in result_list:
                output_file.write(f'{result}\n')
        Write.Print("\n\n     ▪   File: Numbers - Process Completed Successfully", Colors.light_blue)
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(3)

        try:
            os.remove(tempfile)
        except FileNotFoundError:
            pass
        tempfile = passtracker / "COMBOS.txt"

    Combo()

    MainBanner();print(Options);USERCHOICE()


Options = (Fore.BLUE+"""

                                    Please Select Your Option:

                                    [1] Remove Duplicates.

                                    [2] Remove UNKNOWN.

                                    [3] Search URL's

                                    [4] URL's to Combo

""")

print(Options)

def USERCHOICE():
    User_Option = input(Fore.WHITE+"                                     >>   ")
    
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
        Combos()

USERCHOICE()
