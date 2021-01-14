from pathlib import Path

def unify_ext_with_pathlib(path, old_ext_pattern='*.csv', new_ext='.py'):
    for fpath in Path(path).glob(old_ext_pattern):
        fpath.rename(fpath.with_suffix(new_ext))


if __name__ == '__main__':
    path = './py_scripts' 
    unify_ext_with_pathlib(path)