from PIL import Image
import pytesseract
from iso639 import languages
import enhance

pytesseract.pytesseract.tesseract_cmd = 'resources/Tesseract-OCR/tesseract.exe'

#Bulgaria, Croatia, Hungary, Macedonia, Poland, Russia, Ukraine 
tessLangsSlavic = ["bul","hrv","hun","mkd","pol","rus","ukr"]
#Estonia, Finland, Iceland, Latvia, Lithuania, Norway, Sweden
tessLangsNordicBaltic = ["est","fin","isl","lat","lit","nor","swe"]
#Bangladesh, India, Cambodia, Malaysia, Sri Lanka, Thailand
tessLangsSEA = ["ben","ind","khm","mal","slk","tha"]


def langDetection(inputRegions):
    matchedCountries = ""
    selectedRegions = []
    if "slavic" in inputRegions:
        selectedRegions.extend(tessLangsSlavic)
    if "nordicBaltic" in inputRegions:
        selectedRegions.extend(tessLangsNordicBaltic)
    if "SEA" in inputRegions:
        selectedRegions.extend(tessLangsSEA)
    for country in selectedRegions:
        imgString = pytesseract.image_to_string(Image.open('assets/image.png'), lang=country)
        if not imgString.isspace():
            matchedCountries += languages.get(part3=country).name + ", "
            print("Matched with " + country)
        else:
            print("No match for " + country)
    return matchedCountries