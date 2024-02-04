import os
import shutil


def get_initial_txt_path(input_directory: str) -> str: 
    if os.path.exists(os.path.join(input_directory, 'original_data.txt')):
        return os.path.join(input_directory, 'original_data.txt')     
    assert os.path.exists(input_directory), f"{input_directory = } doesn't exist."  
    all_txts: list = [txt for txt in os.listdir(input_directory) if txt.endswith('.txt')]
    assert len(all_txts) == 1, "Either too many or none txt files were found in the input directory."
    return os.path.join(input_directory, all_txts[0])


def create_clean_temp_dir(TEMP_DIR: str) -> None:
    if os.path.exists(TEMP_DIR) and len(os.listdir(TEMP_DIR)) > 0:
        all_temp_files: list = [file for file in os.listdir(TEMP_DIR)]
        print(f"Found {len(all_temp_files)} files in the tempo directory {all_temp_files}. They will be deleted.")
        shutil.rmtree(TEMP_DIR)
    if not os.path.exists(TEMP_DIR):
        print(f"Creating temp directory at {TEMP_DIR}.")
        os.makedirs(TEMP_DIR)

    
    
def clean_txt(txt_directory: str, clean_txt_name: str = 'clean_data.txt') -> None: 
    shutil.copy(txt_directory, os.path.join(os.path.dirname(txt_directory), clean_txt_name))
    with open(txt_directory, 'r', encoding='utf-8') as f:
        errors: list = set()
        for i, line in enumerate(f.readlines()):
            line: str = line.strip()
            if '<' in line and '>' in line: 
                errors.add(line[line.find('<'):line.find('>')+1:])