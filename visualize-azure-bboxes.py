import cv2
import requests

# modify for your settings.
endpoint = ""
prediction_key = ""
img_path = ""


def get_image_azure():
    # create post request with headers
    results = requests.post(
        endpoint,
        headers={"Prediction-Key": prediction_key, "Content-Type": "application/octet-stream"},
        data=open("/Users/marc.mezger/data/EON/up2date/alle/img15.jpg", "rb"),
    )
    results = results.json()

    res = []
    for prediction in results["predictions"]:
        res.append(
            (
                prediction["tagName"],
                prediction["probability"] * 100,
                prediction["boundingBox"]["left"],
                prediction["boundingBox"]["top"],
                prediction["boundingBox"]["width"],
                prediction["boundingBox"]["height"],
            )
        )

    return res


def draw_azure_results(res, img, x, y):
    bboxes = []
    labels = []
    for detect in res:
        label = detect[0]
        box = detect[2:6]
        conf_score = detect[1]
        if conf_score > 60:
            left, top, width, height = box[0], box[1], box[2], box[3]
            topleft_x, topleft_y = x * left, y * top
            bottomright_x, bottomright_y = x * (left + width), y * (top + height)

            # save into array
            bboxes.append([topleft_x, topleft_y, bottomright_x, bottomright_y])
            labels.append(label)

            print(
                "{}: [{}, {}, {}, {}], {}".format(label, round(topleft_x, 3), round(topleft_y, 3), round(bottomright_x, 3), round(bottomright_y, 3), round(conf_score, 3))
            )

            cv2.rectangle(img, (int(topleft_x), int(topleft_y)), (int(bottomright_x), int(bottomright_y)), (0, 255, 0), 2)
            cv2.putText(img, label, (int(topleft_x), int(topleft_y - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, lineType=cv2.LINE_AA)


def main():

    res = get_image_azure()

    img = cv2.imread(img_path)
    y, x, channels = img.shape

    draw_azure_results(res, img, x, y)

    cv2.imshow("Show", img)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
