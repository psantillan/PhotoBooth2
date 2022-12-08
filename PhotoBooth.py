import pygame
from picamera2 import Picamera2
import sys
import timeit


class Camera:
    def __init__(self, *args, **kwargs):
        # initialize picamera2
        self.camera = Picamera2()
        self.size = (640, 480) if 'size' not in kwargs else kwargs['size']
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

    def wait(self, job):
        return self.camera.wait(job)

class PhotoBooth:
    def __init__(self, camera, *args, **kwargs):
        pygame.init()
        self.camera = camera
        self.size = (1600, 2560) if 'window_size' not in kwargs else kwargs['window_size']
        self.window = pygame.display.set_mode(self.size, pygame.NOFRAME)
        self.current_image = None

    def preview_capture_complete(self, job):
        result = self.camera.wait(job)
        capture = pygame.image.frombuffer(result, self.camera.size, 'RGBA')
        self.current_image = pygame.transform.scale2x(capture)


    def run(self):
        running = True
        starttime = timeit.default_timer()
        while running:
            #self.camera.capture(wait=False, signal_function=self.preview_capture_complete)
            self.camera.capture(wait=False)
            capturedone = timeit.default_timer()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()


            #raw_surface = pygame.image.frombuffer(cam_data, self.camera.size, 'RGBA')
            #cam_surface = pygame.transform.scale(raw_surface, (1440, 1080))
            #cam_surface = pygame.transform.scale2x(raw_surface)
            drawstart = timeit.default_timer()
            self.window.fill((10, 10, 10))
            # Initializing Color
            color = (75, 68, 83)
            btn_color = (255, 128, 102)

            # Drawing BG Rectangle
            pygame.draw.rect(self.window, color, [
                int(self.size[0]/2) - int((1280+50)/2),
                25,
                1280+50,
                960+50
            ], 0, 20)

            # Drawing button Rectangle
            pygame.draw.rect(self.window, btn_color, [
                int(self.size[0]/2) - 400,
                int(self.size[1]/2) + 700,
                800,
                400
            ], 0, 5)
            drawend = timeit.default_timer()
            if self.current_image:
                self.window.blit(self.current_image, (int(self.size[0]/2) - 640, 50))
            photorendered = timeit.default_timer()
            pygame.display.update()
            print(f'Total Time: {photorendered-starttime}\n  Capture Command: {capturedone - starttime}\n  Draw Calls: {drawend-drawstart}\n  Capture and Render: {photorendered-drawend}')
        pygame.quit()


if __name__ == "__main__":
    pb = PhotoBooth(Camera(), window_size=(1080, 1920))
    pb.run()
