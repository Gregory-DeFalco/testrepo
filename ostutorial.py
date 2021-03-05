import os

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('Current Path: ', dirpath)
    print('Directories', dirnames)
    print('filenames', filenames)
    print()
