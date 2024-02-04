# --------------------------------------------------------
# Camera sample code for Tegra X2/X1
#
# This program could capture and display video from
# IP CAM, USB webcam, or the Tegra onboard camera.
# Refer to the following blog post for how to set up
# and run the code:
#   https://jkjung-avt.github.io/tx2-camera-with-python/
#
# Written by JK Jung <jkjung13@gmail.com>
# --------------------------------------------------------

import os

import cv2
import time
from threading import Thread


def create_video_from_images(cfg):

    import glob
    vfile= '{}/video_from_images.avi'.format(cfg['path_to_video'])
    fileidx = 0
    if not  os.path.exists(vfile):
        img_array = []
        if cfg['video_order'] == 'any':
            for filename in os.listdir(cfg['path_to_video']):
                filename = os.path.join(cfg['path_to_video'],filename )
                img = cv2.imread(filename)
                height, width, layers = img.shape
                size = (width,height)
                img_array.append(img)
                fileidx+=1
        else:
            while 1:
                filename = os.path.join(cfg['path_to_video'], f"{fileidx:06d}.png")
                if not os.path.exists(filename): 
                    filename = os.path.join(cfg['path_to_video'], "1_{}.jpg".format(fileidx))#f"{fileidx}.jpg")
                if not os.path.exists(filename):    
                    break
                img = cv2.imread(filename)
                height, width, layers = img.shape
                size = (width,height)
                img_array.append(img)
                fileidx+=1

        out = cv2.VideoWriter('{}/video_from_images.avi'.format(cfg['path_to_video']),cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
         
        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()
    cfg['path_to_video'] = vfile
    return cv2.VideoCapture(cfg['path_to_video']) 



class ThreadedCamera(object):
    def __init__(self, src=0, fps=0):
       
        self.capture = cv2.VideoCapture(src)
        self.capture.set(cv2.CAP_PROP_BUFFERSIZE, 1)
       
        # FPS = 1/X
        # X = desired FPS
        self.FPS = False
        self.FPS_MS = False
        if fps > 0:
            self.FPS = 1/fps
            self.FPS_MS = int(self.FPS * 1000)
            
        # Start frame retrieval thread
        self.read_once = False
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()
        print("done setting video")
        
    def update(self):
    
        while True:
            if self.capture.isOpened():
                (self.status, self.tmp_frame) = self.capture.read()
                if self.status:
                    self.read_once = True
                    self.frame = self.tmp_frame
                else:
                    print("Camera report: No new frames, read status: ", self.status)
            
            if self.FPS: 
                time.sleep(self.FPS)
    def read(self):
        if self.read_once: 
            return True, self.frame
        else:
            return False,None

#if __name__ == '__main__':
   