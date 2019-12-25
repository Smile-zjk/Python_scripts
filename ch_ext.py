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
    parser.add_argument('old_ext', metavar='OLD_EXT', help='old extension')
    parser.add_argument('new_ext', metavar='NEW_EXT', help='new extension')
    return parser.parse_args()

def batch_raname(work_dir, old_ext, new_ext):
    if not os.path.exists(work_dir):
        print('work_dir is not exist')
        return
    # Check whether old_ext and new_extare the same
    if old_ext == new_ext:
        print('old_ext eque and new_ext are the same, nothing would be changed')
        return
    for filename in os.listdir(work_dir):
        split_file = os.path.splitext(filename)
        newfile = split_file[0] + new_ext
        # only old_ext will be rename
        if split_file[1] != old_ext:
            continue
        os.rename(os.path.join(work_dir, filename), os.path.join(work_dir, newfile))
    print('rename is done!')
    print(os.listdir(work_dir))

def main():
    # parse the args
    args = get_parser()
    old_ext = args.old_ext
    new_ext = args.new_ext
    work_dir = args.work_dir
    if old_ext[0] != '.':
        old_ext = '.' + old_ext 
    if new_ext[0] != '.':
        new_ext = '.' + new_ext
    batch_raname(work_dir, old_ext, new_ext)
    
if __name__ == '__main__':
    main()
    
    