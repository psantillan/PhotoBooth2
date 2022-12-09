from UI import PhotoBooth
from Camera import Camera
from Framebuffer import Framebuffer
import pygame

if __name__ == '__main__':
    fb = Framebuffer
    with Camera(fb) as camera:
        with PhotoBooth(camera, fb) as pb:
            pb.run()
