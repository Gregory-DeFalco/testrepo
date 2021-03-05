#Greg DeFalco
#This program is designed to take in a text file name and find its path
import os
import sys

if len(sys.argv) > 1:
    target = sys.argv[1]

os.chdir(os.environ.get('USERPROFILE'))

path = os.getcwd()
pathlist = []

for dirpath, subdirs, files in os.walk(path):

        for x in files:

            if x == target:
                pathlist.append(os.path.join(dirpath, x))
                break

if len(pathlist) > 0:

    print(pathlist)

else:

    print('file not found')
