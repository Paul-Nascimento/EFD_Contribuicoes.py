import numpy as np
import cv2
from matplotlib import pyplot as plt


obj_img = cv2.imread("Imagens\EFD .png")

obj_img = cv2.cvtColor(obj_img,cv2.COLOR_BGR2RGB)

plt.imshow(obj_img)
plt.show()