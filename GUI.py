import tkinter as tk
import os

def list_files():
    # Use os.system to execute a command in the container to list files
    container_id = container_id_entry.get()
    command = f'docker exec {container_id} ls -a /app'
    files = os.popen(command).read().splitlines()

    # Clear previous items from the listbox
    file_listbox.delete(0, tk.END)

    # Insert the list of files into the listbox
    for file in files:
        file_listbox.insert(tk.END, file)

def open_selected_item():
    # Get the selected item from the listbox
    selected_item_index = file_listbox.curselection()
    
    if selected_item_index:
        selected_item = file_listbox.get(selected_item_index)
        
        # Get the container ID from the input field
        container_id = container_id_entry.get()

        # Construct the path to the selected item
        item_path = f'/app/{selected_item}'

        # Use the Remote - Containers extension to connect to the container
        # command = f'code --attach 6eb7900fe9cc266373632a1288e84030f4b52c3a0fe9784435560a63f4dab4b0'
        command = f'code --remote ssh-remote+container://6eb7900fe9cc266373632a1288e84030f4b52c3a0fe9784435560a63f4dab4b0'
        os.system(command)

# Create the GUI
root = tk.Tk()
root.title("Docker Container File Explorer")

container_id_label = tk.Label(root, text="Enter Container ID:")
container_id_label.pack()
container_id_entry = tk.Entry(root)
container_id_entry.pack()

list_files_button = tk.Button(root, text="List Files", command=list_files)
list_files_button.pack()

file_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=50)
file_listbox.pack()

open_selected_button = tk.Button(root, text="Open Selected in VS Code", command=open_selected_item)
open_selected_button.pack()

root.geometry("600x400")
root.mainloop()



############################################################################################################################################################################

# import tkinter as tk
# from tkinter import filedialog
# import docker
# import os

# def list_files():
#     container_id = container_id_entry.get()
#     if not container_id:
#         return
    
#     # Connect to the Docker API
#     client = docker.from_env()
    
#     try:
#         # Get the container object
#         container = client.containers.get(container_id)
        
#         # List files in the container's directory
#         files_list = container.exec_run("ls /app").output.decode().splitlines()
        
#         # Display the list of files in the GUI
#         files_listbox.delete(0, tk.END)
#         for file in files_list:
#             files_listbox.insert(tk.END, file)
            
#     except Exception as e:
#         print(f"Error: {e}")

# def open_file():
#     selected_file = files_listbox.get(tk.ACTIVE)
#     container_id = container_id_entry.get()
#     if not container_id or not selected_file:
#         return
    
#     # Connect to the Docker API
#     client = docker.from_env()
    
#     try:
#         # Get the container object
#         container = client.containers.get(container_id)
        
#         # Copy the selected file from the container to a temporary file on the host
#         with open(selected_file, "wb") as f:
#             data, _ = container.get_archive(f"/app/{selected_file}")
#             for d in data:
#                 f.write(d)
        
#         # Open the temporary file in Visual Studio Code
#         os.system(f"code {selected_file}")
        
#         # Clean up the temporary file
#         os.remove(selected_file)
        
#     except Exception as e:
#         print(f"Error: {e}")

#  Create the GUI
# root = tk.Tk()
# root.title("Docker Container File Explorer")

# container_id_label = tk.Label(root, text="Enter Container ID:")
# container_id_label.pack()
# container_id_entry = tk.Entry(root)
# container_id_entry.pack()

# list_files_button = tk.Button(root, text="List Files", command=list_files)
# list_files_button.pack()

# open_file_folder_button = tk.Button(root, text="Open File/Folder in VS Code", command=open_file_folder)
# open_file_folder_button.pack()
# root.geometry("1500x1500")
# root.mainloop()



##########################################################################################GOOD
