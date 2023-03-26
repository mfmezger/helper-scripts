import os
from pathlib import Path
from zipfile import ZipFile


def initialize_runtime_env():
    """

    :return: _description_
    :rtype: _type_
    """

    # User specific RUN_ID for aws session
    run_id = os.getenv("RUN_ID", default="")
    if run_id == "":
        # if docker is executed locally, there will be no run_id, and therefore we don't need a path on the cloud for the params
        path_prefix = os.getcwd()
        print("RUN_ID is EMPTY")
    else:
        # if docker is executed in the cloud, we define a path with a folder named 'data' in between
        path_prefix = os.path.join("/data", run_id)
        print("RUN_ID is NOT EMPTY")

    return path_prefix


def read_in_memory_zip(path_prefix):
    # search the only zip file in the directory
    for file in os.listdir(path_prefix):
        if file.endswith(".zip"):
            path_to_zip = os.path.join(path_prefix, file)
    del file

    # save the zip file name to txt file.
    zip_name = path_to_zip.split("/")[-1].split(".")[0]
    with open(path_prefix + "/input/origin_name.txt", "w") as text_file:
        text_file.write(zip_name)

    # generate the target path
    target_path = os.path.join(path_prefix, "input")
    Path(target_path).mkdir(parents=True, exist_ok=True)
    # unpack the zip file, but in memory
    input_zip = ZipFile(path_to_zip)
    for name in input_zip.namelist():
        # check if the file is a directory
        if name.endswith("/"):
            continue
        else:
            f = input_zip.read(name)
            # save the in memory file to the target path
            with open(os.path.join(target_path, name.split("/")[-1]), "wb") as file:
                file.write(f)


def main():
    # initialize the runtime environment
    path_prefix = initialize_runtime_env()

    # read in the in memory zip file
    read_in_memory_zip(path_prefix)


if __name__ == "__main__":
    main()
