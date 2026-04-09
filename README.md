# 🗂️ Python File Organizer

A Python-based desktop utility that automatically organizes files into categorized folders and provides a safe restore (desort) feature to return files to their original state.

---

## 📌 Overview
This project was built to simplify file management by automatically sorting files based on their type. It also includes a reversible workflow, allowing users to restore files back to their original structure safely.

---

## 🚀 Features

### 📁 Organize Files
- Select any folder using a GUI (no hard-coded paths)
- Automatically sorts files into categories:
  - Images (.jpg, .png, .jpeg)
  - Documents (.pdf, .docx, .txt)
  - Videos (.mp4, .mkv)
  - Music (.mp3)
- Creates category folders automatically
- Moves unsupported file types into an **Others** folder

### 🔄 Restore (Desort) Files
- Moves files back to the original parent folder
- Removes empty category folders after restoring
- Only affects folders created by the program (safe operation)

---

## 🛠️ Tech Stack
- Python 3
- `os` (directory and path handling)
- `shutil` (file operations)
- `tkinter` (GUI folder selection)

---

## ⚙️ How It Works
- The program scans the selected directory and identifies file extensions
- Files are grouped into predefined categories
- Files are moved into corresponding folders using `shutil`
- Restore logic reverses the process by flattening folder structure
- Safety checks ensure only program-created folders are modified

---

## ▶️ How to Run

1. Make sure Python 3 is installed  
2. Clone the repository:
   ```bash
   git clone https://github.com/ommpatel142/PythonFileOrganizer.git
