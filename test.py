import os

def create_folder_structure(folder_path):
  try:
    # Create the directory structure recursively, handling potential permission errors
    os.makedirs(folder_path, exist_ok=True)
    print(f"Successfully created folder structure: {folder_path}")
  except OSError as error:
    print(f"Error creating folder structure: {error}")

# Example usage
folder_path = "/path/to/create/nested/folders"
create_folder_structure(folder_path)
