import os


def get_images_of_directory(path):
    directory_structure = os.walk(path)
    for contents in directory_structure:
        dirpath, dirnames, images = contents
        return images