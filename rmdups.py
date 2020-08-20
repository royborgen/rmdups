#!/usr/bin/python3
import os.path
import sys

#A function that reads the file content 
def readfile (filename): 
    if os.path.isfile(filename):
        with open(filename, 'r' ) as f:
            content = f.readlines() 
        
        newcontent=[]
        for line in content: 
            newcontent.append(line.strip())

        return newcontent
    else: 
        return False

#a function that checks arguments provided, prints helptext and version 
def checkargs(arguments):
    version = "rmdups 1.0"
    helptext = """Usage: rmdups [FILENAME]
Reads a file and removes duplicate lines.
Filename must be provided as argument. 

Optional arguments: 
    -v, --version   Displays version information and exits
        --help      Displays this helptext

Example: 
rmdups test.txt         Reads test.txt and removes duplicate lines
"""

    usage = """Usage: rmdups [FILENAME]
Try 'rmdups --help for more information."""

    #checks arguments provided
    #if no argument is provided 
    if len(arguments) ==1: 
        print(usage)
        return False

    #if more than one argument is provided
    elif len(arguments) >= 2:
        if str.startswith(str(arguments[1]), "--") == True or str.startswith(str(arguments[1]), "-") == True: 
            
            #if argument --help is provided, helptext is printed 
            if str(arguments[1]) =="--help":
                print(helptext)
                return False
            #if argument -v or --version is provided, script name and version number is printed
            elif str(arguments[1]) =="-v" or str(arguments[1]) =="--version": 
                print(version) 
                return False
            #does not proceed as no valid options are provided
            else: 
                print(usage)
                return False
        #proceeds if "filename" is provided
        else: 
            return True
    #returns false if no argument is provided
    else:
        print(usage) 
        return False


def main():
    #fetching command line arguments
    arguments = sys.argv
    
    #Checks the privded arguments and proceeds if function returns true
    if checkargs(arguments): 
        #fetches filename from argument
        filename = arguments[1]
        
        #checks if filename exist
        if os.path.isfile(filename):  
            #reads file content
            content = readfile(filename)
    
            #removing duplicate lines
            content = set(content) 
            if content: 
                for line in content: 
                    print(line) 
            else:
                print("Could not read test.txt") 
                print("Please make sure the file exist!")
        else: 
            print("Error: Could not read file " + filename) 

#calling main function
if __name__ == "__main__": 
    main()

