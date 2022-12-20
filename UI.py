import pygame
import sys


class PhotoBoothUI:
    def __init__(self, **kwargs):
        pygame.init()
        self.window_size = self.setup_window() if 'window_size' not in kwargs else kwargs['window_size']
        self.window = pygame.display.set_mode(self.window_size, pygame.NOFRAME)
        self.clock = pygame.time.Clock()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pygame.quit()

    def make_surface_from_frame(self, frame):

        return pygame.image.frombuffer(frame['data'](), frame['size'], frame['format'])

    def setup_window(self):
        display_info = pygame.display.Info()
        return display_info.current_w, display_info.current_h

    def handle(self, event):
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            if event.key and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key:
                if event.key == pygame.KEYUP:
                    pass
                if event.key == pygame.KEYDOWN:
                    pass

    def render_all(self, current_frame=None):
        for event in pygame.event.get():
            self.handle(event)
        if current_frame:
            surf = self.make_surface_from_frame(current_frame)
            self.window.blit(surf, (0, 0))
        pygame.display.update()
        self.clock.tick(30)




