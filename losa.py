import os
import requests
from time import sleep
from os import system
from colorama import Fore, Style
from bomber import Bomber

system("cls||clear")

print(
    """{}
    __                                   
   / /___  _________ _                   
  / / __ \/ ___/ __ `/         Güncellemeler          
 / / /_/ (__  ) /_/ /          Kontrol Ediliyor...          
/_/\____/____/\__,_/      __             
   / /_  ____  ____ ___  / /_  ___  _____
  / __ \/ __ \/ __ `__ \/ __ \/ _ \/ ___/
 / /_/ / /_/ / / / / / / /_/ /  __/ /    
/_.___/\____/_/ /_/ /_/_.___/\___/_/                                                                     
by @losa.dev """.format(Fore.LIGHTRED_EX)
)

# GitHub deposunun URL'si ve dosya yollarını ayarladık
github_repo_url = 'https://raw.githubusercontent.com/LewisLosa/losa-bomber/main'
file_paths = ['version.txt', 'sms.py', 'bomber.py', 'requirements.txt']

# Güncelleme kontrolü ve indirme işlemleri
for file_path in file_paths:
    remote_file_url = f'{github_repo_url}/{file_path}'
    local_file_path = os.path.basename(file_path)

    response = requests.get(remote_file_url)
    
    if response.status_code == 200:
        remote_content = response.content.decode('utf-8').strip()
        local_content = ''

        if os.path.exists(local_file_path):
            with open(local_file_path, 'r', encoding='utf-8') as local_file:
                local_content = local_file.read().strip()

        if remote_content != local_content:
            with open(local_file_path, 'wb') as local_file:
                local_file.write(response.content)
            print(f"{file_path} güncellendi.")
            sleep(1)
        else:
            print(f"{file_path} güncel.")
            sleep(0.5)
    else:
        print(f"{file_path} dosyası indirilemedi.")
        sleep(1)
Bomber()
