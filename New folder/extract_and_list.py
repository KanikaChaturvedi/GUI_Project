import os
import tkinter as tk
from tkinter import filedialog
import zipfile
import docker

def select_zip_file():
    file_path = filedialog.askopenfilename(filetypes=[("ZIP Files", "*.zip")])
    if file_path:
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall()

        list_files()

def list_files():
    files = os.listdir()
    for file in files:
        print(file)

root = tk.Tk()
root.withdraw()

select_zip_file()
