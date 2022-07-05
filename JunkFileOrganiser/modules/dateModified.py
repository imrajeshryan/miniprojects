from pathlib import Path
import os
import shutil
import datetime

def byDateModified(current_directory):
    #converting to Path type
    current_directory = Path(current_directory)
    for item in current_directory.iterdir():
        if not item.is_dir():
            file_path = Path(item)
            
            #Getting epoch time and converting to standard date-month-year
            epoch_time = os.stat(item).st_mtime #returns a float
            date_modified = datetime.datetime.fromtimestamp(epoch_time).strftime('%d-%m-%Y')
            
            new_path = current_directory.joinpath(date_modified)
            
            if not new_path.exists():
                new_path.mkdir()
            shutil.move(file_path, new_path)