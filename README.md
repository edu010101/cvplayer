##Description

Welcome to **OpenCVPlayer**, a powerful and easy to use tool for visualizing computer vision models and their inferences. With OpenCVPlayer, you can easily view and analyze the output of your models, no mather wich library or framework you are using, saving you from long codes for a simple inference visualization.

##Features
- [x] Video inference visualization.
- [ ] Images inference visualization.
- [x] Frame level control.
- [x] Easy to use.
- [ ] Portable for PyQt6 aplications.



##Requirements

- Anaconda
- opencv-python
- PyQt6
- Python3

##Instalation

###pip

```bash
# inside your env
pip install PyQt6==6.4.2 PyQt6-Qt6==6.4.2 PyQt6-sip==13.4.1
pip install opencv-python
```

##Usage

###Video Player

```python
from opencvplayer import VideoPlayer

#create a class with any name
class ExampleName():
    def __init___(self): #it can have many args as you need
        #initialize your model
    
    #your class NEED to have this method with this exactly name.
    def custom_method(self, numpy_image):
      	#this method receives an np.array representing your image or frame
      	#modify and inference your array as you want
	
    	return numpy_image  #then return your modified np.array

VideoPlayer(ExampleName()) #load your class as an argument to the player
```
###Image Player

```python
from opencvplayer import ImagePlayer

#create a class with any name
class ExampleClass():
    def __init___(self): #it can have many args as you need
        #initialize your model
    
    #your class NEED to have this method with this exactly name.
    def custom_method(self, numpy_image):
      	#this method receives an np.array representing your image or frame
      	#modify and inference your array as you want
	
    	return numpy_image  #then return your modified np.array

imageclassifier = ExampleClass()
ImagePlayer(imageclassifier) #load your class as an argument to the player
```

###Yolov8 demo

###mmdetection demo