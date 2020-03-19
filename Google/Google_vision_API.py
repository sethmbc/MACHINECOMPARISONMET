import io
import os
import pandas as pd
import re


# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Set Google API authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "METELENAGA-3d5b0d76acea.json"

# ---------------------------------------------------------------------
# Retrieve labels for a batch of images and create a dataframe

# Folder where images are stored
ImageFolder = "images"


# Placeholders to store data
ImageID = []
Description = []


# Instantiates a client
ImageLabels = pd.DataFrame()
client = vision.ImageAnnotatorClient()


# Get labels and scores for every image in folder
	for file in os.listdir(ImageFolder):
 	filename = os.path.basename(file).split('.jpg')[0] # Get image ID
 	image_file = io.open(ImageFolder+file, 'rb') # Open image
 	content = image_file.read() # Read image into memory
 	image = types.Image(content=content)
 	response = client.label_detection(image=image) # Gets response from API for image
 	labels = response.label_annotations # Get labels from response
 	Nlabels = len(labels) # Get the number of labels that were returned

 
 	for i in range(0, Nlabels): # For each label we will store the MID, label, and score
 	ImageID.append(filename) # Keep track Image ID
 	Description.append(labels[i].description) # Store label


# Put Image ID and label into data frame
ImageLabels["imageid"] = ImageID
ImageLabels["desc"] = Description

ImageLabels.groupby(ImageID)

# print(ImageLabels)
Export = ImageLabels.to_json (r'test2.json',orient='records')