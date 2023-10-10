import os
import requests
from time import sleep
from os import system
from colorama import Fore, Style
from bomber import Bomber
from rich.progress import Progress

system("cls||clear")

print(
    """{}
    __                                   
   / /___  _________ _                   
  / / __ \/ ___/ __ `/         Kodlar          
 / / /_/ (__  ) /_/ /          Hazırlanıyor...          
/_/\____/____/\__,_/      __             
   / /_  ____  ____ ___  / /_  ___  _____
  / __ \/ __ \/ __ `__ \/ __ \/ _ \/ ___/
 / /_/ / /_/ / / / / / / /_/ /  __/ /    
/_.___/\____/_/ /_/ /_/_.___/\___/_/                                                                     
by @losa.dev """.format(Fore.LIGHTRED_EX)
)

github_repo_url = 'https://raw.githubusercontent.com/LewisLosa/losa-bomber/main'
file_paths = ['version.txt', 'sms.py', 'bomber.py', 'requirements.txt', 'losa.py']

# Kendi dizininde version.txt dosyası ara
local_version_path = os.path.join(os.getcwd(), 'version.txt')

# Dosya varsa, içeriğini oku
if os.path.exists(local_version_path):
    with open(local_version_path, 'r', encoding='utf-8') as local_file:
        local_version = local_file.read().strip()

# GitHub'dan version.txt dosyasını indir
remote_version_path = f'{github_repo_url}/version.txt'
response = requests.get(remote_version_path)

# Dosya varsa, içeriğini oku
if response.status_code == 200:
    remote_version = response.content.decode('utf-8').strip()

# Dosyalar aynı ise güncelleme yapma
if local_version == remote_version:
    print('Dosyalar güncel.')
    Bomber()
else:
    print('Dosyalar güncel değil. İndiriliyor...')

    # İlerleme çubuğu oluştur
    with Progress() as progress:
        task = progress.add_task("[red]Güncelleniyor...", total=len(file_paths))

        # Dosya yollarını ve sürümleri tutacak bir sözlük oluştur
        file_versions = {}

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

                # Eğer dosya version.txt ise sürüm bilgisini sakla
                if file_path == 'version.txt':
                    file_versions[file_path] = remote_content

                if remote_content != local_content:
                    with open(local_file_path, 'wb') as local_file:
                        local_file.write(response.content)
                    sleep(0.5)
                else:
                    sleep(0.5)

            # Dosya adını ilerleme çubuğu görev başlığına ekleyin
            progress.update(task, completed=1, description=f"[red]{file_path}")
# İndirme işlemi tamamlandığında Bomber'ı başlat
Bomber()









