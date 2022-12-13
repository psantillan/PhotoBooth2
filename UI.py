import pygame
import timeit
import signal


class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message
    def handle_timeout(self, signum, frame):
        print(self.error_message)
        #raise TimeoutError(self.error_message)
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.setitimer(signal.ITIMER_REAL, 0.13, 0.01)
        #signal.alarm(self.seconds)
    def __exit__(self, type, value, traceback):
        signal.setitimer(signal.ITIMER_REAL, 0)
        #signal.alarm(0)


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

    def render_all(self):
        for event in pygame.event.get():
            self.handle(event)
        self.camera.capture_buffer(wait=False, signal_function=self.capture_complete)
        if self.current_frame:
            self.window.blit(self.current_frame, (0, 0))
        pygame.display.update()

    def run(self):
        while self.running:
            try:
                with timeout():
                    self.render_all()
            except TimeoutError:
                pass




