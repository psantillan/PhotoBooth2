from picamera2 import Picamera2, MappedArray, Preview
from picamera2.encoders import Encoder


class PyGameEncoder(Encoder):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface


class Camera:
    def __init__(self, *args, **kwargs):
        self.camera = Picamera2()
        self.sensor_size = (1332, 990)
        self.sensor_format = 'SRGGB10_CSI2P'
        self.output_size = (640, 360)
        self.current_frame = {
            'data': None,
            'size': self.output_size,
            'format': 'RGBA'
        }
        self.mode = {
            'video': self.camera.create_video_configuration(
                {'size':self.output_size},
                raw={
                    'format': str(self.sensor_format),
                    'size': self.sensor_size
                }
            ),
            'still': self.camera.create_still_configuration(),
            'preview': self.camera.create_preview_configuration(),
        }
        self.setup_camera('video')
        self.camera.pre_callback = self.capture_pre_callback
        self.camera.start()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.camera.stop()

    def setup_camera(self, mode, **kwargs):
        self.camera.configure(self.mode[mode])

    def async_capture(self):
        return self.camera.capture_buffer(wait=False, signal_function=self.capture_complete_callback)

    def capture_complete_callback(self, job):
        result = self.camera.wait(job)
        self.current_frame['data'] = result

    def capture_pre_callback(self, request):
        with MappedArray(request, "main") as m:
            print(m.array)


