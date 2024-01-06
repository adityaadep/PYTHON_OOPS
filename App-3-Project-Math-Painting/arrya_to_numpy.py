import numpy as np
from PIL import Image

data = np.zeros((5, 4, 3), dtype= np.uint8)
data[:] = [255, 255, 0]
print(data)
data[0:2, 0:2] = [255, 0, 0]
data[3:4, 2:4]= [45, 150, 98]

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')