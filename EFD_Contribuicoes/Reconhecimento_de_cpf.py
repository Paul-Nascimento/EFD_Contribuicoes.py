import pytesseract
import cv2
import pyautogui as pg
from PIL import Image
import re
from time import sleep
import matplotlib.pyplot as plt
import numpy as np
from pytesseract.pytesseract import Output



xSize = 2160
ySize = 1092
empresas = '164'
path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

sleep(1)
impa = pg.screenshot('Tela Atual.png')#,region=(513,477,900,190)


im = cv2.imread('Tela Atual.png')



im = cv2.resize(im,None,fx=4,fy=4,interpolation=cv2.INTER_CUBIC)
im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)


kernel = np.ones((1,1),np.uint8)

# im = cv2.dilate(im,kernel,iterations=1)
# im = cv2.erode(im,kernel,iterations=1)
#
# im = cv2.GaussianBlur(im,(1,1,),0)
# im = cv2.bilateralFilter(im,1,25,25)

im = cv2.threshold(cv2.GaussianBlur(im, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

im =cv2.threshold(cv2.bilateralFilter(im,1, 50, 50), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

im=cv2.threshold(cv2.medianBlur(im, 1), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

im=cv2.adaptiveThreshold(cv2.GaussianBlur(im, (1, 1), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

im=cv2.adaptiveThreshold(cv2.bilateralFilter(im, 1, 40, 40), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

im=cv2.adaptiveThreshold(cv2.medianBlur(im, 1), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)


#cv2.imshow('Image',im)

#cv2.waitKey(0)






sleep(1)
# img = Image.open(im)
# #img = img.resize((xSize,ySize),Image.LANCZOS).convert('L')
#
# #img.save('tesssste.png',dpi=(300,300))  #,dpi=(600,600)
# #img_ = r'tesssste.png'
pytesseract.pytesseract.tesseract_cmd = path
# img = cv2.imread(img_)
# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
###Detecting Characters








hImg, wImg= im.shape
print(hImg,wImg)
boxes=pytesseract.image_to_data(im)

#1800 > 2700 y
#3600 > 4100 x

for x,b in enumerate(boxes.splitlines()):


    if x != 0:
        b = b.split()


        if len(b) == 12:




            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])


            if 4150 > x > 3600 and 2600 > y > 1900:
                #print(b)
                #print(x, y, w, h)
                cnpj = b[11]
                cv2.rectangle(im, (x, y), (w+x,h+y), (0, 0, 255), 2)
                print(cnpj)
                #cv2.rectangle(im, (x, y), (w + x, h + y), (255, 0, 0), 3)
                #cv2.putText(im, b[0], (x, hImg - y + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50, 205, 50), 1)


#cv2.imshow('img', im)
#cv2.waitKey(0)

plt.imshow(im)
plt.show()
#cv2.imshow('Result',im)
#cv2.waitKey(0)
#x=552, y=528)

    # pytesseract.pytesseract.tesseract_cmd = path
    # ###Detecting Characters
    # hImg, wImg,_ = img.shape
    # boxes=pytesseract.image_to_data(img)
    # texto_final = ''
    # xFinal = 0
    # for x,b in enumerate(boxes.splitlines()):
    #     #print(boxes.splitlines())
    #     if x!=0:
    #         b = b.split()
    #         #print(b)
    #         if len(b) == 12:
    #
    #              #print(y)
    #
    #                  print(b[11])
    #                  #print('nEXT')
    #
    #                  #cv2.putText(img,b[0],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)
    #                  if empresa.upper() in b[11]:
    #                     pg.leftClick(int(b[6]),int(b[7]))
    #                     #print(b[11])
    #                     sleep(1)
    # cv2.imshow('Result',img)
    # cv2.waitKey(0)
    # #x=552, y=528)