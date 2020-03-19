import json
from watson_developer_cloud import VisualRecognitionV3
import io
import os
import pandas as pd
import re

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='17jIBKqhYD9f4jJDdTh3Ld0vQC5Km2JcZ4pyRj0vM4bm')

ImageFolder = "images/dir_001/"

for file in os.listdir(ImageFolder):
    filename = os.path.basename(file).split('.jpg')[0] # Get image ID
    image_file = io.open(ImageFolder+file, 'rb') # Open image
    classes = visual_recognition.classify(
        image_file,
        threshold='0.6',
    classifier_ids='default').get_result()
    with open('result3.json', 'a') as fp:
        json.dump(classes, fp)





