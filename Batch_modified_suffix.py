# batch_file_rename.py
# Created: 2019/12/25

"""
This will batch rename a group of files in a given directory,
once you pass the current and new extensions
"""

__author__ = 'Casuall'

import os
import argparse

def get_parser():
	parser = argparse.ArgumentParser(description='change extension of files in a working directory')
	parser.add_argument('work_dir', metavar='WORK_DIR', help='the directory where to change extension')
	parser.add_argument('old_suffix', metavar='old_suffix', help='old extension')
	parser.add_argument('new_suffix', metavar='new_suffix', help='new extension')
	return parser.parse_args()

def batch_raname(work_dir, old_suffix, new_suffix):
	if old_suffix == new_suffix:
		print('old_suffix eque and new_suffix are the same, nothing would be changed')
		return
	for FileName in os.listdir(work_dir):
		split_file = os.path.splitext(FileName)
		newFileName = split_file[0] + new_suffix
		if split_file[1] != old_suffix:
			continue
		os.rename(os.path.join(work_dir, FileName), os.path.join(work_dir, newFileName))
	print('rename is done!')
	print(os.listdir(work_dir))

def check_Suffix(suffix):
	if suffix[0] != '.':
		suffix = '.' + suffix
	return suffix

def check_dir(work_dir):
	return os.path.exists(work_dir)

def main():
	args = get_parser()
	old_suffix = check_Suffix(args.old_suffix) 
	new_suffix = check_Suffix(args.new_suffix) 
	work_dir = args.work_dir
	if check_dir(work_dir):
		batch_raname(work_dir, old_suffix, new_suffix)
	else:
		print('work_dir is not exist')
	
if __name__ == '__main__':
	main()
