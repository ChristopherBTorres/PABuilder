'''
Author: Christopher Torres
Github: https://github.com/ChristopherBTorres
Version 0.0.2 - In-progress

Requires: Python, ng, and npm.

Summary:
This is program sets out to simplify the setup of a new front-end web application by generating the project, and folder structure based on user input.
Currently only supports React and Angular.

***Version 0.0.2 Notes - 
Current build has external script calls commented out for faster testing. Next build will focus on better code readability and organization.
'''
#Imports
import sys, os, subprocess

#Runs external scripts to setup project folder.
def runScript(command, formatedProjectName):
    #Generate Command
    commandline = command + formatedProjectName
    print(commandline)
    
    #Call Command and wait for result.
    #process = subprocess.Popen(commandline, shell=True).wait()
    return 0 #process.returncode

#Introduction
'''
Initial prompts need improvement. Creating recursive function in conjunction with better input verification will improve usability and readability.
'''
print('Welcome to the Python App Builder.\nThis program is designed to streamline web application setup. Currently only Vite React and Angular are supported.')
projectName = input('What is your projects name?\n')
if projectName == "":
    projectName = input('What is your projects name?\n')
formatedProjectName = projectName.translate({ord(c): "_" for c in "!@#$%^&*()[]{};:,./<>?\\|`~-=_+"}).lower()
process = None

while True:
    try:
        frontend = input('Do you want to use React or Angular.\n')
        frontend = frontend.lower()

        if  frontend == 'angular':
            process = runScript('ng new ', formatedProjectName)
        elif  frontend == 'react':
            process = runScript('npm create vite@latest ', formatedProjectName)
        else:
            print("Option invalid.\n")
            continue
        break
    except KeyboardInterrupt:
        break

if process is not None:
    print("Formating Project File...")
    #Call function that creates folder structure based on selected front-end: generateProjectFolderStructure(frontend)
    pageCount = int(input("How many pages will this web application need?\n"))
    i = 0
    while i < pageCount: #End loop when page count is met.
        #Get pageName
        pageName = input('Enter a page name: ')
        formatedPageName = pageName.translate({ord(c): "_" for c in "!@#$%^&*()[]{};:,./<>?\\|`~-=_+"}).lower()
        
        #Generate path
        newpath = os.path.join(formatedProjectName, 'pages', formatedPageName)

        #Try to create folders.
        try:
            os.makedirs(newpath)
            print("Folder %s generated." % pageName)
            #On success increment loop.
            i += 1
        except FileExistsError: #If fail reiterate loop at current i value.
            print("Folder %s already exists." % pageName)
            continue

#Program Concludes
print("Closing PABuilder.")
sys.exit()