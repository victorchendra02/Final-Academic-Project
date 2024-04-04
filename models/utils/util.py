import os


def create_folder(path):
    try:
        os.makedirs(path)
        print(f"Folder --> '{path}' created")
    except FileExistsError:
        print(f"Already exist --> '{path}'")
