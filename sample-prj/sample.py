import cv2
import darknet

# from skimage import io
from typing import Any, Dict, Text


def overlay_detections(detections: Dict[Text, Any]):
    print(detections['detections'])
    print(detections['image'].shape)
    print(detections['caption'])
    # io.imsave('result.jpg', detections['image'])
    img_bgr = cv2.cvtColor(detections['image'], cv2.COLOR_RGB2BGR)
    for label, conf, bbox in detections['detections']:
        xc, yc, w, h = bbox
        x0 = max(0, int(xc - (w/2)))
        y0 = max(0, int(yc - (h/2)))
        annot = '{}:{:.02f}'.format(label, conf)

        putTextWithBackground(
                img_bgr,
                annot,
                (x0, y0-5),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 0),
                lineType=cv2.LINE_AA)

    cv2.imwrite('result.jpg', img_bgr)


# reference: https://gist.github.com/aplz/fd34707deffb208f367808aade7e5d5c
def putTextWithBackground(
        img,
        text,
        org,
        fontFace,
        fontScale,
        color,
        thickness=None,
        lineType=None):
    rectangle_bgr = (255, 255, 255)
    thn = 1 if thickness is None else thickness
    lit = cv2.LINE_AA if lineType is None else lineType
    (tw, th) = cv2.getTextSize(
            text, fontFace, fontScale=fontScale, thickness=thn)[0]
    tx0 = org[0]
    ty0 = org[1]
    box_coords = (
            (tx0, ty0 + 2), (tx0 + tw - 2, ty0 - th - 2))
    cv2.rectangle(
            img, box_coords[0], box_coords[1], rectangle_bgr, cv2.FILLED)
    cv2.putText(
            img, text, (tx0, ty0), fontFace, fontScale=fontScale,
            color=(0, 0, 0), thickness=1, lineType=lit)


if __name__ == '__main__':
    imagePath = 'misica_azuki/IMG_3549.jpg'
    detections = darknet.performDetect(
            imagePath=imagePath,
            configPath='cfg/yolov3-tiny.cfg',
            weightPath='weights/yolov3-tiny.weights',
            metaPath='cfg/coco.data',
            showImage=True)
    # print(detections)

    # overlay detections on the image
    overlay_detections(detections)
