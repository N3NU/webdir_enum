#! /usr/bin/env python3

#Import modules
import requests
import sys

#Assign variable with wordlist content
subdirectory_list = open("wordlist.txt").read()
#Assign variable with a list of subdirectory_list content
directories = subdirectory_list.splitlines()
#Assign variabe with different file extensions
file_extensions = ["html","txt","php", \
                   "xml","py","jsp", \
                   "js","aspx","dll", \
                   "shtml","rb","yml"]

for extension in file_extensions:
    #Iterate through the words in directories list
    for dir in directories:
        #Assign variable with FQDN and directory
        dir_enum = f"http://{sys.argv[1]}/{dir}.{extension}"
        #Assign variable with response from server
        response = requests.get(dir_enum)
        #Check if response code is 404 (Not Found), pass if True
        if response.status_code==404:
            pass
        else:
            print("Valid directory:" ,dir_enum)