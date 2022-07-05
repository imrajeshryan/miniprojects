from pathlib import Path
import os
import shutil

def byFileSize(current_directory):
    current_directory = Path(current_directory)
    for item in current_directory.iterdir():
        if not item.is_dir():
            file_path = Path(item)
            file_size_MB = int((os.path.getsize(file_path)) / (1024 * 1024))
            #making directories based on file size and moving the files in
            if file_size_MB <= 0:
                new_path_oneMB = current_directory.joinpath("Below 1 MB")
                if not new_path_oneMB.exists():
                    new_path_oneMB.mkdir()
                shutil.move(file_path, new_path_oneMB )
                
            elif file_size_MB <= 10 :
                new_path_tenMB = current_directory.joinpath("Below 10 MB")
                if not new_path_tenMB.exists():
                    new_path_tenMB.mkdir()
                shutil.move(file_path, new_path_tenMB )
                    
            elif file_size_MB <= 50:
                new_path_fiftyMB = current_directory.joinpath("Below 50 MB")
                if not new_path_fiftyMB.exists():
                    new_path_fiftyMB.mkdir()
                shutil.move(file_path, new_path_fiftyMB)
                
            else:
                new_path_above_fiftyMB = current_directory.joinpath("Over 50 MB")
                if not new_path_above_fiftyMB.exists():
                    new_path_above_fiftyMB.mkdir()
                shutil.move(file_path, new_path_above_fiftyMB )