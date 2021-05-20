# DekaiMangaSorter
Script to organize manga from Dekai Manga Archive (https://nyaa.si/view/1304255) into tidy folders per-volume since it's separated into chapters by default

You'll need Python 3+

Usage:
Simply drop the folder you want organized on top of the .py, otherwise navigate to the .py on console and add the path to the folder you want organized as first argument, remember to surround the full path with " if it contains spaces.

It will:
  -Create a folder for each volume in the same directory
  -Rename all pages according to their volume and chapter and move them to their respective volume, they will keep their proper reading order (if sorted alphabetically)
  -Delete the now empty chapter folders
