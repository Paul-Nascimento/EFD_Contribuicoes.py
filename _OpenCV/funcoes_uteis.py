import matplotlib.pyplot as plt
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

def showImageGrid(img,title):
    fig,axis = plt.subplots()
    imgMPLIB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    axis.imshow(imgMPLIB)
    axis.set_title(title)
    plt.show()

