import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("웹캠에서 프레임을 읽는데 실패하였습니다.")
        break

    frame[:, :, 1] = 0    
    frame[:, :, 2] = 0  

    cv2.imshow("Original", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()