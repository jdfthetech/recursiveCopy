#!/usr/bin/python

import os
from shutil import copyfile

rootDir = input("Input the starting directory: ")
copyDir = input("Input the export directory: ")
pwd = os.getcwd()

dirCheck = pwd + "/"

if (copyDir == rootDir or rootDir == dirCheck):
	print("You are either attempting to use the same directories, or you are running the program in the starting directory.\nPlease check your directories and try again.")
else:
	for subdir, dirs, files in os.walk(rootDir):
		for f in files:
			copyfile(subdir + "\\" + f, copyDir + f)
			print("copied " + f)				
