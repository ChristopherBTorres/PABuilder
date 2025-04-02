'''
Author: Christopher Torres
Github: https://github.com/ChristopherBTorres
Version 0.0.1 - Inprogress

Requires: Python, ng, and npm.

Summary:
This is program sets out to simplify the setup of a new front-end web application by generating the project, and folder structure based on user input.
Currently only supports React and Angular.
'''
#Imports
import sys, subprocess, re

#Runs external scripts to setup project folder.
def runScript(command, projectName):
    #Generate Command
    projectName = re.sub(r'\s+', '_', projectName)
    commandline = command + projectName
    print(commandline)
    
    #Call Command and wait for result.
    #process = subprocess.Popen(commandline, shell=True).wait()
    return 0 #process.returncode

#Introduction
print('Welcome to the Python App Builder.\nThis program is designed to streamline web application setup. Currently only Vite React and Angular are supported.')
projectName = input('What is your projects name?\n')
process = None

while True:
    try:
        frontend = input('Do you want to use React or Angular.\n')
        frontend = frontend.lower()

        if  frontend == 'angular':
            process = runScript('ng new ', projectName)
        elif  frontend == 'react':
            process = runScript('npm create vite@latest ', projectName)
        else:
            print("Option invalid.\n")
            continue
        break
    except KeyboardInterrupt:
        break

if process is not None:
    print("Formating Project File...")
    #Call function that creates folder structure based on selected front-end: generateProjectFolderStructure(frontend)
    pageCount = input("How many pages will this web application need?\n")
    for i in range(int(pageCount)):
        #Get page name from user
        pageName = input('Enter a page name: ')
        pageName = re.sub(r'\s+', '_', pageName.lower())
        print(pageName)
        #Generate pages based on the number given by the user
        print("Generating folder {i}.")

#Program Concludes
print("Closing PABuilder.")
sys.exit()