import os
import shutil

# 👉 change this path to your folder
folder = "test_folder"

# check folder exists
if not os.path.exists(folder):
    print("Folder not found!")
    exit()

for file in os.listdir(folder):
    file_path = os.path.join(folder, file)

    # ignore folders
    if os.path.isdir(file_path):
        continue

    # Images
    if file.endswith((".jpg", ".png", ".jpeg")):
        img_folder = os.path.join(folder, "Images")
        os.makedirs(img_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(img_folder, file))

    # Documents
    elif file.endswith(".pdf"):
        doc_folder = os.path.join(folder, "Docs")
        os.makedirs(doc_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(doc_folder, file))

    # Videos
    elif file.endswith(".mp4"):
        vid_folder = os.path.join(folder, "Videos")
        os.makedirs(vid_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(vid_folder, file))

print("Files organized successfully ✅")