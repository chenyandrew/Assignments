from tkinter import *

class Shapes:

    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        return self.length * self.height


def main():

    root = Tk()
    poly1 = Shapes(10, 5)
