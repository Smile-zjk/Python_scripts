# -*- coding: UTF-8 -*-
"""
Batch changes to file names
you need  to modify the path 
and regular matching pattern of newFileName when to use it
"""
__author__='Casuall'

import os
import re

def getNewname(path, fileName):
	prefix = u''
	try:
		prefix = prefix + re.search(r'test_(\w).txt', fileName).group(1)
	except :
		return None
	postfix = r'.py'
	return os.path.join(path, prefix + postfix)

def batch_rename(path):
	filenameList = os.listdir(path)
	for fileName in filenameList:
		oldName = os.path.join(path, fileName)
		newName = getNewname(path, fileName)
		if not newName:
				continue
		os.rename(oldName, newName)
		print(oldName,'========>',newName)

def main():
	path = u'G:\py_learning\chdir'
	batch_rename(path)

if __name__ == '__main__':
	main()
	