
"""
DISCENTE: IGOR BEZERRA REIS

Histograma.ipynb

Implementar sem libs:

**Histogram Stretching e Mapeamento Linear**

Implementar com libs:

**Histogram Equalization, Histogram Specification e CLAHE**
"""

import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt


image_test = cv2.imread('a-low-contrast-image-b-after-enhancement_Q320.jpg', cv2.IMREAD_GRAYSCALE)

"""# Histrogram Stretching"""

def histogram_stretching(image):
    # g(x,y) = ( f(x,y) - fmin / fmax - fmin ) * 255
    new_image = image.copy()

    valor_minino = image.min()
    valor_maximo = image.max()
    
    for i in range(image.shape[0]):
      for j in range(image.shape[1]):
        pixel = (image[i,j] - valor_minino) / (valor_maximo - valor_minino)
        new_image[i,j] = int(pixel * 255)
  
    return new_image

origin = image_test.copy()
image_stretching = histogram_stretching(origin)

"""# Mapeamento Linear"""

def mapeamento_linear(image):
  
  valor_minimo = image.min()
  valor_maximo = image.max()
  
  #Intervalo de valores
  minimo = 0
  maximo = 255

  escala = (maximo - minimo) / (valor_maximo - valor_minimo)

  new_image = (image - valor_minimo) * escala + minimo
  new_image = np.uint8(new_image)

  return new_image

origin = image_test.copy()
image_linear_maping = mapeamento_linear(origin)

"""# Histogram Equalization"""

def histogram_equalizaton(image):
 
  hist, bins = np.histogram(image.flatten(), 256, [0,256])
  cdf = hist.cumsum()

  cdf_normalizado = cdf * hist.max() / cdf.max()
  img_equalized = np.interp(image.flatten(), bins[:-1], cdf_normalizado).reshape(image.shape)

  return img_equalized

origin = image_test.copy()
image_equalized = histogram_stretching(origin)

"""# Histogram Specification"""

def histogram_specification(image, image_ref):
 
  hist, bins = np.histogram(image.flatten(), 256, [0,256])
  hist_ref, bins_ref = np.histogram(image_ref.flatten(), 256, [0,256])

  cdf = hist.cumsum()
  cdf_ref = hist_ref.cumsum()

  cdf_normalized = cdf * hist.max() / cdf.max()
  cdf_ref_normalized = cdf_ref * hist_ref.max() / cdf_ref.max()

  img_equalized = np.interp(image.flatten(), bins[:-1], cdf_ref_normalized).reshape(image.shape)

  img_equalized = cv2.normalize(img_equalized, None, 0, 255, cv2.NORM_MINMAX)

  return img_equalized

origin = image_test.copy()
image_specification = histogram_specification(origin, image_equalized)


"""# CLAHE"""

def algoritm_clahe(image):

  clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

  img_clahe = clahe.apply(image)

  return img_clahe

origin = image_test.copy()
image_clahe = algoritm_clahe(origin)


images = [origin, image_stretching, image_linear_maping, image_equalized, image_specification, image_clahe]
titles = ['Original', 'Stretching', 'Linear', 'Equalization', 'Specification', 'CLAHE']
output_size = (len(images) * 200, 200)
output_image = np.zeros((200, len(images) * 200), dtype=np.uint8)
for i, image in enumerate(images):
    resized_image = cv2.resize(image, (200, 200))
    output_image[:, i*200:(i+1)*200] = resized_image
    cv2.putText(output_image, titles[i], (i*200 + 50, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)


cv2.imshow('Imagens', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
