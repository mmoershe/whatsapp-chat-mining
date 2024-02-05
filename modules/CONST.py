import os 

# path to the input directory 
INPUT_DIR: str = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'input')

# path to the temporary directory
TEMP_DIR: str = os.path.join(INPUT_DIR, 'temp')

# name of / path to the file that will be created and not have it's content altered
ORIGINAL_NAME: str = 'original_data.txt'
ORIGINAL_PATH: str = os.path.join(TEMP_DIR, ORIGINAL_NAME)

# name of / path to the file that will be created that will have it's content cleaned and altered
CLEAN_NAME: str = 'clean_data.txt'
CLEAN_PATH: str = os.path.join(TEMP_DIR, CLEAN_NAME)

# name of / path to the csv file that will be created. 
CSV_NAME: str = 'chat.csv'
CSV_PATH: str = os.path.join(TEMP_DIR, CSV_NAME)

# name of / path to the json file that includes some basic metadata
SIMPLE_METADATA_NAME: str = 'metadata.json'
SIMPLE_METADATA_PATH: str = os.path.join(TEMP_DIR, SIMPLE_METADATA_NAME)