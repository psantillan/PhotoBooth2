from picamera2 import Picamera2, MappedArray


class Camera:
    def __init__(self, *args, **kwargs):
        self.camera = Picamera2()
        self.size = (640, 480)
        self.current_frame = None
        self.mode = {
            'video': self.camera.create_video_configuration({'size': self.size}),
            'still': self.camera.create_still_configuration(),
            'preview': self.camera.create_preview_configuration(),
        }
        self.setup_camera('video')
        self.camera.start()
        self.camera.pre_callback = self.pre_callback

    def __enter__(self):
        return self.camera

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.camera.stop()

    def setup_camera(self, mode, **kwargs):
        self.camera.configure(self.mode[mode])

    def pre_callback(self, request):
        with MappedArray(request, "main") as m:
            self.current_frame = m.array
