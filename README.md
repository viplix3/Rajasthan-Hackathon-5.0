# Repository for Rajasthan Hackathon 5.0

## Todo

<<<<<<< HEAD
- [x] Design the deep leaning model architecture for traffic element detection
- [ ] Train the model for the required task (Currently training)
=======
- [x] Design the deep leaning model architecture for traffic element detection (YOLOv2 algorithm)
- [X] Train the model for the required task (Currently training)
- [x] Use SSD (Single Shot Detection) model for better results
>>>>>>> 9a265f1c6f007613af1bc45915da526c7ba70008
- [x] Develop a formula for calculating the traffic density using the information extracted by our deep learning model 
- [ ] Write an algorithm for managing traffic light efficiently using multiple threads for real time results
- [ ] Design a GUI to show out working (Partly done)
- [ ] Write scripts for syncing model results, traffic light management algorith and GUI 
- [ ] Deploy model onto raspberry-pi
<<<<<<< HEAD
- [ ] Win Hackathon 5.0 (Hopefully)
=======
>>>>>>> 9a265f1c6f007613af1bc45915da526c7ba70008


## An attempt to reduce traffic congestion using deep learning for object detection and traffic light time management.

### Note : All this is done in real time (approximately 1.2fps for the whole computation)

We are using a raspberry pi (micro-controller) that captures the live feed form the traffic signal posts and feeds it to a deep neural network.
The deep neural network is trained for detection and localising traffic elements (like cars, trucks, buses, motorcycles, bikes, persons etc.)

Once the live feed is fed to the deep neural network it returns the location of traffic elemets, their count and their type (cars, buses, etc.).
This information is used for the calcuation of traffic density using a formula we developed.
Once we have the traffic density, we feed it to an sufficiently decent algorithm which uses multiple threads to handle the task of managing traffic light according to the traffic density present on every lane, in real time.

<<<<<<< HEAD
All this result is displayed using a GUI we developed on out own.

### Screenshots
<img
	src=./model.JPG
	allign='center'
/>
=======
All this result is displayed using a GUI we developed on out own.
>>>>>>> 9a265f1c6f007613af1bc45915da526c7ba70008
