from UI import PhotoBoothUI
from test import PyGameCamera
from Camera import Camera
import os

if __name__ == '__main__':
    with Camera() as camera:
        camera.stop()
        pgc = PyGameCamera()
        pgc.run()
        #while True:
         #   frame = camera.current_frame['frame'].read()

            #print(f'Buffer Length = {len(frame)}')
            #os.system('clear')
        #with PhotoBoothUI(window_size=(1080, 1920)) as ui:
            #while True:
                #camera.async_capture()
                #ui.render_all(camera.current_frame)
