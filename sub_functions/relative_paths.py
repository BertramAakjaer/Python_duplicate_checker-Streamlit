#   External libaries used in the following scipt
import os

# Function to list all relative paths in a directory
def list_files(directory):
    
    # Empty list
    relative_paths = []
    
    # Storage size definition
    byte_size = 0
    
    # for loop going over every file in the folder and subfolders
    for root, dirs, files in os.walk(directory):
        print("hey")
        for file in files:
            # Get relative path by removing the directory path
            relative_path = os.path.relpath(os.path.join(root, file), directory)
            
            # Doesn't add "fake" files
            if relative_path != file:
                relative_paths.append(relative_path)
                byte_size += os.path.getsize(os.path.join(directory, relative_path))
                
    # Adding files from root
    for file in os.listdir(directory):
        relative_paths.append(file)
        byte_size += os.path.getsize(os.path.join(directory, file))
    
    # Returns a list
    return byte_size, relative_paths