import os
import json
import shutil
import datetime
from pathlib import Path as pt
from PIL import Image

# Define the allowed file extension
allowed_extensions = [".jpeg", ".webp"]

# Define the source and destination directories
src_dir = '/Users/jjesuyver/Documents/GitHub/DrawBotsDesigns/explorations'
dest_dir = '/Users/jjesuyver/Documents/GitHub/dre05119071/src/images'
json_dir = '/Users/jjesuyver/Documents/GitHub/dre05119071/src/_data'

# Get the list of subdirectories in the source directory
subdirs = [d for d in os.listdir(src_dir) if os.path.isdir(os.path.join(src_dir, d))]
# print("subdirectories in the source directory", subdirs)

# Initialize an empty dictionary to store file information
file_info = {}

# Loop through each subdirectory and get information about its files
# But only for subdirs containing a hero image
my_subdirs = []
for subdir in subdirs:
    subdir_path = os.path.join(src_dir, subdir)
    files = os.listdir(subdir_path) # Get the list of files in the subdirectory
    for file in files:
        if  file.endswith("hero.jpeg"):
            my_subdirs.append(subdir)
            # print("subdirs containing a hero image", my_subdirs)

# Loop through each SELECTED subdirectory and get information about its files
for subdir in my_subdirs:
    subdir_path = os.path.join(src_dir, subdir)
    # print("Mijn subdir_path is", subdir_path)
    
    # list the files in my_subdirs
    files = os.listdir(subdir_path) 
    # print("Files with allowed extensions within selected subdirs", files)

    # Loop through each file and get information about it    
    for file in files:
        for allowed_extension in allowed_extensions: #eigenlijk klopt de volgorde van deze loops niet
            if "hero" in file:
                print("Ha! Er zit een held in je bestand", file)
            elif file.endswith(allowed_extension):
                # print("File with allowed extension within selected subdir", file)
                file_path = os.path.join(subdir_path, file)
                # file_size = os.path.getsize(file_path)
                file_creation_time = os.path.getctime(file_path)
                file_creation_date = datetime.datetime.fromtimestamp(file_creation_time).strftime('%Y-%m-%d %H:%M:%S')
                file_creation_year = datetime.datetime.fromtimestamp(file_creation_time).strftime('%Y')

                # Extract the relevant parts of the filename and folder name and create new fields
                gallery = subdir.replace("-", " ").capitalize()
                # print(gallery)
                date = file_creation_date
                # print(date)
                src = file
                #print("src is", src)
                # linkToAuthor = "https://www.opensea.io/" + subdir + "/" + src
                linkToAuthor = "https://www.opensea.io/" + subdir + "-by-ernest"
                # print(linkToAuthor)
                title = file.replace("-", " ").capitalize() #consider removing the date and extension
                title = title.split()
                title = title[0] + " " + title[1] + " " + title[2]
                print(title)
                alt = title
                credit = title + " by ERNEST ©" + str(file_creation_year)
                imgDir = "/images/" + subdir + "/"
                file_info[file] = {
                    "gallery": gallery,
                    "date": date,
                    "credit": credit,
                    "linkToAuthor": linkToAuthor,
                    "src": src,
                    "title": title,
                    "alt": alt,
                    "imgDir": imgDir,
                    "myfile": file
                }
                # print(file_info)

# Create a new list to store the modified data
new_data = []

# Iterate over the items in the original data
for item in file_info.values():
    new_data.append(item)

# just a test
# print(new_data)

# Dump the new data to a JSON file
with open(os.path.join(json_dir, "images.json"), "w") as f:
     json.dump(new_data, f, indent=4)

# Copy the files from the source directory to the destination directory
for subdir in my_subdirs:
    subdir_path = os.path.join(src_dir, subdir)
    dest_subdir_path = os.path.join(dest_dir, subdir)
    print("hier komen we vandaan", subdir_path)
    print("hier gaan we heen", dest_subdir_path)

    if os.path.exists(dest_subdir_path) == False:
        print("Attention! The destination folder does not exist!")
    
    # Get the list of files in the subdirectory
    files = os.listdir(subdir_path)
        
    # Loop through each file and copy and rename it
    # This does NOT copy any sfolders
    for file in files:
        for allowed_extension in allowed_extensions:
            if file.endswith(allowed_extension):
                src_path = os.path.join(subdir_path, file)
                dest_path = os.path.join(dest_subdir_path)
                shutil.copy(src_path, dest_path)

