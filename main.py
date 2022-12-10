from UI import PhotoBooth
from Camera import Camera
from Framebuffer import Framebuffer
from picamera2 import Preview
import pygame

if __name__ == '__main__':
    fb = Framebuffer
    with Camera(fb) as camera:
        camera.start_preview(Preview.QTGL)
        while True:
            pass
        #with PhotoBooth(camera, fb, window_size=(1080, 1920)) as pb:
            #pb.run()
