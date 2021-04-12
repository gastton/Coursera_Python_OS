"""The file_date function creates a new file in the current working directory, checks the date that the file was modified, 
and returns just the date portion of the timestamp in the format of yyyy-mm-dd. Fill in the gaps to create a file called "newfile.txt" 
and check the date that it was modified."""

import os
from datetime import datetime

def file_date(filename):
    # Create the file in the current directory
    with open (os.getcwd() + "/" + filename, 'w') as file:
        pass

    newfileTS = os.path.getmtime(os.getcwd() + "/" + filename)
    dt_object = datetime.fromtimestamp(newfileTS).strftime("%Y-%m-%d")
    
    return (dt_object)

print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd