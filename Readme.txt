github.com/dhruv-gitt

Description:

This Python script is designed to help you organize files in a specified directory by sorting them into separate folders based on their file types (extensions) and renaming them in the process. It is a handy tool for keeping your files neatly organized, especially when dealing with a large number of files with different extensions.

Features:

Automatically organizes files by their extensions into separate folders.
Renames files based on their order within each folder.
Customizable to include additional file types and folder names.
Usage:

Place the script in the same directory where you want to organize your files.

Open the script in a code editor and customize the source_directory and extension_to_folder variables to match your specific needs. You can add or remove file extensions and corresponding folder names as necessary.

Run the script, and it will automatically sort and rename the files in the specified directory.

Example:

Suppose you have a directory called "New folder" containing a mix of JPEG images, PNG images, text files, and PDFs. After running the script, your directory will be organized
as follows:

 -New folder
    - Images
        - 1.jpg
        - 2.jpg
        - 3.png
        - 4.png
    - Text
        - 1.txt
        - 2.txt
    - PDFs
        - 1.pdf

Now, each file is sorted into an appropriate folder, and they are renamed with a numerical prefix based on their order within each folder.