import os

# Define the directory where your files are located
source_directory = r"C:\Users\lenovo\Desktop\python\New folder"

# Create a dictionary to map file extensions to folder names
extension_to_folder = {
    "jpg": "Images",
    "png": "Images",
    "txt": "Text",
    "pdf": "PDFs",
}

# Iterate over the files in the source directory
for file in os.listdir(source_directory):
    if os.path.isfile(os.path.join(source_directory, file)):
        # Get the file extension
        file_extension = file.split(".")[-1].lower()

        # Check if the extension is in our mapping
        if file_extension in extension_to_folder:
            # Get the folder name for the extension
            folder_name = extension_to_folder[file_extension]

            # Create the destination folder if it doesn't exist
            destination_folder = os.path.join(source_directory, folder_name)
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Rename and move the file to the destination folder
            new_filename = os.path.join(destination_folder, file)
            os.rename(os.path.join(source_directory, file), new_filename)

print("Files sorted and renamed.")