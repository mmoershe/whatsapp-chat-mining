import os
import sys
import shutil
from re import search


def get_initial_txt_path(input_directory: str) -> str:    
    all_txts: list = [file for file in os.listdir(input_directory) if file.endswith('.txt')]
    if len(all_txts) == 0:
        print('no input txts found.')
        sys.exit()  
        return
    if len(all_txts) == 1:
        return os.path.join(input_directory, all_txts[0])
    while True: 
        print('Several txts were found in the input folder. Please choose one file.')
        for i, txt in enumerate(all_txts):
            print(i+1, txt)
        user_input = input('\t>>> ')
        try: 
            choice: str = all_txts[int(user_input)-1]
        except ValueError: 
            print("\n\tPlease enter a whole number!")
            continue
        except IndexError: 
            print(f"\n\tPlease enter a number from 1 to {len(all_txts)}")
            continue
        else: 
            return os.path.join(input_directory, choice)
        finally: 
            print()


def create_clean_temp_dir(TEMP_DIR: str) -> None:
    if os.path.exists(TEMP_DIR) and len(os.listdir(TEMP_DIR)) > 0:
        all_temp_files: list = [file for file in os.listdir(TEMP_DIR)]
        print(f"Found {len(all_temp_files)} files in the tempo directory {all_temp_files}. They will be deleted.")
        shutil.rmtree(TEMP_DIR)
    if not os.path.exists(TEMP_DIR):
        print(f"Creating temp directory at {TEMP_DIR}.")
        os.makedirs(TEMP_DIR)


def clean_txt(input_dir: str, clean_dir: str) -> None: 
    ERRORS: list = [
        "Nachrichten und Anrufe sind Ende-zu-Ende-verschlüsselt. Niemand außerhalb dieses Chats kann sie lesen oder anhören, nicht einmal WhatsApp. Tippe, um mehr zu erfahren.",
		"hat sich geändert. Tippe, um mehr zu erfahren."
    ]
    
    # retrieve erorrs that are  encased by <>   
    with open(input_dir, 'r', encoding='utf-8') as f:
        special_errors: list = set()
        for i, line in enumerate(f.readlines()):
            line: str = line.strip()
            if '<' in line and '>' in line: 
                special_errors.add(line[line.find('<'):line.find('>')+1:])
    for special_error in list(special_errors):
        ERRORS.append(special_error)
                
    with open(input_dir, 'r', encoding='utf-8') as input_txt, open(clean_dir, 'w', encoding='utf-8') as destination_txt:
        for line in input_txt: 
            if any(error in line for error in ERRORS):
                continue
            destination_txt.write(line)
        




def create_simple_metadata(origin: str, destination: str) -> None:
    # ^(\d{2})\.(\d{2})\.(\d{2})\,\s(\d{2})\:(\d{2})\s\-
    metadata: dict = dict()
    with open(origin, 'r', encoding = 'utf-8') as origin: 
        line_amount: int = 0
        names = set()
        for line in origin.readlines():
            line_amount += 1
            if not search(r"^(\d{2})\.(\d{2})\.(\d{2})\,\s(\d{2})\:(\d{2})\s\-", line):
                continue
            line: str = line[line.find('-')+1::]
            line: str = line[:line.find(':'):].strip()
            names.add(line)
        names = list(names)
    print(f"{names = }")
    print(f"{line_amount = }")