# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 08:40:30 2024

@author: Fred
"""

import os

def list_files_with_extension(directory:str, extension:str):
    list_of_files = []
    for root_folder, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                full_path = os.path.join(root_folder, file)
                list_of_files.append(full_path)
    return list_of_files
    

def list_mochi_files(directory):
    return list_files_with_extension(directory, ".mochi")

#######################################
#TEST PART
#######################################
if __name__ == "__main__":
    # Starting directory to begin the search
    start_directory = "D:\\User10\\Bureau\\Mochi\\Fred\\Mochi"
    
    # Call the function to list *.mochi files in the starting directory
    mochi_files = list_mochi_files(start_directory)
    
    # Display the results
    for file in mochi_files:
        print(file)