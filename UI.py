import pygame


class PhotoBooth:
    def __init__(self, camera):
        self.camera = camera
        self.running = True

    def run(self):
        pygame.init()
        while self.running:
            pygame.display.update()
        pygame.quit()
