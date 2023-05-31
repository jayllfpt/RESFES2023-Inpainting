import os

def get_file_names(folder_path):
    file_names = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_names.append(file)
    return file_names

def write_to_txt(file_names, txt_file_path):
    with open(txt_file_path, 'w') as txt_file:
        for file_name in file_names:
            txt_file.write(file_name + '\n')

# Specify the folder path
folder_path = r'yesureresult'

# Specify the output text file path
txt_file_path = r"evaluateFiles.txt"

# Get file names from the folder
file_names = get_file_names(folder_path)

# Write file names to a text file
write_to_txt(file_names, txt_file_path)
