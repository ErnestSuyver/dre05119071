import os
import json
import shutil
import datetime

# Define the allowed file extension
allowed_extension = ".jpg"

# Define the source and destination directories
src_dir = "/Users/jjesuyver/Documents/GitHub/DrawBotsDesigns/explorations"
dest_dir = "/Users/jjesuyver/Documents/eleventy-tests/DRE_03/src/images"
json_dir = "/Users/jjesuyver/Documents/eleventy-tests/DRE_03/src/_data"

# Get the list of subdirectories in the source directory
subdirs = [d for d in os.listdir(src_dir) if os.path.isdir(os.path.join(src_dir, d))]

# Initialize an empty dictionary to store file information
file_info = {}

# Loop through each subdirectory and get information about its files
for subdir in subdirs:
    subdir_path = os.path.join(src_dir, subdir)

    # Get the list of files in the subdirectory
    files = os.listdir(subdir_path)
    # just a test
    # print(len(files))

    # Loop through each file and get information about it
    for file in files:
        if file.endswith(allowed_extension):
            if "hero" in file:
                file_path = os.path.join(subdir_path, file)
                file_size = os.path.getsize(file_path)
                file_creation_time = os.path.getctime(file_path)
                file_creation_date = datetime.datetime.fromtimestamp(file_creation_time).strftime('%Y-%m-%d %H:%M:%S')
            
                # Extract the relevant parts of the filename and folder name and create new fields
                title = subdir.replace("-", " ").capitalize()
                date = file_creation_date
                credit = "Created with DrawBot"
                src = subdir + "-hero" + allowed_extension
                linkToAuthor = "https://www.opensea.io/" + subdir
                alt = "FILL THIS OUT MANUALLY"
                imgDir = "/images/" + subdir + "/"
                file_info[file] = {
                    "title": title,
                    "date": date,
                    "credit": credit,
                    "linkToAuthor": linkToAuthor,
                    "src": src,
                    "alt": alt,
                    "imgDir": imgDir,
                }

# just a test
# print(file_info)

# Create a new list to store the modified data
new_data = []

# Iterate over the items in the original data
for item in file_info.values():
    new_data.append(item)

# just a test
# print(new_data)

# Dump the new data to a file
with open(os.path.join(json_dir, "drecolls.json"), "w") as f:
     json.dump(new_data, f, indent=4)

'''
The idea is simple. 
If a directory in /explorations/ in the DrawBot folder has an image with the string "hero" in the file name.
Then a JSON object is created and written into the file.
The file therefore contains only DRE site worth collections.
A folder without a hero image is not a collection.
All that remains to be done is add descriptions for the collections.
These are added under the `alt` key in the JSON objects.
'''

# Copy the hero images from the source directory to the destination directory

# First, create a new directory in the destination with the same name as the source directory
# but only if it contains a hero image
for subdir in subdirs:
    subdir_path = os.path.join(src_dir, subdir)
    dest_subdir_path = os.path.join(dest_dir, subdir)
    if not os.path.exists(dest_subdir_path):
        files = os.listdir(subdir_path)
        for file in files:
                if "hero" in file:
                    os.makedirs(dest_subdir_path)

    # Get the list of files in the subdirectory
    files = os.listdir(subdir_path)
    for file in files:
        if "hero" in file:
            src_path = os.path.join(subdir_path, file)
            dest_path_1 = os.path.join(dest_subdir_path, file)
            dest_path = os.path.join(dest_dir, dest_path_1 )
            shutil.copy2(src_path, dest_path)
