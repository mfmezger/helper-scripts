import os

import imageio
import imgaug as ia
from imgaug import augmenters as iaa

# this is used to enabled the load of truncated images.
from PIL import Image, ImageFile

ia.seed(4)


ImageFile.LOAD_TRUNCATED_IMAGES = True

data_path = "/path/to/data/"
data_path = "data/"

target_path = "/path/to/target/"
target_path = "output/"


def main():
    # iterate over data directory.
    # add error handeling

    flip = False
    blur = False
    rotation = False
    contrast = False
    combination = True

    try:
        for file in sorted(os.listdir(data_path)):

            # ignore mac files.
            if file == ".DS_Store":
                continue

            # load the image.
            img = imageio.imread(data_path + file)

            if rotation:
                # read image with imageio because it is rotated -90 degrees with PIL and numpy.

                # rotation augmentation.
                image_rotation_angles = [-10, -5, 5, 10]
                for i in image_rotation_angles:
                    rotate = iaa.Affine(rotate=(i))
                    image_aug = rotate(image=img)

                    # convert the image to PIL and save it.
                    image_aug = Image.fromarray(image_aug)
                    # save rotated image
                    image_aug.save(target_path + file.split(".")[0] + "_" + "rot" + str(i) + ".jpg")  # choose .png or .jpg

            if blur:
                # blurring.
                image_blurring_simgas = [4.0, 5.0]

                for i in image_blurring_simgas:
                    blur = iaa.GaussianBlur(sigma=(i))
                    image_aug = blur(image=img)

                    # convert the image to PIL and save it.
                    image_aug = Image.fromarray(image_aug)
                    # save blurred image
                    image_aug.save(target_path + file.split(".")[0] + "_" + "blur" + str(i) + ".jpg")

            if contrast:
                # contrast.
                image_contrast_values = [1.0, 1.5]

                for i in image_contrast_values:
                    contrast = iaa.ContrastNormalization(i)
                    image_aug = contrast(image=img)

                    # convert the image to PIL and save it.
                    image_aug = Image.fromarray(image_aug)
                    # save contrast image
                    image_aug.save(target_path + file.split(".")[0] + "_" + "contrast" + str(i) + ".jpg")

            if flip:
                # horizontal flip.
                flip = iaa.Fliplr(1)

                image_aug = flip(image=img)
                # convert the image to PIL and save it.
                image_aug = Image.fromarray(image_aug)
                image_aug.save(target_path + file.split(".")[0] + "_" + "flip" + ".jpg")

            if combination:
                # combine flip, blur and rotate
                seq = iaa.Sequential(
                    [
                        iaa.Fliplr(1),
                        iaa.ContrastNormalization(2),
                        # iaa.Affine(rotate=(-10, 10)),
                        # iaa.AdditiveGaussianNoise(scale=(10, 30)),
                        # iaa.Crop(percent=(0, 0.2))
                    ]
                )

                images = [img] * 1
                images_aug = seq(images=images)

                for x, i in enumerate(images_aug):
                    # convert the image to PIL and save it.
                    image_aug = Image.fromarray(i)
                    image_aug.save(target_path + file.split(".")[0] + "_" + "combine" + str(x) + ".jpg")
    except Exception as e:
        print(f"Error in File: {file}")
        print("Error: ", e)


if __name__ == "__main__":
    main()
