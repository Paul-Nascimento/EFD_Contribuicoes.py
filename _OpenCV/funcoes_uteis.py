import numpy as np
import cv2


def showImage(img):

    from matplotlib import pyplot as plt
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def getColor(obj_img,x,y):
    return obj_img.item(y, x, 0), obj_img.item(y, x, 1),obj_img.item(y, x, 2)

def setCOlor(obj_img,x,y,b,g,r):
    obj_img.itemset((y, x, 0), b)
    obj_img.itemset((y, x, 1), g)
    obj_img.itemset((y, x, 2), r)
    # a função itemset altera valores; ela recebe dois parametros, uma matriz tripla que contem altura, largura e faixa de cor e o valor RGB daquela localidade;sendo os canais de cor de 0 a 2 onde 0 é azul, 1 é verde e 2 é vermelhor

    return obj_img
def main():

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




main()