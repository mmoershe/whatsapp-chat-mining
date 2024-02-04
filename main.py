import os, sys
import shutil
import csv 

from modules import CONST
from modules.txt_operations import get_initial_txt_path, clean_txt, create_clean_temp_dir


if __name__ == '__main__':
    create_clean_temp_dir(CONST.TEMP_DIR)