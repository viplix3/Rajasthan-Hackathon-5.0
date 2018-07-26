# Repository for Rajasthan Hackathon 5.0

## Todo

- [x] Design the deep leaning model architecture for traffic element detection (YOLOv2 algorithm)
- [X] Train the model for the required task (Currently training)
- [x] Use SSD (Single Shot Detection) model for better results
- [x] Develop a formula for calculating the traffic density using the information extracted by our deep learning model 
- [x] Write an algorithm for managing traffic light efficiently using multiple threads for real time results
- [x] Design a GUI to show out working (Partly done)
- [x] Write scripts for syncing model results, traffic light management algorith and GUI 
- [x] Deploy model onto raspberry-pi

## Instructions for running the code (On linux/unix system)

```
	pip install -r requirements.txt (First time only, for installing all the required dependencies)
	./run.sh
```


## An attempt to reduce traffic congestion using deep learning for object detection and traffic light time management.

### Note : All this is done in real time (approximately 1.2fps for the whole computation)

We are using a raspberry pi (micro-controller) that captures the live feed form the traffic signal posts and feeds it to a deep neural network. The deep neural network is trained for detecting and localizing traffic elements (like cars, trucks, buses, motorcycles, bikes, persons etc.)

Once the live feed is fed to the deep neural network it returns the location of traffic elements, their count and their type (cars, buses, etc.). This information is used for the calculation of traffic density using a formula we developed. Once we have the traffic density, we feed it to an sufficiently decent algorithm which uses multiple threads to handle the task of managing traffic light according to the traffic density present on every lane, in real time without any human intervention.

All this result is displayed using a GUI we developed on out own.

### Screenshots

<img
	src=./1.png
	align="center"
/>

<img
	src=./2.png
	align="center"
/>

### Work Flow Model

<img
	src=./model.JPG
	align="center"
/>
