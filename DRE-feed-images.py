import os
import json
import shutil
import datetime

# Define the allowed file extension
allowed_extension = ".jpg"

# Define the source and destination directories
src_dir = "/Users/jjesuyver/Documents/GitHub/DrawBotsDesigns/explorations"
dest_dir = "/Users/jjesuyver/Documents/GitHub/dre05119071/src/images"
json_dir = "/Users/jjesuyver/Documents/GitHub/dre05119071/src/_data"

# Get the list of subdirectories in the source directory
subdirs = [d for d in os.listdir(src_dir) if os.path.isdir(os.path.join(src_dir, d))]

# Initialize an empty dictionary to store file information
file_info = {}

# Loop through each subdirectory and get information about its files
# But only for subdirs containing a hero image
my_subdirs = []
for subdir in subdirs:
    subdir_path = os.path.join(src_dir, subdir)
    files = os.listdir(subdir_path) # Get the list of files in the subdirectory
    for file in files:
        if  file.endswith("hero.jpg"):
            my_subdirs.append(subdir)
            # print(my_subdirs)

# Loop through each SELECTED subdirectory and get information about its files
for subdir in my_subdirs:
    subdir_path = os.path.join(src_dir, subdir)
    # print(subdir_path)
    # Keep track of the file count within each folder
    file_count = 1
    # list the files in my_subdirs
    files = os.listdir(subdir_path) 
    # Loop through each file and get information about it    
    for file in files:
        if file.endswith(allowed_extension):
            file_path = os.path.join(subdir_path, file)
            # file_size = os.path.getsize(file_path)
            file_creation_time = os.path.getctime(file_path)
            file_creation_date = datetime.datetime.fromtimestamp(file_creation_time).strftime('%Y-%m-%d %H:%M:%S')
            file_creation_year = datetime.datetime.fromtimestamp(file_creation_time).strftime('%Y')
                
            # Extract the relevant parts of the filename and folder name and create new fields
            gallery = subdir.replace("-", " ").capitalize()
            date = file_creation_date
            src = "{}-{}".format(subdir, file_count) + allowed_extension
            # linkToAuthor = "https://www.opensea.io/" + subdir + "/" + src
            linkToAuthor = "https://www.opensea.io/" + subdir + "-by-dre"
            title = subdir.replace("-", " ").capitalize() + " " + str(file_count)
            alt = title
            credit = title + " by DRE ©" + str(file_creation_year)
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
            file_count += 1

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
with open(os.path.join(json_dir, "images.json"), "w") as f:
     json.dump(new_data, f, indent=4)

# Copy and rename the files from the source directory to the destination directory

for subdir in subdirs:
    subdir_path = os.path.join(src_dir, subdir)
    dest_subdir_path = os.path.join(dest_dir, subdir)
    if os.path.exists(dest_subdir_path):
        # just a test
        # print(dest_subdir_path)
        
        # Get the list of files in the subdirectory
        files = os.listdir(subdir_path)
        
        # Keep track of the file count within each folder
        file_count = 1

        # Loop through each file and copy and rename it
        for file in files:
            if file.endswith(allowed_extension):
                src_path = os.path.join(subdir_path, file)
                new_file_name = "{}-{}".format(subdir, file_count) + allowed_extension
                dest_path_1 = os.path.join(dest_subdir_path, new_file_name)
                dest_path = os.path.join(dest_dir, dest_path_1 )
                shutil.copy2(src_path, dest_path)
                file_count += 1
