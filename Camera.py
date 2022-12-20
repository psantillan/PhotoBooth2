from picamera2 import Picamera2, MappedArray, Preview
from picamera2.encoders import Encoder, H264Encoder
from picamera2.outputs import CircularOutput
from libcamera import controls
from io import BytesIO
import time


class PyGameEncoder(Encoder):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface


class Camera:
    def __init__(self, *args, **kwargs):
        self.camera = Picamera2()
        self.encoder = Encoder()
        self.ring_buffer = BytesIO()
        self.sensor_size = (1332, 990)
        self.sensor_format = 'SRGGB10_CSI2P'
        self.output_size = (640, 360)
        self.current_frame = {
            'frame': BytesIO(),
            'size': self.output_size,
            'format': 'RGBA',
            'data': lambda _: self.current_frame['frame'].read()
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
        self.ring_buffer_manager = CircularOutput(file=self.current_frame['frame'], buffersize=1)

    def __enter__(self):
        #self.camera.start()
        self.camera.start_recording(self.encoder, self.ring_buffer_manager)
        print('Waiting for 1 second to get camera defaults')
        time.sleep(1)
        self.camera.set_controls({"AeMeteringMode": controls.AeMeteringModeEnum.Spot, "AwbEnable": False, "AeEnable": False, 'FrameDurationLimits': (11111, 33333)})
        self.ring_buffer_manager.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.ring_buffer_manager.stop()
        self.camera.stop()

    def setup_camera(self, mode, **kwargs):
        self.camera.configure(self.mode[mode])

    def async_capture(self):
        return self.camera.capture_buffer(wait=False, signal_function=self.capture_complete_callback)

    def capture_complete_callback(self, job):
        result = self.camera.wait(job)
        self.current_frame['data'] = result

    def capture_pre_callback(self, request):
        pass


