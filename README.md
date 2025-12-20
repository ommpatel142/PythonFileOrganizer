# Python File Organizer

A Python desktop utility that allows users to **organize and restore (desort)** files inside any selected folder.

The program uses a **graphical folder selection dialog** to choose a directory and then lets the user decide whether to **organize files** or **restore them back to the original state** using a simple terminal option.

---

## Features

### 📁 Organize Files
- Select any folder using a GUI (no hard-coded paths)
- Automatically sorts files into folders based on file type:
  - Images (`.jpg`, `.png`, `.jpeg`)
  - Documents (`.pdf`, `.docx`, `.txt`)
  - Videos (`.mp4`, `.mkv`)
  - Music (`.mp3`)
- Creates category folders automatically if they do not exist
- Files with unsupported extensions are moved into an **Others** folder

### 🔄 Restore (Desort) Files
- Moves files back from category folders into the original parent folder
- Removes empty category folders after restoring
- Only processes folders created by the organizer (safe restore)

---

## Technologies Used

- Python 3
- `os` – directory and path handling
- `shutil` – moving files between folders
- `tkinter` – graphical folder selection dialog

---

## How to Run

1. Make sure **Python 3** is installed
2. Clone the repository:
   ```bash
   git clone https://github.com/ommpatel142/PythonFileOrganizer.git
   ```
3. Navigate into the project directory:
   ```bash
   cd PythonFileOrganizer
   ```
4. Run the script:
   ```bash
   python file_organizer.py
   ```
5. Select a folder using the GUI dialog
6. Choose an option in the terminal:
   - `O` → Organize files
   - `R` → Restore (desort) files

---

## Example Workflow

- **Before Organize**  
  All files are mixed in a single folder

- **After Organize**  
  Files are sorted into Images, Documents, Videos, Music, and Others folders

- **After Restore**  
  All files are moved back into the original folder and category folders are removed

---

## Notes

- The restore feature only affects folders created by this program
- Existing unrelated folders are not modified
- Safe to run multiple times

---

## Author

**Om Patel**  
Computer Engineering Technology  

