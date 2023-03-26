import os
import shutil
from pathlib import Path

data_path = "/path/to/data/"

target_path = "/path/to/target/"


def main():
    # iterate over data directory.
    x = 0
    p = Path(data_path)
    t = Path(target_path)
    try:
        for file in sorted(os.listdir(data_path)):

            # add error handeling
            source = os.path.join(data_path, file)
            target = os.path.join(target_path, "non" + str(x) + "." + file.split(".")[1])
            shutil.copy(source, target)
            x += 1

    except Exception as e:
        print("Error in File: " + file)
        print("Error: ", e)


if __name__ == "__main__":
    main()
