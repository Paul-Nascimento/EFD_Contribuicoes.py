import numpy as np
import matplotlib.pyplot as plt
import cv2
from funcoes_uteis import getColor,setCOlor,showImage

 #Se passar 0 como parâmetro a imagem não tem canal de cor
obj_img = cv2.imread('Imagens\EFD .png')
altura,largura,canais_de_cor = obj_img.shape

print(altura,largura,canais_de_cor)


for y in range(0,altura):
    for x in range(0,largura):


        azul,verde,vermelho = getColor(obj_img,x,y)

        img = setCOlor(obj_img,x,y,0,0,vermelho)

nomes_e_cnpjs = obj_img[480:650,915:1039]

obj_img[315:315 + nomes_e_cnpjs.shape[0],515:515 + nomes_e_cnpjs.shape[1]] = nomes_e_cnpjs

showImage(obj_img)
#cv2.imwrite('efd modificado.png',img)

#915,482
#1039, 650


showImage(obj_img)