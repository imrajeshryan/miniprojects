import argparse
import os
#importing local modules
from modules.extension import byExtension
from modules.dateModified import byDateModified
from modules.fileSize import byFileSize
from modules.alphabet import byAlphabet

#main function which call all other functions
def main(organizeBy, directory):
    if organizeBy == "byextension":
        print("Organizing By File extension...")
        byExtension(directory) 
    elif organizeBy == "bydatemodified":
        print("Organizing By Date Modified...")
        byDateModified(directory)
    elif organizeBy == "byfilesize":
        print("Organizing By File Size...")
        byFileSize(directory)
    elif organizeBy == "byalphabet":
        print("Organizing by Alphabets...")
        byAlphabet(directory)
        
#to validate the path string provided by user
def validate_folder_path (user_path):
    if not os.path.exists(user_path):
        raise argparse.ArgumentTypeError("'{}' path doesn't exist".format(user_path))
    return user_path

#driver code
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    cwd = os.getcwd()
    parser.add_argument("--organize", 
                        help=" Current default = byextension. Use lower alphabets only!",
                        default="byextension",
                        choices=["byfilesize", "bydatemodified", "byalphabet", "byextension"])
    parser.add_argument("--directory", help="Enter Folder Path within double quotes"
                        + " Current Default = {} (Current Directory)".format(cwd),type=validate_folder_path,
                        default=cwd)
    args = parser.parse_args()
    
    main(args.organize, args.directory)
    