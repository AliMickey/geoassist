from PIL import Image
import pytesseract
from google_trans_new import google_translator  
from langdetect import detect

detector = google_translator()  
translator = google_translator()  
pytesseract.pytesseract.tesseract_cmd = 'resources/Tesseract-OCR/tesseract.exe'

#Bulgaria, Croatia, Hungary, Macedonia, Poland, Russia, Ukraine 
tessLangsSlavic = "bul+hrv+hun+mkd+pol+rus+ukr"
#Estonia, Finland, Iceland, Latvia, Lithuania, Norway, Sweden
tessLangsNordicBaltic = ["est","fin","isl","lat","lit","nor","swe"]
#Bangla, India, Cambodia, Malaysia, Sri Lanka, Thailand, Turkey
tessLangsSEA = ["ben","ind","khm","mal","slk","tha","tur"]

#imgString = pytesseract.image_to_string(Image.open('image.png'), lang=(tessLangsSlavic + "+" + tessLangsNordicBaltic))

print(pytesseract.image_to_string(Image.open('image.png')))
# matchedCountryCodes = {}
# for country in tessLangsNordicBaltic:
#     imgString = pytesseract.image_to_string(Image.open('image.png'), lang="tur")
#     if not imgString.isspace():
#         matchedCountryCodes[country] = imgString
#         print("Matched with " + country)
#     else:
#         print("No match for " + country)
# for country in matchedCountryCodes:
#     print(country)

    
    

# if not imgString.isspace():
#     print("Input String: " + imgString)

#     detect_result = detector.detect(imgString)
#     print("Detection (Google): " + str(detect_result))
#     print("Detection (Custom): " + detect(imgString))
    
    
#     if detect_result[0] != 'en':
#         translate_text = translator.translate(imgString, lang_tgt='en') 
#         print("Translated: " + translate_text)

# else:
#     print("Did not detect anything")



# languageCodes = []
# with open('resources/countryInfo.txt') as f:
#         reader = csv.reader(f, delimiter="\t")
#         d = list(reader)
#         for row in d:
#             languageCodes.append(row[15])
#         print(languageCodes)