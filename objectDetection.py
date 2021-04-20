import sys, os, io
from google.cloud import vision

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def objectDetection(landmark):
    landmarksString = ""
    if landmark:
        client = vision.ImageAnnotatorClient()

        with io.open(resource_path("resources/image.png"), 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        response = client.landmark_detection(image=image)
        landmarks = response.landmark_annotations
        print('Landmarks:')

        for landmark in landmarks:
            landmarksString += landmark.description + ", "
    return landmarksString