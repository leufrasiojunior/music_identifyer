from tkinter import filedialog, messagebox
import os, shutil

from checkReqs import *
from curses import *
from cutFiles import convert_file_to_send

# Ask the user to upload music files to recognize
music_Files = filedialog.askopenfilename(
    multiple=True,
    filetypes=[("Music Files", ".mp3")],
)

if len(music_Files) > 100:
    messagebox.showerror("Erro", "Você só pode selecionar até 100 arquivos.")
else:
    for file in music_Files:
        shutil.copy2(file, folder_destiny)

# List all music files
allmusicFiles = os.listdir(folder_destiny)

for musicFile in allmusicFiles:
    musicToEdit = os.path.join(folder_destiny, musicFile)
    convert_file_to_send(musicToEdit, musicFile)
