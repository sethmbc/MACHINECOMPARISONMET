#!/usr/bin/env python
import urllib
import urllib2
import json
import os

class ImagesMET(object):


    file_path_with_ids = './object_ids.txt'
    local_image_folder = './images'

    def __init__(self):
        pass


    def run_export(self):
        object_ids = self.get_objects_ids()
        met_object_api_url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/'
        object_ids = object_ids[1:-1]
        for i, object_id in enumerate(object_ids):
            object_url = met_object_api_url + object_id
            req = urllib2.Request(object_url)
            response = urllib2.urlopen(req)
            met_object = response.read()
            try:
                met_object = json.loads(met_object)
            except Exception as e:
                met_object = False
                print("Error al cargar la respuesta: JSON") 

            if met_object:
                primary_image = met_object.get('primaryImage')
                if primary_image:
                    self.download_image(primary_image)

                #additional_images = met_object.get('additionalImages')
                #for image_url in additional_images:
                    #self.download_image(image_url)
            #print '%s/%s'%(i+1, len(object_ids))

    def download_image(self, image_url):
        image_local_path = os.path.join(self.local_image_folder, image_url.rsplit('/', 1)[1])
        if not os.path.exists(image_local_path):
            try:
                urllib.urlretrieve(image_url, image_local_path)
            except Exception as e:
                print("ERROR - Image not downloaded")
                print(image_url)
                print('*'*80)
            


    def get_objects_ids(self):
        file = open(self.file_path_with_ids, 'r')
        object_ids = file.read().split('\n')
        file.close()
        return object_ids


if __name__ == "__main__":
    images_export = ImagesMET()
    images_export.run_export()