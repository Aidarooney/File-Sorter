import os 
import shutil 
from time import sleep


# Enter path for the folder that will be sorted
# Eg: C:/Users/abcd/Downloads
path = ''


# makes a list of all unsorted files in directory 
list_ = os.listdir(path) 

random = 0


while random == 0:

    # Pauses script for 5 Minutes to allow for any downloads to finish as it will crash if it trys to move a file while it is downloading
    sleep(300)

    
    list_ = os.listdir(path) 

    # Goes through each file
    for file_ in list_: 
        name, ext = os.path.splitext(file_) 
        
        # Stores the file extension
        ext = ext[1:] 
        
        if ext == '': 
            continue
        
        # Moves file to directory corisponding with file extension
        if os.path.exists(path+'/'+ext): 
            shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_) 
            print('Moving File', file_, 'to', ext, '...')
            sleep(0.5)
        
        # Makes new directory if one is not found
        else:
            os.makedirs(path+'/'+ext) 
            shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
            print('Moving File', file_, 'to new folder', ext, '...')
            sleep(0.5)
