from pathlib import Path
import os
import shutil

from modules.directories import return_category

def byExtension(current_directory):
    current_directory = Path(current_directory)
    for item in os.scandir(current_directory):
        if not item.is_dir():
            #currentitem's path
            file_path = Path(item)
            file_suffix = file_path.suffix.lower()
            
            #calling return_category to get the current item's catrgory 
            item_category = return_category(file_suffix)
            
            if item_category == None:
                continue
            
            #creating new_file_path using the item_category
            new_file_path = current_directory.joinpath(item_category)
            
            #Make a new directory if not created already
            if not new_file_path.is_dir():
                new_file_path.mkdir()
            shutil.move(file_path, new_file_path)