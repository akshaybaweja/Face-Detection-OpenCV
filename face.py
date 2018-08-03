import cv2

cap = cv2.VideoCapture(0) # Get reference to our Video Capture device (webcam)

cap.set(3, 480) #set width
cap.set(4, 640) #set height

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

while True:

	ret, image = cap.read()

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.1, 5)

	for (x, y, w, h )in faces:
		cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)

	cv2.imshow('frame', image)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break




