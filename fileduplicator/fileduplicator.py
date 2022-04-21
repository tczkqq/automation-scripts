#filename, stage, name

import os
import shutil
from colorama import init, Fore, Style


EXT = ".pdf"
FILENAME = "lokale.csv"
DIR = FILENAME[:-4] + '/'


if not os.path.exists(DIR):
    os.mkdir(DIR)

init()

if not FILENAME in os.listdir():
    print(Fore.RED + f"Fail: {FILENAME} not found in current directory")
    input()
    quit()

for line in open(FILENAME):
    csv_row = line.split(",")
    if not os.path.exists(DIR+str(csv_row[1])):
        os.mkdir(DIR + str(csv_row[1]))
    
    try:
        shutil.copy(
            csv_row[0] + EXT, 
            DIR  + str(csv_row[1]) +
             "/" + csv_row[2].replace("\n", "") + EXT
        )
        print(Fore.GREEN + str(csv_row[1]) + "/" +
            csv_row[2].replace("\n", "") + EXT + " -> " + csv_row[0])
    except FileNotFoundError:
        print(Fore.RED + str(csv_row[1]) + "/" +
              csv_row[2].replace("\n", "") + EXT + " -> " + csv_row[0] + "\tFail: FileNotFoundError")
    
print(Style.RESET_ALL)
input()
