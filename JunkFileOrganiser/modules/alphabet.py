from pathlib import Path
import shutil
def byAlphabet(current_directory):
    current_directory = Path(current_directory)
    for item in current_directory.iterdir():
        if not item.is_dir():
            file_path = Path(item)
            file_alphabet = item.stem[:1].upper()
            new_path = current_directory.joinpath(file_alphabet)
            if not new_path.is_dir():
                new_path.mkdir()
            shutil.move(file_path, new_path)
