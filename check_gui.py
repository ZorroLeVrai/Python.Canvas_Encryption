from tkinter import *
from PIL import Image, ImageTk
from Draw.gui import create_widget_screen, open_picture, modify_image, get_tkimage, create_image

def display_picture():
    img = open_picture(r".\Pythagore_V1.png")
    modify_image(img)
    return img


ws = create_widget_screen("Test with a picture")
#img = display_picture()
img = create_image()

photoImage = get_tkimage(img)
Label(ws, image=photoImage).pack()

#main loop
ws.mainloop()
