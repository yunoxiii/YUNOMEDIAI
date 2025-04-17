import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    "src/_init_.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trails.ipynb",
    "test.py"
]

created_directories = set()

for filepath in list_of_files:
    filepath = Path(filepath)
    
    filedir, filename = os.path.split(filepath)

    
    if filedir and filedir not in created_directories:
        os.makedirs(filedir, exist_ok=True)
        created_directories.add(filedir)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    

    if not filedir:
        filedir = '.'
    

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
