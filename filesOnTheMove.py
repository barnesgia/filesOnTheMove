"""Python 2.7.13
Georgia Barnes
This program moves files from one folder on my desktop to another folder"""

import shutil
import os

sourceFolder = 'c:/users/georgia/desktop/folderA'
destFolder = 'c:/users/georgia/desktop/folderB'


#for every file in the folder
for node in os.listdir(sourceFolder):
    #move the file to another folder
    shutil.move(os.path.join(sourceFolder, node), os.path.join(destFolder,node))
    #print the new location
    print node,os.getcwd()

