import os
import shutil
import threading
import maya.cmds as cmds
from plyer import notification

# Get current scene file in Maya
def get_current_scene():
    scene = cmds.file(q=True, sceneName=True)
    return scene if scene else None

# Generate the next version of the file
def get_next_version(file_path):
    base, ext = os.path.splitext(file_path)
    
    if "_v" in base:
        parts = base.rsplit("_v", 1)
        if parts[1].isdigit():
            new_version = int(parts[1]) + 1
            return f"{parts[0]}_v{new_version:03}{ext}"
    
    return f"{base}_v001{ext}"

# Backup function (Runs every 2 hours)
def backup_scene():
    scene_file = get_current_scene()
    
    if not scene_file:
        print("No active scene found.")
        return
    
    new_version = get_next_version(scene_file)
    shutil.copy(scene_file, new_version)
    print(f"Backup created: {new_version}")

# Save reminder function (Runs every 1 hour)
def remind_save():
    notification.notify(
        title="Save Reminder",
        message="Don't forget to save your work in Maya!",
        timeout=5
    )
    print("Save Reminder Sent!")

# Start the timers
def start_timers():
    threading.Timer(3600, remind_save).start()  # 1 hour reminder
    threading.Timer(7200, backup_scene).start()  # 2-hour backup

start_timers()
