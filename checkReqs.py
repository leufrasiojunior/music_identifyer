import os

# Global Variables
folder_destiny = "upload/"
editedFolder = "editedFiles/"

# Verify if upload folder exist. If not, create
if not os.path.exists(folder_destiny):
    os.mkdir(folder_destiny)

if not os.path.exists(editedFolder):
    os.mkdir(editedFolder)
