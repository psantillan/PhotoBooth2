from UI import PhotoBooth
from Camera import Camera
from Framebuffer import Framebuffer
import pygame

if __name__ == '__main__':
    fb = Framebuffer
    with Camera(fb) as camera:
        while True:
            pass
        #with PhotoBooth(camera, fb, window_size=(1080, 1920)) as pb:
            #pb.run()
