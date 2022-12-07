import pygame
from picamera2 import Picamera2
import sys


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

    def capture(self, *args, **kwargs):
        return self.camera.capture_buffer(*args, **kwargs)

class PhotoBooth:
    def __init__(self, camera, *args, **kwargs):
        pygame.init()
        self.camera = camera
        self.size = (1600, 2560) if 'window_size' not in kwargs else kwargs['window_size']
        self.window = pygame.display.set_mode(self.size, pygame.NOFRAME)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            self.window.fill((255, 255, 255))
            cam_data = self.camera.capture()
            cam_surface = pygame.image.frombuffer(cam_data, self.camera.size, 'RGBA')
            self.window.blit(cam_surface, (int(self.size[0]/2) - int(self.camera.size[0]/2), int(self.size[1]*0.1)))
            pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    pb = PhotoBooth(Camera())
    pb.run()
