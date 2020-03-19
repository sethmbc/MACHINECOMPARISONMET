import boto3
import os
import io
import pandas as pd


os.environ['AWS_DEFAULT_REGION'] = 'us-east-2'
os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAJL263EWRC5YGNCQA'
os.environ['AWS_SECRET_ACCESS_KEY'] = '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'


ImageFolder = 'images/dir_001/'

ImageID = []

Description = []


ImageLabels = pd.DataFrame()
client=boto3.client('rekognition')
 
for file in os.listdir(ImageFolder):
    filename = os.path.basename(file).split('.jpg')[0] # Get image ID
    image_file = io.open(ImageFolder+file, 'rb') # Open image # Read image into memory
    response = client.detect_labels(Image={'Bytes': image_file.read()}) # Gets response from API for image
    labels = response # Get labels from response
    Nlabels = len(labels)
    


    for i in range(Nlabels): # For each label we will store the MID, label, and score
        ImageID.append(filename) # Keep track Image ID
        Description.append(labels) # Store label


# Put Image ID and label into data frame
ImageLabels["imageid"] = ImageID
ImageLabels["Name"] = Description

ImageLabels.groupby(ImageID)

Export = ImageLabels.to_json (r'',orient='records')

