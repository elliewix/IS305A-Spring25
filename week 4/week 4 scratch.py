import pathlib

project_files = pathlib.Path().rglob('../*')

for p in project_files:
    # if "/." in str(p):
    #     continue
    print(p.absolute().name)





