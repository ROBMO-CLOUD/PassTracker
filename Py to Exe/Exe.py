import os
import shutil
import tkinter as tk
from tkinter import filedialog
import requests

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

def select_python_file():
    root = tk.Tk()
    root.withdraw()  
    archivo_py = filedialog.askopenfilename(title="Select the .py file", filetypes=(("Python Files", "*.py"), ("All files", "*.*")))
    return archivo_py

def convert_to_exe(archivo_py, icon_url):
    if not archivo_py:
        print("No .py file selected.")
        return
    
    icon_path = "icon.ico"
    if not os.path.exists(icon_path):
        print("Downloading the icon...")
        if download_icon(icon_url, icon_path):
            print("Icon downloaded successfully.")
        else:
            print("Error downloading the icon. Default icon will be used.")
    
    command = f'pyinstaller --onefile --icon "{icon_path}" "{archivo_py}"'
    print(f"Executing: {command}")
    os.system(command)

icon_url = "https://raw.githubusercontent.com/ROBMO-CLOUD/PassTracker/main/Img/Logo.ico"

print("     Welcome!\n")
response = input("     Do you want to convert the Tools.py file to Tools.exe? (Yes/No): ").strip().lower()

if response == "yes":
    archivo_py = "Tools.py"
    print(f"\n     Automatically selecting the file {archivo_py}...\n\n")
    
    convert_to_exe(archivo_py, icon_url)
elif response == "no":
    print("Conversion will not be performed.")
else:
    print("Unrecognized response. Conversion will not be performed.")
