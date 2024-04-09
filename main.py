#   External libaries used in the following scipt
import streamlit as st
import os
from pathlib import Path

#   Modules from subfolders
from sub_functions.dup_checker import compare_files 

#*********************************************************************
#   Function to display the interactable UI can be found under here !!
#*********************************************************************

#   Streamlit UI
def main():
    st.title("Folder Comparison Tool")
    
    st.header("Select Folders")
    check_folder = st.text_input("Folder with duplicated files:")
    dump_folder = st.text_input("Dumping folder for the duplicates:")

    start_button = st.button("Start duplicate check")

    # When start button is pressed: check if folders are valid and the proceed to call "compare files" function with the folders as args
    if start_button:
        if (not os.path.exists(Path(check_folder)) or not os.path.exists(Path(dump_folder))) or (check_folder == "" or dump_folder == ""):
            st.error("Please enter valid folder paths!")
        else:
            st.write("Checking started...")
            progress_bar = st.progress(0)
            time_text = st.empty()
            time_text.text(f"Calculating time left...")
            
            curr_file_text = st.empty()
            curr_file_text.text("Waiting for file to delete...")
            
            # Calls function to compare files in givin folders
            compare_files(check_folder, dump_folder, progress_bar, time_text, curr_file_text)

if __name__ == "__main__":
    main()
