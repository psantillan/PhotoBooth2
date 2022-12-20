import pygame
import pygame.camera
import sys
from UI import PhotoBoothUI

class PyGameCamera:
    def __init__(self):
        pygame.camera.init()
        self.window = pygame.display.set_mode((700, 500), pygame.NOFRAME)
        self.camera = pygame.camera.Camera('/dev/media1', (640, 360))
        self.cameras = [pygame.camera.Camera(x, (640, 360)) for x in pygame.camera.list_cameras()]
        print(pygame.camera.list_cameras())
        self.state = {}
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
            for i in range(len(self.cameras)):
                camera = self.cameras[i]
                temp = None
                try:
                    camera.start()
                except Exception as e:
                    temp = e
                    # print(e,  end=': ')
                finally:
                    if i in self.state.keys():
                        if self.state[i] != temp:
                            print(f'input {i}: {temp}')
                            self.state[i] = temp
                    else:
                        print(f'input {i}: {temp}')
                        self.state[i] = temp
                ready = self.camera.query_image()
                print(f'img ready {ready}')
            pygame.display.update()