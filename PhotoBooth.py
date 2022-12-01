from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QApplication, QWidget
from picamera2.previews.qt import QGlPicamera2
from picamera2 import Picamera2


class PhotoBooth:
    def __init__(self, window):
        self.picam2 = Picamera2()
        self.config = {
            'preview': self.picam2.create_preview_configuration(),
            'still': self.picam2.create_still_configuration()
        }
        self.picam2.configure(self.config['preview'])
        self.qpicamera2 = QGlPicamera2(self.picam2, width=800, height=600, keep_ar=True)
        self.picam2.start()


        self.layout = QVBoxLayout()
        self.setup_ui()
        window.setLayout(self.layout)

    def setup_ui(self):
        button = QPushButton("Click to capture JPEG")
        self.layout.addWidget(self.qpicamera2)
        self.layout.addWidget(button)



if __name__ == "__main__":
    app = QApplication([])
    MainWindow = QWidget()
    pb = PhotoBooth(MainWindow)
    MainWindow.show()
    app.exec()