from UI import PhotoBooth
from Camera import Camera

if __name__ == '__main__':
    with Camera() as camera:
        pass
        with PhotoBooth(camera, window_size=(1080, 1920)) as pb:
            pb.run()
