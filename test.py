import pygame
import pygame.camera
import sys
from UI import PhotoBoothUI

class PyGameCamera:
    def __init__(self):
        pygame.camera.init()
        self.window = pygame.display.set_mode((700, 500), pygame.NOFRAME)
        self.camera = pygame.camera.Camera('/dev/media1')
        self.cameras = [pygame.camera.Camera(x) for x in pygame.camera.list_cameras()]
        print(pygame.camera.list_cameras())
        #self.camera.stop()
        #self.camera.start()

    def run(self):
        while True:
            self.window.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    if event.key and event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key:
                        if event.key == pygame.KEYUP:
                            pass
                        if event.key == pygame.KEYDOWN:
                            pass
            for camera in self.cameras:
                try:
                    camera.start()
                except Exception as e:
                    print(e,  end=': ')
                ready = self.camera.query_image()
                print(f'img ready {ready}')
            pygame.display.update()