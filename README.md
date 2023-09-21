# file_cleaner
this is a tool for cleaning duplicated files on your disk/DIR. 

# how to use
option-1: scan each dir, and then clean
'''
step 1. do scanning, this will scan dir and output its csv
ex. scanner.py -i dir1 -o dir1.csv; scanner.py -i dir2 -o dir2.csv;

step 2. do cleanning, this will remove duplicated files in dir2.  
ex. cleaner.py -b dir1.csv -e dir2.csv
'''

option-2: scan based dir and extra dir, and then clean 
'''
step 1: do scanning, this will output base.csv and extr.csv
ex. scanner_base_extr.py -b dir1 -e dir2

step 2. do cleanning, this will remove duplicated files in dir2.  
ex. cleaner.py -b base.csv -e extr.csv
'''

# help
scanner.py -h
scanner_base_extr.py -h
cleaner.py -h
