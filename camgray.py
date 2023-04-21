import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("웹캠에서 프레임을 읽는데 실패하였습니다.")
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    flipped_frame = cv2.flip(gray_frame, 1)

   

    cv2.imshow("Flipped", flipped_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
