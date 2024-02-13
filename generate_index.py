import os
import urllib.parse

base_dir = 'nintendo/switch/savegames'
base_url = 'https://github.com/Viren070/NX_Saves/raw/main/nintendo/switch/savegames/'

with open('index.md', 'w', encoding='utf-8') as f:
    # List filenames and sort them alphabetically
    filenames = sorted(os.listdir(base_dir))
    
    for filename in filenames:
        encoded_filename = urllib.parse.quote(filename)  # URL encode the filename
        if "~" in filename or "_" in filename:
            filename = filename.replace("~", "\\~")
        download_url = base_url + encoded_filename
        f.write(f'[{filename}]({download_url})\n\n\n')