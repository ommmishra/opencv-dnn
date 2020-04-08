import cv2


model = cv2.dnn.readNetFromTensorflow('model/frozen_inference_graph.pb',
                                      'model/graph.pbtxt')

vs = cv2.VideoCapture(0)

while True:
	_, image = vs.read()
	image_height, image_width, _ = image.shape
	model.setInput(cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True))
	output = model.forward()

	for detection in output[0, 0, :, :]:
		confidence = detection[2]
		#Changed to detect only persons
		class_person = detection[1]
		if confidence > .5 and class_person == 1.0:
			box_x = detection[3] * image_width
			box_y = detection[4] * image_height
			box_width = detection[5] * image_width
			box_height = detection[6] * image_height
			cv2.rectangle(image, (int(box_x), int(box_y)), (int(box_width), int(box_height)), (23, 230, 210), thickness=2)
	cv2.imshow('image', image)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break

vs.release()
cv2.destroyAllWindows()
