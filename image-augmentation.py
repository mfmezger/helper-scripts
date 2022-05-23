import os

import imageio
import imgaug as ia
import numpy as np
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

    

    try:
        for file in sorted(os.listdir(data_path)):

            # ignore mac files.
            if file == ".DS_Store":
                continue
            
            # read image with imageio because it is rotated -90 degrees with PIL and numpy.
            img = imageio.imread(data_path + file)

            # rotation augmentation.
            image_rotation_angles = [-15, - 5, 5, 15]
            for i in image_rotation_angles:
                rotate = iaa.Affine(rotate=(i))
                image_aug = rotate(image=img)

                # convert the image to PIL and save it.
                image_aug = Image.fromarray(image_aug)
                # save rotated image
                image_aug.save(target_path + file.split(".")[0] + "_" + "rot" + str(i) + ".jpg")  # choose .png or .jpg

            # blurring.
            aug = iaa.GaussianBlur(sigma=(0.0, 3.0))

            image_blurring_simgas = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]

            for i in image_blurring_simgas:
                blur = iaa.GaussianBlur(sigma=(i))
                image_aug = blur(image=img)

                # convert the image to PIL and save it.
                image_aug = Image.fromarray(image_aug)
                # save blurred image
                image_aug.save(target_path + file.split(".")[0] + "_" + "blur" + str(i) + ".jpg")

            # contrast.

            image_contrast_values = [1.0, 1.5]
            
            for i in image_contrast_values:
                contrast = iaa.ContrastNormalization((i))
                image_aug = contrast(image=img)

                # convert the image to PIL and save it.
                image_aug = Image.fromarray(image_aug)
                # save contrast image
                image_aug.save(target_path + file.split(".")[0] + "_" + "contrast" + str(i) + ".jpg")
            

            # horizontal flip.
            flip = iaa.Fliplr(1)

            image_aug = flip(image=img)
            # convert the image to PIL and save it.
            image_aug = Image.fromarray(image_aug)
            image_aug.save(target_path + file.split(".")[0] + "_" + "flip" + ".jpg")  

            # combine flip, blur and rotate
            seq = iaa.Sequential([
                iaa.Affine(rotate=(-15, 15)),
                iaa.AdditiveGaussianNoise(scale=(10, 30)),
                iaa.Crop(percent=(0, 0.2))
            ])

            images = [img] * 5
            images_aug = seq(images=images)

            x = 0
            for i in images_aug:
                # convert the image to PIL and save it.
                image_aug = Image.fromarray(i)
                image_aug.save(target_path + file.split(".")[0] + "_" + "combine"+ str(x) + ".jpg")
                x += 1

            
            
        
    except Exception as e:
        print("Error in File: " + file)
        print("Error: ", e)


if __name__ == '__main__':
    main()
