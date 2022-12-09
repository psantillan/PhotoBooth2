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

    def handle(self, event):
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            if event.key and event.key == pygame.K_ESCAPE:
                pygame.quit()


    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.handle(event)
            pygame.display.update()


