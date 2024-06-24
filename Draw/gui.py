from tkinter import *
from PIL import Image, ImageTk

def create_widget_screen(title: str) -> Tk:
    ws = Tk()
    ws.title(title)
    return ws


def open_picture(file_name: str) -> Image:
    #load the image
    return Image.open(file_name)


def create_image() -> Image:
    img = Image.new("RGB", size=(256,256))
    for x in range(256):
        for y in range(256):
            img.putpixel((x,y), (x,y,0))
    return img


def modify_image(img: Image) -> None:
    def displayPixel(x: int, y: int) -> None:
        pixel_color = img.getpixel((x, y))
        print(f"Pixel color: {pixel_color}")

    (coordX, coordY) = (150, 150)
    displayPixel(coordX, coordY)

    for x in range(11):
        for y in range(11):
            img.putpixel((coordX+x-5, coordY+y-5), (25*x,0,25*y))

    displayPixel(coordX, coordY)


def get_tkimage(image: Image) -> None:
    return ImageTk.PhotoImage(image)
