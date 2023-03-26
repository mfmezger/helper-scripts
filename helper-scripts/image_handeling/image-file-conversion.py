import os

# this is used to enabled the load of truncated images.
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

data_path = "/path/to/data/"

target_path = "/path/to/target/"


def main():
    # iterate over data directory.
    # add error handeling
    try:
        for file in sorted(os.listdir(data_path)):

            # ignore mac files.
            if file == ".DS_Store":
                continue

            # open image
            img = Image.open(data_path + file)

            # remove the alpha from the images if available.
            img = img.convert("RGB")

            # save image
            img.save(target_path + file.split(".")[0] + ".jpg")  # choose .png or .jpg

    except Exception as e:
        print(f"Error in File: {file}")
        print("Error: ", e)


if __name__ == "__main__":
    main()
