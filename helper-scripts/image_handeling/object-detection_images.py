import os

import cv2
from detecto import utils
from detecto.core import Model


def draw_bouding_boxes(img, predictions):
    # Add the top prediction of each class to the frame
    for label, box, score in zip(*predictions):
        if score < 0.8:
            continue
        # Create the box around each object detected
        # Parameters: frame, (start_x, start_y), (end_x, end_y), (r, g, b), thickness
        cv2.rectangle(img, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (255, 0, 0), 3)

        # Write the label and score for the boxes
        # Parameters: frame, text, (start_x, start_y), font, font scale, (r, g, b), thickness
        cv2.putText(
            img,
            f"{label}: {round(score.item(), 2)}",
            (int(box[0]), int(box[1]) - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            3,
        )
    return img


model = Model()

images = sorted(os.listdir("Frame/"))  # Helper function to read in images


for i in images:
    img_tmp = utils.read_image(f"Frame/{i}")
    predictions = model.predict(img_tmp)

    img = cv2.imread(f"Frame/{i}")
    # plot the bounding boxes on the image.
    img = draw_bouding_boxes(img, predictions)
    # save the image with opencv
    cv2.imwrite(f"Output/{i}", img)
