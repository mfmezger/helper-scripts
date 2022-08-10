import zipfile
from pathlib import Path
import os

def main():

    # unpack all of the zips in to a folder that is named after the zip file
    try:
        path_2_file = "test.zip"

        folder_name = path_2_file.split(".")[0]
        Path("tmp").mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(path_2_file, 'r') as zip_ref:
            zip_ref.extractall("tmp")
    except Exception as e:
        raise ValueError("Error: ", e)

    # iterate over all directories in the folder and move all files in the directory on the same level

    # implement a os.walk function to iterate over all directories in the folder and move all files in the directory on the same level
    try:
        Path(folder_name).mkdir(parents=True, exist_ok=True)
        for root, dirs, files in os.walk("tmp"):

            for file in files:
                origin = os.path.join(root, file)
                target = os.path.join(os.path.join(os.getcwd(), folder_name), file)
                Path(origin).rename(target)
    
        # delete the folder that was created
        # os.rmdir("tmp")


    except Exception as e:
        raise 




if __name__ == '__main__':
    main()

