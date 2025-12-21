import os
import shutil

desktop_path = os.path.expanduser("~/Desktop")
print(desktop_path)

folders = {
    "Images": [".jpeg", ".jpg", ".png", ".gif"],
    "Documents": [".docx", ".doc", ".pdf", ".txt"],
    "Archives": [".zip", ".rar"],
}

for folder_name in folders:
    folder_path = os.path.join(desktop_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

for file_name in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, file_name)
    if os.path.isfile(file_path):
        for folder_name, extensions in folders.items():
            for extension in extensions:
                if file_name.endswith(extension):
                    destination_folder = os.path.join(desktop_path, folder_name)
                    shutil.move(file_path, destination_folder)
