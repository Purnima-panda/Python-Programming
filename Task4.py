import os
import shutil
import time

def organize_desktop_folder():
    desktop_path = os.path.expanduser("~/Desktop")
    target_folders = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
        "Videos": [".mp4", ".avi", ".mov"],
        "Compressed": [".zip", ".rar"],
        "Executables": [".exe", ".msi"]
    }
    
    for filename in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, filename)
        if os.path.isfile(file_path):
            for folder, extensions in target_folders.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    folder_path = os.path.join(desktop_path, folder)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    shutil.move(file_path, os.path.join(folder_path, filename))
                    print(f"Moved {filename} to {folder}")
                    break

if __name__ == "__main__":
    print("Organizing Desktop folder...")
    organize_desktop_folder()
    print("Task Completed!")
