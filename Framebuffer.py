class Framebuffer:
    def __init__(self):
        self.current_frame = None

    def __get__(self, instance, owner):
        return instance.current_frame

    def __set__(self, instance, value):
        instance.current_frame = value
