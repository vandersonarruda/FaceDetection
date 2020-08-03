import cv2

#classifier = cv2.CascadeClassifier('cascades\haarcascade_frontalcatface.xml')
#classifier = cv2.CascadeClassifier('cascades\relogios.xml')
classifier = cv2.CascadeClassifier('cascades\cars.xml')

image = cv2.imread('resources\outros\carro3.jpg')
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

detected = classifier.detectMultiScale(imageGray, scaleFactor=1.01)
print(detected)

for (x, y, l, a) in detected:
    cor = (255, 0, 0)

    if (l > 50 or a > 50):
        cor = (0, 0, 255)

    image = cv2.rectangle(image, (x, y), (x + l, y + a), cor, 2)

cv2.imshow("Encontrado", image)
cv2.waitKey()