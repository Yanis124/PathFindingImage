from queue import PriorityQueue
import cv2
import numpy as np
import tkinter as tk
from tkinter import Tk, Label, PhotoImage, Button
from PIL import Image, ImageTk

from graphic_interface import *


def main():
    global image, window, canvas, instruction_label
    
    create_tk_interface()
    
    add_image_tk()
    

if __name__ == "__main__":
    main()
