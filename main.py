from UI import PhotoBoothUI
from Camera import Camera


if __name__ == '__main__':
    with Camera() as camera:
        with PhotoBoothUI(window_size=(1080, 1920)) as ui:
            while True:
                camera.async_capture()
                ui.render_all(camera.current_frame)
