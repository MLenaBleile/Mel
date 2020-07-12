
from keras.metrics import AUC
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import cv2
import argparse



parser = argparse.ArgumentParser()
parser.add_argument('--data_path', default='', help='Location of image to predict')

def Melvin_compute(imagefile):
	model = load_model('weights.h5')
	model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
	img = cv2.imread(imagefile)/225
#	print(img.shape)

	img = cv2.resize(img,(160,160))
	#img = np.reshape(img,[150,150,3])
	img = (np.expand_dims(img, axis=0))
	pred = model.predict(img)
#	return(np.argmax(pred, axis=1))
	return(np.round(pred))

def Melvin_predict(filepath):
	outcome = Melvin_compute(filepath)
	sys.stdout = sys.__stdout__
	sys.stderr = sys.__stderr__
	if outcome == [[1]]:
		return("Looks like Topology to me!")
	elif outcome ==[[0]]:
		return("Oooh, a jellyfish!!")
	else:
		return("I don't know what that is!!! Maybe it's too big for me!! Wow!!")

args = parser.parse_args()

out = Melvin_predict(args.data_path)

print(out)

