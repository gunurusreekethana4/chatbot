import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')


list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trails.ipynb",
    "test.py"

]

#modular approach
#__init__ constructor file
# helper functionality (ingest data,extract info,downloadhuggingface) 
#prompt towrite promt
#setup installing my local package
#research juypter file

for filepath in list_of_files:
    filepath =Path(filepath)#path is used to work in any os system
    filedir, filename = os.path.split(filepath)#tuple split
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory;{filedir} for the file:{filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0):
        with open(filepath, "w")  as f:
         pass
        logging.info(f"creating empty file:{filepath}") 
            
    else:
        logging.info(f"{filename} is already exists")
                
        
       
