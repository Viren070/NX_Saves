import os
import urllib.parse

base_dir = 'nintendo/switch/savegames'
base_url = 'https://github.com/Viren070/NX_Saves/raw/main/nintendo/switch/savegames/'

with open('index.md', 'w', encoding='utf-8') as f:
    for filename in os.listdir(base_dir):
        encoded_filename = urllib.parse.quote(filename)  # URL encode the filename
        download_url = base_url + encoded_filename
        f.write(f'[{filename}]({download_url})\n\n\n')