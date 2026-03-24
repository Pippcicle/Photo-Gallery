import cv2
import os
from PIL import Image


image_folder = r"C:\\Users\\Pippa Smith\\Documents\\Coding\\OpenCV\\Photo Gallery"
os.chdir(image_folder)
path = image_folder
height = 400
width = 300

image_files = []
for file in os.listdir(path):
    if file.lower().endswith(('.png')):
        image_files.append(file)

resized_images = []

for file in image_files:
    img = Image.open(os.path.join(path,file))
    img = img.convert('RGB')
    imgResized = img.resize(
        (width,height),
        Image.Resampling.LANCZOS
    )
    new_name = file.split('.')[0]+'.jpg'
    imgResized.save(new_name,'JPEG', quality = 95)
    resized_images.append(new_name)


def VideoGenerator(): 
    video_name = 'Video.avi'

    resized_images.sort()
    
    frame = cv2.imread(resized_images[0])
    height,width,layers = frame.shape
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter(video_name, fourcc, 1, (width, height))

    for image in resized_images : 
        video.write(cv2.imread(image))

    video.release()
    cv2.destroyAllWindows()

VideoGenerator()

