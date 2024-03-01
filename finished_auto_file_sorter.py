#!/usr/bin/env python
# coding: utf-8

#importing libraries
import os,shutil,sys
from time import time


def main(path):
    start = time()

    # List files in the directory
    file_list = os.listdir(path)

    for file in file_list:
        if os.path.isfile(os.path.join(path, file)):  # Check if it's a file
            file_name, file_ext = os.path.splitext(file) #split the file by name and extention
            file_ext = file_ext[1:]  # Remove the dot from the extension
        
            file_dir = os.path.join(path, file_ext + " files") # create path to the resp. folder with the name
            dest_file_path = os.path.join(file_dir, file) #create the file path
            head,tail=os.path.split(file_dir)
            
        
            # Create directory if it doesn't exist and move
            if not os.path.exists(file_dir):
                print(f"{file_ext} folder doesn't exist. creating folder...")
                os.makedirs(file_dir)
                print(f'{tail} folder created')
                print(f'moving {file} to {tail}...')
                shutil.move(os.path.join(path, file), dest_file_path)
                print(f'{file} moved!')
            # Move the file if it's not already in the correct directory
            elif os.path.exists(file_dir) and not os.path.exists(dest_file_path):
                print(f'moving {file} to {tail}...')
                shutil.move(os.path.join(path, file), dest_file_path)
                print(f'{file} moved!')
            else:
                print('Nothing to move')
                
    end = time()
    total_time = end - start
    print(f'took %.4f seconds to complete' % (total_time))


if __name__ == '__main__':
    while True:
        try:
            path=str((input('enter a path:')))
            if not os.path.exists(path): #input fn doesnt catch the filenorfound error, we have to manually raise it.
                raise FileNotFoundError
            break
        except FileNotFoundError as e: #catch wrong inputs
            print(e,'please enter a valid file path')
            continue
        except KeyboardInterrupt: #if the user exits using the keyboard
            print('You exited this program')
            sys.exit()
    main(path)

