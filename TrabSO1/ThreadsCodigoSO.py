# by ricardmvv e RobsonCCarneiro

import numpy as np # Realizar cálculos em Arrays Multidimensionais
import cv2 as cv #Deteccao de faces em uma imagem
import threading
from time import sleep


def ContrasteLargo(img, altura, largura):
    imgMax = img.max()
    imgMin = img.min()
    g = np.zeros((altura,largura), np.uint8)
    print(g)
    for i in range(0, altura):
        for j in range(0, largura):
            g[i][j] = (255 // (imgMax - imgMin)) * (img[i][j] - imgMin)
    cv.imwrite('imgContraste.png', g)

def ProbabilidadeOcorrencia(hist, altura, largura): # Retorna a probabilidade de ocorrência de cada valor de pixel
    prob = [0] * 256
    for i in range(0, 256):
        prob[i] = hist[i] / (altura * largura)   
    return prob

def ProbabilidadeAcumulada(prob): # Retorna a probabilidade acumulada
    prob_ac = [0] * 256
    for i in range(0, 256):
        cont = 0
        for j in range(0, i):
            cont += prob[j]
        prob_ac[i] = cont
    return prob_ac

def OcorrenciaHistograma(img, altura, largura): # Retorna o histograma da imagem I
    hist = [0] * 256
    for i in range(altura):
        for j in range(largura):
            hist[img[i][j]] += 1
    return hist

def EqualizacaoHistograma(img, altura, largura): # Equalização de Histograma sendo realizado
    hist = OcorrenciaHistograma(img, altura, largura)
    prob = ProbabilidadeOcorrencia(hist, altura, largura)
    prob_ac = ProbabilidadeAcumulada(prob)

    g = np.zeros((altura,largura), np.uint8)
    for i in range(altura):
        for j in range(largura):
            g[i][j] = round(255 *  prob_ac[img[i][j]])

    cv.imwrite('imgHistograma.png', g)


if __name__ == '__main__':
    
    # Essa parte que vai ler o arquivo PNG
    image_path = 'balloons.png'
    image = cv.imread(image_path, 0)
    altura, largura = image.shape

    primera_thread = threading.Thread(target=ContrasteLargo, args=(image, altura, largura))
    segunda_thread = threading.Thread(target=EqualizacaoHistograma, args=(image, altura, largura))

    primera_thread.start()
    segunda_thread.start()

    primera_thread.join()
    segunda_thread.join()

    while primera_thread.is_alive():
        sleep(1)
    print('Thread 1 (Contraste)')

    while segunda_thread.is_alive():
        sleep(1)
    print('Thread 2 (Equalização de Histograma)')
