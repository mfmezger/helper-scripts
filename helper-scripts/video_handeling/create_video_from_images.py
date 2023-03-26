# modified from https://stackoverflow.com/questions/44947505/how-to-make-a-movie-out-of-images-in-python.
import os

import cv2

image_folder = "output/"
output_name = "video.avi"


def main():
    # load all images in the folder that ends with the extension '.jpg'
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]

    # read the first image to determine the size of the video
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(output_name, 0, 3, (width, height))

    # iterate over images and writhe to the video.
    for image in images[:100]:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()


if __name__ == "__main__":
    main()
