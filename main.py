import tkinter as tk
from tkinter import *
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Image Editer")
window.geometry("850x650")

img = None
original_img = None
display_img = None

def show_image(image):
    global display_img
    display_img = image

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (500,350))

    img_pil = Image.fromarray(image)
    img_tk = ImageTk.PhotoImage(img_pil)

    panel.config(image = img_tk)
    panel.image = img_tk

def load_image(path):
    global img, original_img
    
    img = cv2.imread(path)
    original_img = img.copy()

    show_image(img)

def grayscale():
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    show_image(cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR))

def blur():
    blurred = cv2.GaussianBlur(img, (15,15), 0)
    show_image(blurred)

def edge():
    edges = cv2.Canny(img, 100, 200)
    show_image(cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR))

def cartoon():
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray,5)

    edges = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9,9
    )
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon_img = cv2.bitwise_and(color, color, mask = edges)

    show_image(cartoon_img)

def reset():
    show_image(original_img)

def save_image():
    global display_img
    file_path = filedialog.asksaveasfilename(
        defaultextension = ".jpg",
        filetypes = [("JPED files", "*.jpg"), ("PNG files", "*.png")]
    )
    
    if file_path: 
        cv2.imwrite(file_path, display_img)
        print("Image saved successfully!")
    
panel = Label(window)
panel.pack(pady = 20)
frame_images = Frame(window)
frame_images.pack(pady = 10)
Button(frame_images, text = "Image 1", command = lambda: load_image('img1.jpg')).grid(row = 0, column = 0, padx = 5)
Button(frame_images, text = "Image 2", command = lambda: load_image('img2.jpg')).grid(row = 0, column = 1, padx = 5)
Button(frame_images, text = "Image 3", command = lambda: load_image('img3.jpg')).grid(row = 0, column = 2, padx = 5)
Button(frame_images, text = "Image 4", command = lambda: load_image('img4.jpg')).grid(row = 0, column = 3, padx = 5)
Button(frame_images, text = "Image 5", command = lambda: load_image('img5.jpg')).grid(row = 0, column = 4, padx = 5)
Button(frame_images, text = "Image 6", command = lambda: load_image('img6.jpg')).grid(row = 0, column = 5, padx = 5)
Button(frame_images, text = "Image 7", command = lambda: load_image('img7.jpg')).grid(row = 0, column = 6, padx = 5)
Button(frame_images, text = "Image 8", command = lambda: load_image('img8.jpg')).grid(row = 0, column = 7, padx = 5)
Button(frame_images, text = "Image 9", command = lambda: load_image('img9.jpg')).grid(row = 0, column = 8, padx = 5)
Button(frame_images, text = "Image 10", command = lambda: load_image('img10.jpg')).grid(row = 0, column = 9, padx = 5)


frame_filters = Frame(window)
frame_filters.pack(pady = 20)
Button(frame_filters, text = "Greyscale", command = grayscale).grid(row = 0, column = 0, padx = 5)
Button(frame_filters, text = "Blur", command = blur).grid(row = 0, column = 1, padx = 5)
Button(frame_filters, text = "Edge", command = edge).grid(row = 0, column = 2, padx = 5)
Button(frame_filters, text = "Cartoon", command = cartoon).grid(row = 0, column = 3, padx = 5)
Button(frame_filters, text = "Reset", command = reset).grid(row = 0, column = 4, padx = 5)

Button(window, text = 'Save Image', command = save_image, bg = 'green', fg = 'white').pack(pady = 15)
load_image('img1.jpg')
window.mainloop()