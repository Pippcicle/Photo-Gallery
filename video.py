import cv2
import os
from PIL import Image


image_folder = r"C:\\Users\\Pippa Smith\\Documents\\Coding\\OpenCV\\Photo Gallery"
os.chdir = (image_folder)
path = image_folder
height = 400
width = 300

image_files = []
for file in os.listdir('.'):
    if file.lower().endswith(('.png')):
        image_files.append(file)

num_of_images = len(image_files)

for file in image_files:
    img = Image.open(os.path.join(path,file))
    imgResized = img.resize(
        (height,width),
        Image.Resampling.LANCZOS
    )
    imgResized.save(file,'JPEG', quality = 95)

def VideoGenerator(): 
    video_name = 'Video.avi'

    images = []
    for img in os.listdir('.'):
        if img.lower().endswith(('.png')):
            images.append(img)

    frame = cv2.imread(images[0])
    height,width,layers = frame.shape
    
    video = cv2.VideoWriter(video_name, 0, 1,(width,height))

    for image in images : 
        video.write(cv2.imread(image))

    video.release()
    cv2.destroyAllWindows

VideoGenerator()

