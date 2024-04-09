#   External libaries used in the following scipt
import streamlit as st
import os, hashlib, shutil
from datetime import datetime
from pathlib import Path

#   Modules from subfolders
from sub_functions.dup_checker import compare_files 

"""

  Function to display the interactable UI can be found under here !!

"""

#   Streamlit UI
def main():
    st.title("Folder Comparison Tool")

    st.header("Select Folders")
    folder1 = st.text_input("Folder with duplicates:")
    folder2 = st.text_input("Destination folder:")

    start_button = st.button("Start duplicate check")

    if start_button:
        if (not os.path.exists(Path(folder1)) or not os.path.exists(Path(folder2))) or (folder1 == "" or folder2 == ""):
            st.error("Please enter valid folder paths!")
        else:
            st.write("Checking started...")
            progress_bar = st.progress(0)
            time_text = st.empty()
            time_text.text(f"Calculating time left...")
            
            curr_file_text = st.empty()
            curr_file_text.text("Waiting for file to delete...")
            
            compare_files(folder1, folder2, progress_bar, time_text, curr_file_text)

if __name__ == "__main__":
    main()