# -*- coding: UTF-8 -*-

import cv2.cv as cv
import tesseract

path = raw_input('Input Image Path:')
lang = raw_input('Input language chi_sim or eng:')


image=cv.LoadImage(path, cv.CV_LOAD_IMAGE_GRAYSCALE)

api = tesseract.TessBaseAPI()
api.Init(".",lang,tesseract.OEM_DEFAULT)
#api.SetPageSegMode(tesseract.PSM_SINGLE_WORD)
api.SetPageSegMode(tesseract.PSM_AUTO)
tesseract.SetCvImage(image,api)
text=api.GetUTF8Text()
conf=api.MeanTextConf()
print text
