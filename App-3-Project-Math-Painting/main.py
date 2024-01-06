import numpy as np
from PIL import Image


class Canvas:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # create a 3d numpy arrays of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, imagepath):
        # converts the current array into image file
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)


class Square:

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x:self.x + self.side, self.y:self.y + self.side] = self.color


class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x:self.y + self.width, self.x:self.y + self.height] = self.color


canvas = Canvas(30, 20, (255, 255, 255))

rect = Rectangle(1, 6, 10, 7, (0, 100, 222))
rect.draw(canvas)

sqr = Square(3, 14, 12, (100, 200, 125))
sqr.draw(canvas)
canvas.make("test.png")
