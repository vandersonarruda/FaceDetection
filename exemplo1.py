import cv2

classifier = cv2.CascadeClassifier('cascades\haarcascade_frontalface_default.xml')

image = cv2.imread('resources\pessoas\pessoas4.jpg')
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

facesDetected = classifier.detectMultiScale(imageGray, scaleFactor=1.1, minNeighbors=20, minSize=(30,30))
print(len(facesDetected))
print(facesDetected)

for (x, y, l, a) in facesDetected:
    print(x, y, l, a)
    cv2.rectangle(image, (x, y), (x + l, y + a), (255, 0, 255), 2)

cv2.imshow("Faces encontradas", image)
cv2.waitKey()