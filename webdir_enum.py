#! /usr/bin/env python3

#Import modules
import requests
import sys
import os


print("\
               _         _ _       \n \
__      _____| |__   __| (_)_ __  \n \
\ \ /\ / / _ \ '_ \ / _` | | '__| \n \
 \ V  V /  __/ |_) | (_| | | |    \n \
  \_/\_/ \___|_.__/ \__,_|_|_|    \n\nCreated by N3NU\n")

#Assign variable with wordlist content
try:
    wordlist = input("Enter wordlist (leave blank for default):")
    if len(wordlist) > 0:
        subdirectory_list = open(wordlist, encoding="ISO-8859-1").read()
    else:
        subdirectory_list = open("wordlist.txt", encoding="ISO-8859-1").read()
except KeyboardInterrupt:
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)

#Assign variable with a list of subdirectory_list content
directories = subdirectory_list.splitlines()
#Assign variabe with different file extensions
file_extensions = ["",".html",".txt",".php", \
                   ".xml",".py",".jsp", \
                   ".js",".aspx",".dll", \
                   ".shtml",".rb",".yml"]

def main():
    if len(sys.argv) < 3:
        for extension in file_extensions:
            #Iterate through the words in directories list
            for dir in directories:
                #Assign variable with FQDN and directory
                dir_enum = f"http://{sys.argv[1]}/{dir}{extension}"
                #Assign variable with response from server
                response = requests.get(dir_enum, allow_redirects=False)
                #Check if response code is 404 (Not Found), pass if True
                if response.status_code==404:
                    response.close()
                    pass
                else:
                    print("Valid directory:" ,dir_enum)
                    response.close()

    else:
        for dir in directories:
            dir_enum = f"http://{sys.argv[1]}/{dir}.{sys.argv[2]}"
            response = requests.get(dir_enum)
            if response.status_code==404:
                pass
            else:
                print("Valid directory:" ,dir_enum)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)