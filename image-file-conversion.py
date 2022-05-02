import os
from PIL import Image

# this is used to enabled the load of truncated images.
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

data_path = "/path/to/data/"
target_path = "/path/to/target/"


def main():
    # iterate over data directory.
    for file in sorted(os.listdir(data_path)):

        # add error handeling
        try:
            # open image
            img = Image.open(data_path + file)
            # save image
            img.save(target_path + file.split(".")[0] + ".png")
        except Exception as e:
            print("Error in File: " + file)

if __name__ == '__main__':
    main()
