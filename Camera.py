from picamera2 import Picamera2, MappedArray, Preview
from picamera2.encoders import Encoder


class PyGameEncoder(Encoder):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface


class Camera:
    def __init__(self, *args, **kwargs):
        self.camera = Picamera2()
        self.size = (1332, 990)
        self.format = 'SRGGB10_CSI2P'
        self.current_frame = None
        self.mode = {
            'video': self.camera.create_video_configuration({'size':(640,360)}, raw={'format': str(self.format), 'size': self.size}),
            'still': self.camera.create_still_configuration(),
            'preview': self.camera.create_preview_configuration(),
        }
        self.setup_camera('video')
        self.camera.start()

    def __enter__(self):
        return self.camera

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.camera.stop()

    def setup_camera(self, mode, **kwargs):
        self.camera.configure(self.mode[mode])


