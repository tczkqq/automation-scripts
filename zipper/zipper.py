import os
from zipfile import ZipFile


size_of_zip = input("Size of zip: ")
try:
    size_of_zip = int(size_of_zip)
except ValueError:
    print("\tSetting default (15)\n")
    size_of_zip = 15 # DEFAULT SIZE OF ZIP


extension = input("Extension: ")
if len(extension) < 1:
    print("\tSetting default (pdf)\n")
    extension = "pdf" # DEFAULT EXTENSION    

print()

files_num = 0
current_directory = os.getcwd()
zip_list = []
chunks = []

for f in os.listdir(current_directory):
    if f.endswith(extension):
        zip_list.append(f)

for item in range(0,len(zip_list), size_of_zip):
    chunks.append(zip_list[item:item+size_of_zip])

for index,chunk_1 in enumerate(chunks):
    with ZipFile(str(index) + '.zip', 'w') as myzip:
        for files in chunk_1:
            myzip.write(files)
            print(f'{files} -> {index}.zip')
            files_num += 1
            

print(f"\nFiles zipped => {files_num}")
print(f"Extension => {extension}")
print(f"Size of zip => {size_of_zip}")
input("\nokkkkkkk")
