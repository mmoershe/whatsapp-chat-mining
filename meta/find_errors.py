import os 
from re import search

# This file is only temporary and only supposed to work for testing purposes. In particular, I'm playing around here and trying to find what kind of errors messages exist in these whatsapp txts. 

CURRENT_DIR: str = os.path.dirname(os.path.abspath(__file__))

txt_path: str = os.path.join(os.path.dirname(CURRENT_DIR), "input", "asdf.txt")

with open(txt_path, "r", encoding = "utf-8") as f:  
	errors: set = set()
	for line in f.readlines():
		if search(r"\<.*\>", line):
			errors.add(line[line.find('<'):line.find('>')+1:])
		if not search(r"^(\d{2})\.(\d{2})\.(\d{2})\,\s(\d{2})\:(\d{2})\s\-", line):
			continue
		line: str = line[line.find('-')+1::]
		line: str = line[:line.find(':'):].strip()
		errors.add(line)
