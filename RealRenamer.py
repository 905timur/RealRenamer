import os

"""
This script renames all files in a folder to [prefix] and [sequential # suffix].
The script prompts the user to provide the prefix and the value for the suffix start.
"""

# Get user input for directory, prefix, and suffix start value
dir_path = input("Enter directory path where files are located: ")
prefix = input("Enter prefix for file names: ")
suffix_start = int(input("Enter suffix start value: "))

try:

    # Get list of files in directory
    files = os.listdir(dir_path)

    # Rename files in directory
    count = 0
    for i, file in enumerate(files):
        if os.path.isfile(os.path.join(dir_path, file)):

            # Get file extension
            ext = os.path.splitext(file)[1]

            # Construct new file name
            new_name = f"{prefix}{i+suffix_start:02d}{ext}"

            # Rename file
            os.rename(os.path.join(dir_path, file), os.path.join(dir_path, new_name))
            count += 1

    print(f"{count} files renamed successfully!")

except OSError as e:
    # Error handling
    print(f"An error occurred: {str(e)}")
    print("Files not renamed.")
