import os
import zipfile
from zipfile import ZipFile
from pathlib import Path



def write_zip_file(target, path_to_zip):
    input_zip=ZipFile(path_to_zip)
    for name in input_zip.namelist():
        # check if the file is a directory
        if name.endswith("/"):
            continue
        else:
            if name.endswith(".pdf"):
                f = input_zip.read(name)
                #save the in memory file to the target path
                zip_name = path_to_zip.split("/")[-1].split(".")[0]
                new_file_name = zip_name + "_" + name.split("/")[-1]
                new_file_name.replace("\\", "")
                new_file_name.replace("/", "")
                with open(os.path.join(target, new_file_name), "wb") as file:
                    file.write(f)

def main():
    target_path = "target"
    Path(target_path).mkdir(parents=True, exist_ok=True)
    for root, dirs, files in os.walk("Angebotsunterlagen"):

        for file in files:
            if file.endswith(".zip"):
                path_to_zip = os.path.join(root, file)
                write_zip_file(target_path, path_to_zip)


                

if __name__ == '__main__':
    main()