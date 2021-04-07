from PIL import Image
import pytesseract
from iso639 import languages
from langdetect import detect_langs
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
    #for country in selectedRegions:
        #imgString = pytesseract.image_to_string(Image.open('assets/image.png'), lang=country, config=conf)
        #imgData = pytesseract.image_to_data(Image.open('assets/image.png'), lang=country, output_type='data.frame')
        #imgData = imgData[imgData.conf != -1] # Remove any non-matches
        #confidence = imgData.groupby(['block_num'])['conf'].mean()
        #conf = imgData.groupby(['conf']).mean(
    img = cv2.imread('assets/image.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('assets/bw.png', img)

    img = cv2.medianBlur(img,5)
    cv2.imwrite('assets/blur.png', img)

    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    cv2.imwrite('assets/thres.png', img)


    kernel = np.ones((5,5),np.uint8)
    img = cv2.dilate(img, kernel, iterations = 1)
    cv2.imwrite('assets/dilate.png', img)


    kernel = np.ones((5,5),np.uint8)
    img = cv2.erode(img, kernel, iterations = 1)
    cv2.imwrite('assets/erode.png', img)

    kernel = np.ones((5,5),np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    cv2.imwrite('assets/morph.png', img)

    #cv2.imwrite('assets/image2.png', img)
    imgS = pytesseract.image_to_string('assets/thres.png', lang="ben")
    print(detect_langs(imgS))
    print(imgS)

    
        # if not imgString.isspace():
        #     matchedCountries += languages.get(part3=country).name + ", "
        #     print("Matched with " + country)
        #     print(detect_langs(imgString))
        # else:
        #     print("No match for " + country)

    return matchedCountries