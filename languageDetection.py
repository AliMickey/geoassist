import pytesseract
import cv2
import numpy as np
import sys
import os

#Bulgaria, Croatia, Hungary, Macedonia, Poland, Russia, Ukraine 
tessLangsSlavic = {"bul":"bulgaria", "hrv":"croatia", "hun":"hungary", "mkd":"North Macedonia", "pol":"Poland", "rus":"Russia", "ukr":"Ukraine"}
#Estonia, Finland, Iceland, Latvia, Lithuania, Norway, Sweden
tessLangsNordicBaltic = {"est": "Estonia", "fin":"Finland", "isl":"Iceland", "lav":"Latvia", "lit":"Lithuania", "nor":"Norway", "swe":"Sweden"}
#Bangladesh, Hindi, Indonesia, Cambodia, Malaysia, Sri Lanka, Thailand
tessLangsSEA = {"ben":"Bangladesh", "hin":"India", "ind":"Indonesia", "khm":"Cambodia", "mal":"Malaysia", "sin":"Sri Lanka", "tha":"Thailand"}

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

pytesseract.pytesseract.tesseract_cmd = resource_path('resources/Tesseract-OCR/tesseract.exe')

def langDetection(slavic, nordicBaltic, sea):
    matchedCountries = ""
    selectedRegions = {}
    if slavic:
        selectedRegions.update(tessLangsSlavic)
    if nordicBaltic:
       selectedRegions.update(tessLangsNordicBaltic)
    if sea:
        selectedRegions.update(tessLangsSEA)

    #Pre-processing
    #Black and White
    img = cv2.medianBlur(cv2.cvtColor(cv2.imread(resource_path("resources/image.png")), cv2.COLOR_BGR2GRAY), 5)
    #Blur
    #img = cv2.medianBlur(img,5)
    cv2.imwrite(resource_path("resources/image.png"), img)

    #Threshold Filter
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    cv2.imwrite(resource_path("resources/imageFilter.png"), img)

    for langCode, country in selectedRegions.items():
        imgString = pytesseract.image_to_string(resource_path("resources/image.png"), lang=langCode) #Try Normal Image
        print(imgString)
        if imgString.isspace(): #If no match try filtered image
            imgString = pytesseract.image_to_string(resource_path("resources/imageFilter.png"), lang=langCode) 
            if not imgString.isspace(): #If matched using filtered image
                matchedCountries += country + ", "
                print("Matched with " + langCode + " using filtered image")
        else: #If matched using normal image
            matchedCountries += country + ", "
            print("Matched with " + langCode + " using original image")

        ## Test confidence filters
        #for country in selectedRegions:
        #imgString = pytesseract.image_to_string(Image.open('assets/image.png'), lang=country, config=conf)
        #imgData = pytesseract.image_to_data(Image.open('assets/image.png'), lang=country, output_type='data.frame')
        #imgData = imgData[imgData.conf != -1] # Remove any non-matches
        #confidence = imgData.groupby(['block_num'])['conf'].mean()
        #conf = imgData.groupby(['conf']).mean(
    return matchedCountries