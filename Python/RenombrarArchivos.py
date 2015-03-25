import os
import sys
#import pathlib
from os.path import join, getsize
# Setteamos el directorio raiz a la variable rootDir
# En realidad la variable se puede llamar como sea :)

rootDir = r'/Users/diegopp/Movies/'
for dirName, subdirList, fileList in os.walk(rootDir):
   # print('Directorio encontrado: %s' % dirName)
    
    for fname in fileList:
          if fname[-4:] == ".mkv" or fname[-4:] == ".avi" or fname[-4:] == ".rmvb" or fname[-4:] == ".mp4" or fname[-4:] == ".srt":
          #if fname[-4:] == ".avi" :
                nombre=fname[0:-4:]
                nn=dirName+"/"+os.path.basename(dirName)+fname[-4:]
                #print (pathlib.PurePath(dirName, fname))
                #print (os.path.basename(dirName))
                print('\tRenombrado: %s' %nn) 
                os.rename(join(dirName,fname),nn)
          if fname[-4:] == ".jpg":
                try:
                    ne=dirName+"/"+os.path.basename(dirName)+fname[-4:]
                 #   print (pathlib.PurePath(dirName, fname))
                    #print (os.path.basename(dirName))
                    print('\tRenombrado: %s' %ne) 
                    os.rename(join(dirName,fname),ne)
                except IOError as e:
                    print(e)

