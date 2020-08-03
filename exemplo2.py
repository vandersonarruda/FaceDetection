import cv2

classifierFace = cv2.CascadeClassifier('cascades\haarcascade_frontalface_default.xml')
classifierEye = cv2.CascadeClassifier('cascades\haarcascade_eye.xml')

image = cv2.imread('resources\pessoas\pessoas4.jpg')
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

facesDetected = classifierFace.detectMultiScale(imageGray)

for (x, y, l, a) in facesDetected:
    image = cv2.rectangle(image, (x, y), (x + l, y + a), (0, 0, 255), 2)
    area = image[y:y + a, x:x + l]
    areaGrayEye = cv2.cvtColor(area, cv2.COLOR_BGR2GRAY)
    eyesDetected = classifierEye.detectMultiScale(areaGrayEye, scaleFactor=1.1, minNeighbors=10)
    print(eyesDetected)
    for (ox, oy, ol, oa) in eyesDetected:
        cv2.rectangle(area, (ox, oy), (ox + ol, oy + oa), (255, 0, 255), 2)

cv2.imshow("Faces e olhos detectados", image)
cv2.waitKey()