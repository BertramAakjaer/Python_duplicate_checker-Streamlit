#   External libaries used in the following scipt
import streamlit as st
import os, hashlib, shutil
from datetime import datetime
from pathlib import Path

#   Modules from subfolders
from sub_functions.relative_paths import list_files 

def compare_files(primary_folder, destination_folder, progress_bar, time_left, currently_deleted_file):
    path = primary_folder
    
    files_list = os.listdir(path)

    size = 0
    for path, dirs, files in os.walk(path):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)

    unique = dict()

    target = destination_folder

    def time_to_num(time_str):
        listen = time_str.split(':')
        return float(listen[2][:-4]) + 60*(int(listen[1]) + 60*int(listen[0]))

    def lang_tid_tilbage():
        gæt_time = datetime.now().strftime('%H:%M:%S.%f')
        tid_Taget = (time_to_num(gæt_time) - time_to_num(start_time))
        procent = første/sidst * 100
        time_left.text((str((100/procent * tid_Taget) - tid_Taget)[:5] + " Estimated seconds to done!") + " / " + (str(float(str((100/procent * tid_Taget) - tid_Taget)[:5])/60)[:5] + " Minutes!"))

    sidst = size
    første = 0
    start_time = datetime.now().strftime('%H:%M:%S.%f')

    antal_Slettede_filer = 0

    for file in os.listdir(path):
        progress_bar.progress(første/sidst)
        
        if første != 0:
            lang_tid_tilbage()
        
        fp2 = os.path.join(path, file)
        første += os.path.getsize(fp2)

        file_name = Path(os.path.join(path, file))
        if file_name.is_file():

            fileHash = hashlib.md5(open(file_name, 'rb').read()).hexdigest()


            if fileHash not in unique:
                unique[fileHash] = file_name

            else:
                pat = os.path.join(target, file)
                shutil.copy(file_name, pat)
                os.remove(file_name)
                currently_deleted_file.text(f"Successfully deleted {file}")
                antal_Slettede_filer += 1
        else:
            print("Path not exits")
            
    st.write(str(antal_Slettede_filer) + " files deleted!")
