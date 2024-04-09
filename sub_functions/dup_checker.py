#   External libaries used in the following scipt
import streamlit as st
import os, hashlib, shutil
from datetime import datetime
from pathlib import Path

#   Modules from subfolders
from sub_functions.relative_paths import list_files 

def compare_files(primary_folder, destination_folder, progress_bar, time_left, currently_deleted_file):
    
    total_byte_size, file_list = list_files(primary_folder)
    
    unique_MD5s = dict()

    processed_data = 0
    
    deleted_files = 0
    
    start_timecode = datetime.now().strftime('%H:%M:%S.%f')


    for file in file_list:
        progress_data = processed_data/total_byte_size
        progress_bar.progress(progress_data)
        
        if file != file_list[0]:
            time_estimate = datetime.now().strftime('%H:%M:%S.%f')
            
            curr_used_time = (time_to_float(time_estimate) - time_to_float(start_timecode))
            time_left_guess = str(100/(progress_data * 100) * curr_used_time - curr_used_time)
            
            time_text_seconds = time_left_guess[:5] + " Estimated seconds to done!"
            time_text_minutes = str(float(time_left_guess[:5])/60)[:5] + " Minutes!"
            
            time_left.text(time_text_seconds + " / " + time_text_minutes)
        
        full_path = os.path.join(primary_folder, file)
        processed_data += os.path.getsize(full_path)

        file_pathlib = Path(full_path)
        if file_pathlib.is_file():

            fileHash = hashlib.md5(open(file_pathlib, 'rb').read()).hexdigest()

            if fileHash not in unique_MD5s:
                unique_MD5s[fileHash] = file_pathlib

            else:
                new_path = os.path.join(destination_folder, file)
                shutil.copy(file_pathlib, new_path)
                os.remove(file_pathlib)
                currently_deleted_file.text(f"Successfully deleted {file}")
                deleted_files += 1
        else:
            print("Path not exits")
            
    st.write(str(deleted_files) + " files deleted!")

# Calculate a string in the format "%H:%M:%S.%f" to a float of seconds
def time_to_float(time_str):
    listen = time_str.split(':')
    seconds_time = float(listen[2][:-4]) + 60 * (int(listen[1]) + 60 * int(listen[0]))
    return seconds_time