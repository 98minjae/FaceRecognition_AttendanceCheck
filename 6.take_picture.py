import cv2

cam = cv2.VideoCapture(0)
s, img = cam.read()
if s:
    cv2.namedWindow("cam-test", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("cam-test",img)
    cv2.waitKey(0)
    cv2.destroyWindow("cam-test")
    cv2.imwrite("test_model.jpeg",img)



