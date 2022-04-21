import os

dirs = []

for e in os.listdir():
    if os.path.isdir(e):
        dirs.append(e)

for dir in dirs:
    for file in os.listdir(dir):
        print(f'\n.\{dir}\{file} -> .')
        os.system(f'move ".\{dir}\{file}"')


input('okkkkkkkkkkkkkkkkkk')