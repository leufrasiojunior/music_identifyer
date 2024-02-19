from tkinter import filedialog, messagebox
import os, shutil

from checkReqs import *
from curses import *

# Ask the user to upload music files to recognize
music_Files = filedialog.askopenfilename(
    multiple=True,
    filetypes=[("Music Files", ".mp3")],
)
print(music_Files)
if len(music_Files) > 100:
    messagebox.showerror("Erro", "Você só pode selecionar até 100 arquivos.")
else:
    for file in music_Files:
        shutil.copy2(file, folder_destiny)

# List all music files

allmusicFiles = os.listdir(folder_destiny)
print(f"Musics {allmusicFiles}")
# completemusicFiles = [
# os.path.join(folder_destiny, allmusicFiles) for musics in allmusicFiles
# ]

for musicFile in allmusicFiles:
    print(os.path.join(folder_destiny, musicFile))
