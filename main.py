import os, sys
import shutil
import csv 
from time import sleep

from modules import CONST
from modules.txt_operations import get_initial_txt_path, clean_txt, create_clean_temp_dir, create_simple_metadata


if __name__ == '__main__':
    create_clean_temp_dir(CONST.TEMP_DIR)
    shutil.copy(get_initial_txt_path(CONST.INPUT_DIR), CONST.ORIGINAL_PATH)
    clean_txt(CONST.ORIGINAL_PATH, CONST.CLEAN_PATH)
    create_simple_metadata(origin=CONST.CLEAN_PATH, destination=CONST.SIMPLE_METADATA_PATH)