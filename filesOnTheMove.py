"""Python 2.7.13
Georgia Barnes
This program moves files from one folder on my desktop to another folder"""

import shutil
import os

#for every file in the folder
for node in os.listdir('c:/users/georgia/desktop/folderA'):
    #move the file to another folder
    shutil.move(os.path.join('c:/users/georgia/desktop/folderA', node), os.path.join('c:/users/georgia/desktop/folderB',node))
    #print the new location
    print node,os.getcwd()
                
