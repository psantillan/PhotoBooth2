from UI import PhotoBooth
from Camera import Camera
import pygame

if __name__ == '__main__':
    with Camera() as camera:
        with PhotoBooth(camera) as pb:
            pb.run()