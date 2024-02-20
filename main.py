from tkinter import filedialog, messagebox
import os, shutil, requests, json
from dotenv import load_dotenv

from checkReqs import *
from cutFiles import convert_file_to_send

load_dotenv()
url = "https://shazam-api6.p.rapidapi.com/shazam/recognize/"

# # Ask the user to upload music files to recognize
# music_Files = filedialog.askopenfilename(
#     multiple=True,
#     filetypes=[("Music Files", ".mp3")],
# )

# if len(music_Files) > 100:
#     messagebox.showerror("Erro", "Você só pode selecionar até 100 arquivos.")
# else:
#     for file in music_Files:
#         shutil.copy2(file, folder_destiny)

# # List all music files
# allmusicFiles = os.listdir(folder_destiny)

# for musicFile in allmusicFiles:
#     musicToEdit = os.path.join(folder_destiny, musicFile)
#     convert_file_to_send(musicToEdit, musicFile)

## # remove files after cut segments
## for fileRemove in allmusicFiles:
##     os.remove(os.path.join(folder_destiny, fileRemove))

fileToUpload = "music_test/03 Papin.mp3"

with open(fileToUpload, "rb") as file:
    files = {f"upload_file": file}
    headers = {
        "X-RapidAPI-Key": os.getenv("X-RapidAPI-Key"),
        "X-RapidAPI-Host": os.getenv("X-RapidAPI-Host"),
    }
    response = requests.post(url, files=files, headers=headers)
    codeStatus = response.status_code
    # print(response.json())
    jsonResponse = response.json()
    with open("resposta.json", "w") as arquivo_json:
        json.dump(jsonResponse, arquivo_json, indent=4)
