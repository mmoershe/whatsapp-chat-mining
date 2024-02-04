import os, sys
import shutil
import csv 

from modules import CONST
from modules.txt_operations import get_initial_txt_path, clean_txt


def setup(TEMP_DIR):
    if os.path.exists(TEMP_DIR) and len(os.listdir(TEMP_DIR)) > 0:
        all_temp_files: list = [file for file in os.listdir(TEMP_DIR)]
        print(f"Found {len(all_temp_files)} files in the tempo directory {all_temp_files}. They will be deleted.")
        shutil.rmtree(TEMP_DIR)
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)


if __name__ == '__main__':
    setup(TEMP_DIR=CONST.TEMP_DIR)