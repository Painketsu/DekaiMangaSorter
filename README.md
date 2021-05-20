# DekaiMangaSorter
Script to organize manga from Dekai Manga Archive (https://nyaa.si/view/1304255) into tidy folders per-volume since it's separated into chapters by default

You'll need Python 3+

_Usage:_

Simply drop the folder you want organized on top of the .py, otherwise navigate to the .py on console and add the path to the folder you want organized as first argument, remember to surround the full path with " if it contains spaces.

![2021-05-20_21-01-26](https://user-images.githubusercontent.com/11485235/119034495-aba38300-b9ae-11eb-81d2-95198a816b4d.gif)

_It will:_

  -Create a folder for each volume in the same directory
  
  -Rename all pages according to their volume and chapter and move them to their respective volume, they will keep their proper reading order (if sorted alphabetically)
  
  -Delete the now empty chapter folders

_It wont:_

  -Create a folder or sort chapters without a volume, this is not very common but I've seen it in some ongoing manga
