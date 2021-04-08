import pytesseract
from iso639 import languages
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'resources/Tesseract-OCR/tesseract.exe'

#Bulgaria, Croatia, Hungary, Macedonia, Poland, Russia, Ukraine 
tessLangsSlavic = ["bul","hrv","hun","mkd","pol","rus","ukr"]
#Estonia, Finland, Iceland, Latvia, Lithuania, Norway, Sweden
tessLangsNordicBaltic = ["est","fin","isl","lav","lit","nor","swe"]
#Bangladesh, Hindi, Indonesia, Cambodia, Malaysia, Sri Lanka, Thailand
tessLangsSEA = ["ben","hin","ind","khm","mal","sin","tha"]


def langDetection(slavic, nordicBaltic, sea):
    matchedCountries = ""
    selectedRegions = []
    if slavic:
        selectedRegions.extend(tessLangsSlavic)
    if nordicBaltic:
        selectedRegions.extend(tessLangsNordicBaltic)
    if sea:
        selectedRegions.extend(tessLangsSEA)

    #Pre-processing
    #Black and White
    img = cv2.medianBlur(cv2.cvtColor(cv2.imread('assets/image.png'), cv2.COLOR_BGR2GRAY), 5)
    #Blur
    #img = cv2.medianBlur(img,5)
    cv2.imwrite('assets/image.png', img)

    #Threshold Filter
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    cv2.imwrite('assets/imageFilter.png', img)

    for country in selectedRegions:
        imgString = pytesseract.image_to_string('assets/image.png', lang=country) #Try Normal Image
        if imgString.isspace(): #If no match try filtered image
            imgString = pytesseract.image_to_string('assets/imageFilter.png', lang=country) 
            if not imgString.isspace(): #If matched using filtered image
                matchedCountries += languages.get(part3=country).name + ", "
                print("Matched with " + country + " using filtered image")
        else: #If matched using normal image
            matchedCountries += languages.get(part3=country).name + ", "
            print("Matched with " + country + " using original image")

        ## Test confidence filters
        #for country in selectedRegions:
        #imgString = pytesseract.image_to_string(Image.open('assets/image.png'), lang=country, config=conf)
        #imgData = pytesseract.image_to_data(Image.open('assets/image.png'), lang=country, output_type='data.frame')
        #imgData = imgData[imgData.conf != -1] # Remove any non-matches
        #confidence = imgData.groupby(['block_num'])['conf'].mean()
        #conf = imgData.groupby(['conf']).mean(
    return matchedCountries