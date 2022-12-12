import pygame
import timeit

class PhotoBooth:
    def __init__(self, camera, **kwargs):
        pygame.init()
        self.camera = camera
        self.window_size = self.setup_window() if 'window_size' not in kwargs else kwargs['window_size']
        self.window = pygame.display.set_mode(self.window_size, pygame.NOFRAME)
        self.running = True
        self.current_frame = None

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

    def capture_complete(self, job):
        result = self.camera.wait(job)
        capture = pygame.image.frombuffer(result, self.camera.video_configuration.main.size, 'RGBA')
        self.current_frame = capture
        #return capture

    def run(self):
        avg = 0
        while self.running:
            print(avg)
            start = timeit.default_timer()
            for event in pygame.event.get():
                self.handle(event)
            self.camera.capture_buffer(wait=False, signal_function=self.capture_complete)
            if self.current_frame:
                self.window.blit(self.current_frame, (0, 0))

            pygame.display.update()
            end = timeit.default_timer()
            avg = (avg + (end - start))/2


