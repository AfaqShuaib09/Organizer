import os

from constant import FILE_TYPE, FILE_IGNORE, FILE_EXT_IGNORE

def organize_files():
    """
    Organize files in the current directory.
    """
    for file_format in FILE_TYPE.keys():
        try:
            os.mkdir(file_format)
        except FileExistsError:
            pass
    # list all files in current directory
    for file in os.listdir():
        # get file extension
        file_ext = os.path.splitext(file)[1]
        print(file_ext)
        # check if file is in ignore list
        if file in FILE_IGNORE or file_ext in FILE_EXT_IGNORE:
            continue
        elif file_ext in FILE_TYPE['software']:
            os.rename(file, os.path.join('software', file))
        elif file_ext in FILE_TYPE['audio']:
            os.rename(file, os.path.join('audio', file))
        elif file_ext in FILE_TYPE['doc']:
            os.rename(file, os.path.join('doc', file))
        elif file_ext in FILE_TYPE['image']:
            os.rename(file, os.path.join('image', file))
        elif file_ext in FILE_TYPE['video']:
            os.rename(file, os.path.join('video', file))
        else:
            os.rename(file, os.path.join('other', file))

if __name__ == '__main__':
    organize_files()
