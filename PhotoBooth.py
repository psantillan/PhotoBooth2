from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QApplication, QWidget
from picamera2.previews.qt import QGlPicamera2
from picamera2 import Picamera2


class PhotoBooth:
    def __init__(self, window):
        window.resize(800, 600)
        self.picam2 = Picamera2()
        self.config = {
            'preview': self.picam2.create_preview_configuration(),
            'still': self.picam2.create_still_configuration()
        }
        self.picam2.configure(self.config['preview'])
        self.qpicamera2 = QGlPicamera2(self.picam2, width=1280, keep_ar=True)
        self.qpicamera2.done_signal.connect(self.capture_done)
        self.picam2.start()


        self.layout = QVBoxLayout()
        self.button = QPushButton("Click to capture")
        self.button.clicked.connect(self.capture)
        self.setup_ui()
        window.setLayout(self.layout)

    def setup_ui(self):
        self.button.setGeometry(200, 150, 100, 40)
        self.layout.addWidget(self.qpicamera2)
        self.layout.addWidget(self.button)

    def capture_done(self):
        self.picam2.wait()
        print('done')
        self.button.setEnabled(True)
        self.button.setText("Click to capture")

    def capture(self):
        self.button.setEnabled(False)
        self.button.setText('Capturing....')
        self.picam2.switch_mode_and_capture_file(self.config['still'], 'test.jpg', signal_function=self.qpicamera2.signal_done)


if __name__ == "__main__":
    app = QApplication([])
    MainWindow = QWidget()
    pb = PhotoBooth(MainWindow)
    MainWindow.show()
    app.exec()