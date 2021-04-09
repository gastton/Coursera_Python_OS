
import os
def new_directory(directory, filename):
    # Before creating a new directory, check to see if it already exists
    curPath = os.getcwd()
    if os.path.isdir(curPath + "/" + directory) == False:
        os.mkdir(curPath + "/" + directory)
        
    # Create the new file inside of the new directory
    os.chdir(curPath + "/" + directory)
    with open (filename, 'w') as file:
        pass

    # Return the list of files in the new directory
    return os.listdir(curPath + "/" + directory)

print(new_directory("PythonPrograms", "script.py"))