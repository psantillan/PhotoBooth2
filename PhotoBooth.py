try:
    from PyQt5.QtWidgets import QApplication, QLabel, QGridLayout, QWidget
    QT_VER = 5
except ModuleNotFoundError as e:
    from PyQt6.QtWidgets import QApplication, QLabel, QGridLayout, QWidget
    QT_VER = 6
except Exception as e:
    raise e
from picamera2.previews.qt import QGlPicamera2
from picamera2 import Picamera2


class QtApp(QApplication):
    def __init__(self, ver, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.qt_version = ver

    def exec(self):
        if self.qt_version == 6:
            super().exec()
        elif self.qt_version == 5:
            super().exec_()


class PhotoBoothApp:
    def __init__(self):
        self.app = QtApp(QT_VER, [])
        self.base = QWidget()
        self.grid = QGridLayout()
        self.picam2 = Picamera2()
        self.picam2.configure(self.picam2.create_preview_configuration())

        self.base.setLayout(self.grid)
        self.build_ui()
        self.run()

    def build_ui(self):
        label = QLabel('Howdy')
        qpicamera2 = QGlPicamera2(self.picam2, width=800, height=600, keep_ar=False)
        qpicamera2.setWindowTitle("Qt Picamera2 App")
        self.grid.addWidget(label, 1, 1)
        self.grid.addWidget(qpicamera2, 1, 2)

    def run(self):
        self.base.show()
        self.app.exec()


if __name__ == '__main__':
    pb = PhotoBoothApp()
