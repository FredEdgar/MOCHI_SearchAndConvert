# MOCHI_SearchAndConvert
Search .mochi files and convert them to JSON files or a unique CSV file

By default the output directory or file is :
* In case of typeresult=="JSON" => "dir_to_search/../JSON/"
* In case of typeresult=="CSV" => "dir_to_search/mochi.csv"
 
To generate Executables Files

In command line tool :
pip install cx_Freeze
python setup.py build
The generated files are in the build directory

