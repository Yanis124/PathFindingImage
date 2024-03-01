from queue import PriorityQueue
import cv2
import glob
import numpy as np
import tkinter as tk
from tkinter import Tk, Label, PhotoImage, Button
from tkinter.ttk import Style
from PIL import Image, ImageTk

from dijkstra import *

points = [] #the two selecetd points in the image
file_image=None #the image retrived from the file  
image=None  #a matrice that represente the image
pil_image = None #turn a matrice to an image

#variables for graphic interface
imgtk=None #image used by tkinter

window=None
label= None
label_image=None
button=None


pad_x=10
pad_y=10
size_circle=None

HEIGHT=1000
WIDTH=800


FODLER_IMAGES="Image"
FONT_SIZE=12
FONT_STYLE="Arial"
FONT_WEIGHT="bold"


# Create the Tkinter interface
def create_tk_interface():
    global window, imgtk, label

    window = tk.Tk()
    window.title("Trouver le chemin le plus court dans une image")
    
    window.resizable(False, False)
    
    
    
    create_label()
    
    add_image_tk()  # Add the image to the Tkinter interface
    
    create_button()

    window.mainloop()

#add the image to the Tkinter interface
def add_image_tk():
    global window, imgtk, file_image, image, pil_image, label_image,size_circle,pad_y,pad_x
    
    files_image = glob.glob(FODLER_IMAGES+"/*.png") + glob.glob(FODLER_IMAGES+"/*.jpg") + glob.glob(FODLER_IMAGES+"/*.jpeg") + glob.glob(FODLER_IMAGES+"/*.gif") +glob.glob(FODLER_IMAGES+"/*.webp")
    file_image=files_image[0] 

    image = cv2.imread(file_image)  # Read the image and create an array(matrice) of pixels
   
    if image is None:
        print("Erreur : Impossible de charger l'image.")
        return

    # Convert the image to RGB (Pillow uses RGB)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Create a PIL Image from the NumPy array
    pil_image = Image.fromarray(image_rgb)

    # Create an initial PhotoImage
    imgtk = ImageTk.PhotoImage(pil_image)
    
    resize_image() #resize the image to fit the window
    
    window.columnconfigure(0, weight=1,minsize=imgtk.width())
    
    size_circle=int(imgtk.width()*0.003)    #define the size of the point in the image
    pad_x=int(imgtk.width()*0.01)   
    pad_y=int(imgtk.width()*0.01)
    
    label_image = tk.Label(window, image=imgtk)
    label_image.grid(row=1, column=0)
    label_image.bind("<Button-1>", on_canvas_click)
    
#resize the image to fit the window
def resize_image():
    
    global imgtk, image, pil_image
    
    resized_image = pil_image.resize((int(HEIGHT*0.9), WIDTH), Image.NEAREST)  # Use Image.NEAREST for non-interpolating resize

    # Convert the resized image to a NumPy array
    image_rgb = np.array(resized_image)

    # Convert the resized image to PhotoImage
    imgtk = ImageTk.PhotoImage(Image.fromarray(image_rgb))
 
#create a label 
def create_label():
    global pad_x, pad_y, label
    
    
    label = Label(window, text="Sélectionnez le premier point.")
    label.grid(row=0, column=0)
    label.config(
        font=(FONT_STYLE, FONT_SIZE, FONT_WEIGHT),        # Set the font family and size
        bg="lightgray",            # Set the background color
        padx=pad_x, pady=pad_y,    # Set the padding
        
    )


def on_enter(widget):
    widget.config(fg='green')  # Change text color to green on hover

def on_leave(widget):
    widget.config(fg='black')  # Change text color back to black on leave

    
#edit the text on a label
def edit_label(text):
    global lable
    label.config(text=text)
    
#create the button 
def create_button():
    
    global window, pad_x, pad_y, button
    
    button= Button(window, text="trouver le chemi le plus court", command=find_path)
    
    button.grid(row=2, column=0)
    
    #button.pack(side="bottom")

    # Configure button properties using button.config
    button.config(font=(FONT_STYLE, FONT_SIZE, FONT_WEIGHT),  padx=pad_x, pady=pad_y)

    # Bind events for custom colors during mouse hover
    button.bind("<Enter>", lambda event: on_enter(button))
    button.bind("<Leave>", lambda event: on_leave(button))
    

    
    
#refrech the image after selecting a point in the image   
def refresh_image():
    global  image, window, imgtk, pil_image, label_image
    
    image_for_tk = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(image_for_tk)
    
    # imgtk=ImageTk.PhotoImage(image=pil_image)
    resize_image()
    label_image = tk.Label(window, image=imgtk)
    
    label_image.bind("<Button-1>", on_canvas_click)
    label_image.grid(row=1, column=0, sticky="news")


# When the user clicks on the canvas, add a point to the list
def on_canvas_click(event):
    global points, image, imgtk, size_circle
    if len(points) < 2:
        x, y = event.x, event.y
        # Resize the coordinates based on the original image size
        x = int(event.x * (image.shape[1] / imgtk.width()))
        y = int(event.y * (image.shape[0] / imgtk.height()))

        points.append((x, y))
        
        # Draw a circle on the resized image
        cv2.circle(image, (x, y), size_circle, (255,0,0), -1)
        
        refresh_image()
        if len(points) == 1:
            edit_label(f"Point 1 sélectionné.")
        elif len(points) == 2:
            edit_label(f"Point 2 sélectionné.")
            
                #create_button()
           

#find the shortest path
def find_path():
    global image, points, imgtk
    if len(points) == 2:
        start, end = points

        path =dijkstra_binary_heap(image, start[::-1], end[::-1])  #find the shortest path using djikstra algorithm
        for i in range(len(path) - 1):
            cv2.line(image, path[i][::-1], path[i + 1][::-1], (0, 255, 0), 2) #draw a line between the two pixels
        refresh_image()
    add_restart_button()
        
def add_restart_button():
    global window, pad_x, pad_y, button
    
    button.config(text="Recommencer",command=restart)

#restart the program
def restart():
    global image, button, points, label
    
    image=cv2.imread(file_image)  #reload the original image
    
    refresh_image()
    points=[]
    button.config(text="trouver le chemin le plus court", command=find_path)
    label.config(text="Sélectionnez le premier point.")
    
    
        

