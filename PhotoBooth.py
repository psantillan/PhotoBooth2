import pygame
from picamera2 import Picamera2

class Camera:
    def __init__(self, *args, **kwargs):
        # initialize picamera2
        self.camera = Picamera2()
        self.size = (800, 600) if 'size' not in kwargs else kwargs['size']
        # create sensor configs
        self.mode = {

            'preview': self.camera.create_preview_configuration({'size': self.size}),
            'still': self.camera.create_still_configuration()
        }
        # apply the configuration
        self.camera.configure(self.mode['preview'])
        # start camera
        self.camera.start()


class PhotoBooth:
    def __init__(self, camera, *args, **kwargs):
        pygame.init()
        self.camera = camera
        self.size = (640, 480) if 'window_size' not in kwargs else kwargs['window_size']
        self.window = pygame.display.set_mode(self.size)

    def run(self):
        running = True
        while running:
            self.window.fill((255, 255, 255))
            cam_data = self.camera.camera.capture_buffer()
            cam_surface = pygame.image.frombuffer(cam_data, self.camera.size, 'RGBA')
            self.window.blit(cam_surface, (0, 0))
            pygame.display.update()


if __name__ == "__main__":
    pb = PhotoBooth(Camera())
    pb.run()
