import numpy as np
import matplotlib.pyplot as plt
import cv2

#Eu posso converter em cinza a imagem simplesmente passando 0 como parâmetro
img = cv2.imread(r'Imagens\EFD .png',0)

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


plt.imshow(img)
plt.show()