# Python File Organizer

A simple Python desktop utility that organizes files inside a selected folder based on file type.  
The user chooses a folder using a graphical dialog, and files are automatically sorted into categorized subfolders.

---

## Features

- Select any folder using a GUI (no hard-coded paths)
- Automatically organizes files by extension
- Creates folders dynamically if they don’t already exist
- Supports common file types:
  - Images (`.jpg`, `.png`, `.jpeg`)
  - Documents (`.pdf`, `.docx`, `.txt`)
  - Videos (`.mp4`, `.mkv`)
  - Music (`.mp3`)
- Unrecognized files are moved into an **Others** folder

---

## Technologies Used

- Python 3
- `os` and `shutil` for file system operations
- `tkinter` for GUI folder selection

---

## How to Run

1. Make sure Python 3 is installed
2. Clone the repository:
   ```bash
   git clone https://github.com/ommpatel142/PythonFileOrganizer.git
