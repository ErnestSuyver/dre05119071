from PIL import Image
import os

# Specify the input and output folders
input_folder = '/Users/jjesuyver/Documents/GitHub/dre05119071/src/images/triangles-1'
output_folder = input_folder

# Make sure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.jpeg') or filename.endswith('.webp'):
        # Open the image
        with Image.open(os.path.join(input_folder, filename)) as img:
            # Convert the image to 'RGB' mode to ensure compatibility with JPEG
            img = img.convert('RGB')
            # Resize the image to 640x640
            img = img.resize((640, 640), Image.ANTIALIAS)
            # Save the resized image to the output folder with the same name
            img.save(os.path.join(output_folder, filename))

print("Resizing and saving completed.")
