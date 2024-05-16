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
        print(f"Error al descargar el icono: {e}")
        return None

def select_python_file():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    archivo_py = filedialog.askopenfilename(title="Selecciona el archivo .py", filetypes=(("Archivos Python", "*.py"), ("Todos los archivos", "*.*")))
    return archivo_py

def convertir_a_exe(archivo_py, icono_url):
    # Seleccionar el archivo .py
    if not archivo_py:
        print("No se seleccionó ningún archivo .py.")
        return
    
    # Descargar el icono desde la URL
    icon_path = "icon.ico"
    if not os.path.exists(icon_path):
        print("Descargando el icono...")
        if download_icon(icono_url, icon_path):
            print("Icono descargado correctamente.")
        else:
            print("Error al descargar el icono. Se utilizará el icono predeterminado.")
    
    # Ejecutar pyinstaller
    comando = f'pyinstaller --onefile --icon "{icon_path}" "{archivo_py}"'
    print(f"Ejecutando: {comando}")
    os.system(comando)

# URL del icono
icono_url = "https://raw.githubusercontent.com/ROBMO-CLOUD/PassTracker/main/Img/Logo.ico"

# Seleccionar el archivo .py
archivo_py = select_python_file()

# Convertir archivo .py a .exe
convertir_a_exe(archivo_py, icono_url)
