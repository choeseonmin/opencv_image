import cv2

image = cv2.imread("C:\\Users\\user\\Pictures\\Screenshots\\hamo.png", cv2.IMREAD_COLOR)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("color", image)
cv2.imshow("Gray", gray_image)
cv2.waitKey()
cv2.destoryAllwindows()