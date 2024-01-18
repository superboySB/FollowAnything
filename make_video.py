from PIL import Image
import cv2
import numpy as np
import os

# Let's create a function to concatenate the images to a video
def images_to_video(image_folder, output_video_file, frame_rate=30):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    # Sort the images by file name
    images.sort(key=lambda x: int(x.split('.')[0]))

    # Determine the width and height from the first image
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    # Define the codec and create VideoWriter object
    # fourcc = cv2.VideoWriter_fourcc(*'FFV1')  # Using FFV1 codec for lossless video
    fourcc = cv2.VideoWriter_fourcc(*'XVID') # 压缩
    video = cv2.VideoWriter(output_video_file, fourcc, frame_rate, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    video.release()

# Folder where the images are stored
image_folder = './our_follow_data'
# Output video file
output_video_file = './example_videos/ours.avi'

# Convert images to video
images_to_video(image_folder, output_video_file)

# Check if the video was successfully created
os.path.exists(output_video_file), output_video_file
