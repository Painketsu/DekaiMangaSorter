## Made by Painketsu
## Script to organize manga from Dekai Manga Archive (https://nyaa.si/view/1304255) into tidy folders per-volume since it's separated into chapters by default

import os
import sys
import shutil

path = sys.argv[1]

for ch in os.listdir(path):
  if not os.path.isdir(os.path.join(path, ch)):
    continue #not a dir
  if ch[0:1].capitalize() != 'V':
    continue #no volume
  
  chNoGroup = ch.partition(' [')[0]
  group = '[' + ch.partition('[')[2]

  volume,chapter = chNoGroup.split()
  volumePath = path + '/' + volume
  chapterPath = path + '/' + ch

  if not os.path.exists(volumePath):
    os.makedirs(volumePath)

  for page in os.listdir(chapterPath):
    newPageName = volume + ' ' + chapter + ' ' + page
    os.rename(os.path.join(chapterPath, page),
              os.path.join(chapterPath, newPageName))
    shutil.move(os.path.join(chapterPath, newPageName), volumePath)
  os.rmdir(chapterPath)

  #create a file with the TL group name(s)
  groupNameFile = open(path + "/" + "Translation Group(s).txt", 'a')
  groupNameFile.write(chapter + ' by ' + group + '\n')
  groupNameFile.close()
    
