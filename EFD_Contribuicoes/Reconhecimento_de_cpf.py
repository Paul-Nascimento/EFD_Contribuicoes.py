import pytesseract
import cv2
import pyautogui as pg
from PIL import Image
import re
from time import sleep


xSize = 2160
ySize = 1092
empresas = '164'
path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
for empresa in empresas:
    sleep(1)
    im = pg.screenshot('tesssste.png') #,region=(513,477,900,190)
    img = Image.open('tesssste.png')
    img = img.resize((xSize,ySize),Image.LANCZOS).convert('L')

    img.save('tesssste.png',dpi=(300,300))  #,dpi=(600,600)
    img_ = r'tesssste.png'
    pytesseract.pytesseract.tesseract_cmd = path
    img = cv2.imread(img_)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    ###Detecting Characters
    hImg, wImg,_ = img.shape
    boxes=pytesseract.image_to_data(img)
    texto_final = ''
    xFinal = 0
    for x,b in enumerate(boxes.splitlines()):
        #print(boxes.splitlines())
        if x!=0:
            b = b.split()
            #print(b)
            if len(b) == 12:
                 x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                 #print(y)
                 if 650 >= y >475 and 1160 >= x >1000:
                     print(b[11])
                     #print('nEXT')
                     cv2.rectangle(img,(x,y),(w+x,h+y),(255,0,0),1)
                     #cv2.putText(img,b[0],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)
                     if empresa.upper() in b[11]:
                        pg.leftClick(int(b[6]),int(b[7]))
                        #print(b[11])
                        sleep(1)
    cv2.imshow('Result',img)
    cv2.waitKey(0)
    #x=552, y=528)