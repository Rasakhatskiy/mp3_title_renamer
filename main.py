import sys
import os
import os.path
import ntpath
import re
from os import walk
import eyed3


# Recursively gets all file paths from given directory
def get_file_list(dirpath):
    result_paths = []
    for (dirpath, dirnames, filenames) in walk(dirpath):
        for file in filenames:
            result_paths.append(os.path.join(dirpath, file))
           
    return result_paths


# Returns only file name without path
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


# Removes numbers and extension from file name
# Returns song name
def remove_extra_text(name: str):
    # Split by dots
    parts = name.split(".")
    del parts[len(parts) - 1]

    if len(parts) > 1:
        trynum = parts[0]
        try:
            int(trynum)
            del parts[0]
        except ValueError: 
            pass
        result = ".".join(parts)    
    else:
        result = parts[0]

    # Delete leading empty space  
    return re.sub(r"^\s+", "", result)


# Renames mp3 tag title according to file name without track number and extention    
def rename_if_MP3(filepath: str):
    ext = filepath.split(".")[-1]
    if ext == "mp3":
        audio = eyed3.load(filepath)
        if audio is not None:
            audio.tag.title = remove_extra_text(path_leaf(filepath))
            audio.tag.save()


def main():
    directory = sys.argv[1]
    print(directory)

    filepath_list = get_file_list(directory)
    for path in filepath_list:
        rename_if_MP3(path)

if __name__ == "__main__":
    main()