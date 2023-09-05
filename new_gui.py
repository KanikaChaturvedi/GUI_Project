

# e7f13d9814fb0379d9b4b0b543d413195bc9627b0a98d79765dde59ac1c4acbe


import tkinter as tk
import subprocess
import docker
import os
from tkinter import filedialog
from tkinter import Listbox, Scrollbar, Button, Label
# Initialize container and selected directory paths to None
container_directory = None
selected_directory = None
container_id = None
selected_file= None

def list_container_files():
    global container_directory, container_id
    container_id = container_id_entry.get()
    command = f'docker exec {container_id} ls -a /app'
    files = os.popen(command).read().splitlines()

    # Clear previous items from the listbox
    file_listbox.delete(0, tk.END)

    # Insert the list of files into the listbox
    for file in files:
        file_listbox.insert(tk.END, file)

def download_files():
    global selected_directory, container_directory, selected_file
    selected_file = file_listbox.get(file_listbox.curselection())
    selected_directory = filedialog.askdirectory()
    # client = docker.from_env()
    # container = client.containers.get(container_id)
    # selected_file = file_listbox.get(file_listbox.curselection())
    print(selected_file)
    if selected_directory:
        # Use 'docker cp' to copy files from the container to the local system
        subprocess.run(["docker", "cp", f"{container_id}:/app/{selected_file}", selected_directory])
        print(selected_directory)
    
    if selected_directory:
        # Open VS Code with the selected directory
        subprocess.Popen(["code", selected_directory])


def upload_changes():
    global container_directory, selected_directory
    # container_id = container_id_entry.get()
    selected_directory = filedialog.askdirectory()
    if selected_directory:
        # Use 'docker cp' to copy files from the selected local directory to the container directory
        subprocess.run(["docker", "cp", f"{selected_directory}", f"{container_id}:/app"])
        print(selected_directory)


def compile_selected_file():
    selected_file = file_listbox.get(file_listbox.curselection())
    container_id = container_id_entry.get()
    try:
        client = docker.from_env()
        container = client.containers.get(container_id)
        compile_command = f"gcc -o compiled_program {selected_file}"
        container.exec_run(compile_command)
        result_label.config(text=f"Compiled {selected_file} in {container_id}")
    except docker.errors.NotFound:
        result_label.config(text="Container not found")


# Create the GUI (previous code)
root = tk.Tk()
root.title("Docker Container File Manager")

container_id_label = tk.Label(root, text="Container ID:")
container_id_label.pack()
container_id_entry = tk.Entry(root, width=70)
container_id_entry.pack()


list_files_button = tk.Button(root, text="List Files", command=list_container_files)
list_files_button.pack()

file_listbox = tk.Listbox(root, width=100)
file_listbox.pack()
scrollbar = Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
file_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=file_listbox.yview)

download_button = tk.Button(root, text="Download Files", command=download_files)
download_button.pack()

compile_button = Button(root, text="Compile Selected File", command=compile_selected_file)
compile_button.pack()

upload_changes_button = tk.Button(root, text="Upload Changes", command=upload_changes)
upload_changes_button.pack()

result_label = Label(root, text="")
result_label.pack()

root.geometry("1200x1000")
root.mainloop()
