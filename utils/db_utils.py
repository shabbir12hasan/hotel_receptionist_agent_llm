import shutil
import os


def remove_directory(directory):
    """
    Removes the specified directory if it exists.
    """
    
    if os.path.exists(directory):
        print(f"Removing existing directory: {directory}")
        shutil.rmtree(directory)
        print("Existing directory removed.")