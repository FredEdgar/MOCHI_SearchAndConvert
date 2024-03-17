# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 14:06:11 2024

@author: Fred
"""

import list_files
import mochi
import os
import json

def analyze_directories_with_mochi_then_convert(dir_to_search:str, typeresult:str, dir_or_file_result:str):
    """
    Analyze a root directory and all is subsequent directories
    Search all *.mochi files, analyze them, and generate result files

    Parameters
    ----------
    dir_to_search : str
        Root directory where the mochi files are
    typeresult : str
        "JSON" or "CSV"
    dir_or_file_result : str
        can be empty
        In case of typeresult=="JSON" => The directory where the JSON files will be put
            If empty, it will be "dir_to_search/../JSON/"
        In case of typeresult=="CSV" => The filename where the result will be put. Content will be erase
            If empty, it will be "dir_to_search/mochi.csv"

    Returns
    -------
    None.

    """
    
    #get the final directory or CSV file
    root_dir = str(dir_to_search)
    if not root_dir.endswith(os.path.sep):
        root_dir += os.path.sep
    if len(dir_or_file_result)==0:
        dir_json = os.path.normpath(root_dir + "..\\JSon\\")
        file_csv = root_dir + "mochi.csv"
    else:
        dir_json = dir_or_file_result
        file_csv = dir_or_file_result
        
    print(dir_json)
    print(file_csv)

    
    if typeresult=="CSV" and os.path.exists(file_csv):
            os.remove(file_csv)

    list_files_mochi = list_files.list_mochi_files(root_dir)
    
    for file_mochi in list_files_mochi:
        result_analyze = mochi.analyze_mochi_file(file_mochi, typeresult)
        if typeresult=="JSON":
            #Get the final subpart
            new_file_name = file_mochi.replace(root_dir, dir_json).replace('.mochi', '.json')
            new_path_name = os.path.dirname(new_file_name)
            if not os.path.exists(new_path_name):
                os.makedirs(os.path.dirname(new_file_name))
            if os.path.exists(new_file_name):
                os.remove(new_file_name)
            with open(new_file_name, "w") as f:
                json.dump(result_analyze, f)
        elif typeresult=="CSV":
            if os.path.exists(file_csv):
                mode="a"
            else:
                mode="w"
            with open(file_csv, mode) as f:
                f.write(result_analyze + "\n")
            
#######################################
#TEST PART
#######################################
if __name__ == "__main__":
    dir_mochi = "D:\\User10\\Bureau\\Mochi\\Fred\\Mochi"
    analyze_directories_with_mochi_then_convert(dir_mochi, "CSV", "")