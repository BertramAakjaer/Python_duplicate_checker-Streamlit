import os

# Function to list all relative paths in a directory
def list_files(directory):
    
    # Empty list
    relative_paths = []
    
    # for loop going over every file in the folder and subfolders
    for root, _, files in os.walk(directory):
        for file in files:
            # Get relative path by removing the directory path
            relative_path = os.path.relpath(os.path.join(root, file), directory)
            
            # Doesn't add "fake" files
            if relative_path != file:
                relative_paths.append(relative_path)
                
    # Returns a list
    return relative_paths