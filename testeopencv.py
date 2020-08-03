import cv2

print(cv2.__version__)

image = cv2.imread('resources\outros\carro2.jpg')
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.imshow("Cinza", imageGray)
cv2.waitKey()