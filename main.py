from UI import PhotoBooth
from Camera import Camera
from picamera2.encoders import Encoder
from picamera2.outputs import FileOutput
import io
import pygame
import sys


if __name__ == '__main__':
    with Camera() as camera:
        with PhotoBooth(camera, window_size=(1080, 1920)) as pb:
            pb.run()
