from UI import PhotoBooth
from Camera import Camera
from picamera2.encoders import Encoder
import io
import pygame


if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode((600,400))
    with Camera() as camera:
        data = io.BytesIO()
        encoder = Encoder()
        camera.start_recording(encoder, data)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    if event.key and event.key == pygame.K_ESCAPE:
                        pygame.quit()
            print(len(data))
            pygame.display.update()

        #with PhotoBooth(camera, window_size=(1080, 1920)) as pb:
            #pb.run()
