# opencv-dnn
The model used here is Tenorflow-lite model(ssdlite_mobilenet_v2_coco) from the tensorflow detection model zoo. To use the pre-trained model with opencv, we first need an extra configuration file to import object detection models from TensorFlow. It's based on a text version of the same serialized graph in protocol buffers format (protobuf). The script is included in the confGen folder. The script included here is for the models trained using the SSD architecture.

For more information and how to generate the config file do check the official Opencv implementation: <br />
https://github.com/opencv/opencv/wiki/TensorFlow-Object-Detection-API

Model Link: <br />
https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md

References:<br />
https://www.pyimagesearch.com/2017/09/18/real-time-object-detection-with-deep-learning-and-opencv/ <br />
https://github.com/rdeepc/ExploreOpencvDnn/ <br />

