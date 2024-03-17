# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 17:46:06 2024

@author: Fred

channelFamilies doit être l'entête
fixtureType doit être le contenu
"""

import json
import pathlib
import os

TR_JSON = "JSON"
TR_CSV = "CSV"

def analyze_mochi_file(filename:str, typeresult:str):
    """
    Analyze the content of a mochi file and return the wanted data
    filename : The complete filename to analyze
    typefile : The type of the result "JSON" or "CSV"
    """
    result = ""
    path_file = pathlib.Path(filename)
    #Get the Brand name
    brand_name = path_file.parent.parent.name
    #Get the machine name
    machine_name = path_file.parent.name
    #Get the modeName
    mode_name = os.path.basename(filename)
    mode_name = mode_name.replace(".mochi", "")
    mode_name = mode_name.removeprefix(machine_name)
    mode_name = mode_name.replace("-", "")
    mode_name = mode_name.lstrip().rstrip()

    #Prepare the result
    channels_found = dict()
    channels_index_param = list()
    if typeresult==TR_JSON:
        result = {
            "brand": brand_name,
            "name": machine_name,
            "modeName": mode_name,
            "channels": {}
            }
    elif typeresult==TR_CSV:
        result = brand_name + ";" + machine_name + ";" + mode_name
        
    #Open the file
    content_file = open(filename, 'r')
    #with open(filename, 'r') as content_file:
    #Get the JSON data
    parsed_data = json.load(content_file)
    #Close the file, not useable anyway
    content_file.close()
    
    #Prepare the 'fixtureType' data in a list
    list_param = list()
    for fixture_type_item in parsed_data['fixtureType'][0]['containers']['channels']['items']:
        parameters = fixture_type_item['parameters']
        for parameter in parameters:
            list_param.append(str(parameter['value']).lower())
    
    
    #Get 'channelFamilies' data
    for channel_family in parsed_data['channelFamilies']:
        nice_name_family = channel_family['niceName']
        #Get 'items'
        for family_item in channel_family['containers']['channelTypes']['items']:
            nice_name = family_item['niceName']
            #Check if nice_name is in "fixtureType"
            str_to_search = "/" + nice_name_family + "/channelTypes/" + nice_name.replace(" ", "")
            index_param = list_param.index(str_to_search.lower())
            if index_param>=0:
                channels_found.update({index_param: nice_name})
                channels_index_param.append(index_param)
                    
    #Sort the index
    channels_index_param.sort()
    
    #Add channels in result
    if typeresult==TR_JSON:
        index_param=1
        all_channels = {}
        for index in channels_index_param:
            all_channels.update({"" + str(index_param) + "" : channels_found[index]})
            index_param = index_param+1
        result.update({"channels": all_channels})
    elif typeresult==TR_CSV:
        #Add the number of channels
        result = result + ";" + str(len(channels_index_param))
        for index in channels_index_param:
            result = result + ";" + channels_found[index]
        
    return result
            

#######################################
#TEST PART
#######################################
if __name__ == "__main__":
    file_test = "D:\\User10\\Bureau\\Mochi\\Fred\\Mochi\\Martin\\Alien 02\\Alien 02 - 7ch.mochi"
    
    print(analyze_mochi_file(file_test, "CSV"))
