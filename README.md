# Maya Auto Save Reminder & Scene Backup

Automatically reminds you to save and backs up your current Maya scene file at regular intervals.

## 🧩 Features

- 🔔 **Save Reminder**: Notifies you every hour to save your work.
- 💾 **Scene Auto-Backup**: Creates a versioned backup of your current Maya scene every 2 hours.

## 🛠️ Requirements

- Autodesk Maya (Python 2 or 3 depending on version)
- Python packages:
  - `plyer`

## 📦 Installation

1. Clone this repo:

   ```bash
   git clone https://github.com/yourusername/maya-auto-save-reminder.git
   ```

2. Install dependencies:

   ```bash
   pip install plyer
   ```

3. Run the script inside Maya's Script Editor (Python tab) or add it to your Maya user setup:

   ```python
   import sys
   sys.path.append("path/to/your/cloned/repo")
   import autosaver
   autosaver.start_timers()
   ```

## 📁 How Backups Work

Backups are saved in the same directory as your current scene with versioned suffixes:
- Original file: `scene.ma`
- Backup file: `scene_v001.ma`, `scene_v002.ma`, ...

## 🧠 Notes

- The script uses `threading.Timer` so backups/reminders run in the background.
- You must have a saved scene open in Maya; otherwise, the backup won't trigger.
- This does not autosave — it just reminds and creates versioned copies.

## 🧑‍💻 Author

Created by [Tanisha Kashyap]([https://github.com/yourusername](https://github.com/tanisha-kp))
