import pygame


class PhotoBooth:
    def __init__(self, camera, **kwargs):
        pygame.init()
        self.camera = camera
        self.window_size = self.setup_window() if 'window_size' not in kwargs else kwargs['window_size']
        self.window = pygame.display.set_mode(self.window_size, pygame.NOFRAME)
        self.running = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pygame.quit()

    def setup_window(self):
        display_info = pygame.display.Info()
        return display_info.current_w, display_info.current_h

    def run(self):
        while self.running:
            pygame.display.update()

