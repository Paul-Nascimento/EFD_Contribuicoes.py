import numpy as np
import matplotlib.pyplot as plt
import cv2
from funcoes_uteis import getColor,setCOlor,showImage,showImageGrid





img = cv2.imread(r'Imagens\EFD .png')
xSize = 2160
ySize = 1092
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
twoDimage = img.reshape((xSize,ySize),1.0)
