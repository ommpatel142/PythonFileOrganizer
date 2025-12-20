import os
import shutil
import tkinter as tk
from tkinter import filedialog

# ==========================================
# Python File Organizer
# Organizes files by extension
# ==========================================

# File type mapping
FILE_TYPES = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3"]
}

def choose_folder():
    """
    Opens a folder selection dialog and returns selected path
    """
    root = tk.Tk()
    root.withdraw()  # Hide main tkinter window
    folder_path = filedialog.askdirectory(title="Select a folder to organize")
    return folder_path


def organize_files(target_folder):
    if not target_folder:
        print("No folder selected. Exiting...")
        return

    for file in os.listdir(target_folder):
        file_path = os.path.join(target_folder, file)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        moved = False
        file_ext = os.path.splitext(file)[1].lower()

        for folder, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                dest_folder = os.path.join(target_folder, folder)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, file))
                print(f"Moved: {file} → {folder}")
                moved = True
                break

        if not moved:
            other_folder = os.path.join(target_folder, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, file))
            print(f"Moved: {file} → Others")

def restore_files(target_folder):
    """
    Moves files back from category folders into the main folder
    and deletes empty folders.
    """
    if not target_folder:
        print("No folder selected. Exiting...")
        return

    for folder in os.listdir(target_folder):
        folder_path = os.path.join(target_folder, folder)

        # Only process folders we created
        if os.path.isdir(folder_path) and folder in list(FILE_TYPES.keys()) + ["Others"]:
            for file in os.listdir(folder_path):
                src = os.path.join(folder_path, file)
                dst = os.path.join(target_folder, file)
                shutil.move(src, dst)
                print(f"Restored: {file}")

            # Remove empty folder
            os.rmdir(folder_path)

    print("Folder restored to original state.")


if __name__ == "__main__":
    selected_folder = choose_folder()

    choice = input(
        "Type O to organize files or R to restore files: "
    ).strip().upper()

    if choice == "O":
        organize_files(selected_folder)
    elif choice == "R":
        restore_files(selected_folder)
    else:
        print("Invalid option.")

