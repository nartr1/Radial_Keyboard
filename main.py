import sys

import pygame
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class CustomWindow(QMainWindow):
    def __init__(self, surface, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setFixedSize(640, 480)
        self.setCentralWidget(ImageWidget(surface))

    def paintEvent(self, event=None):
        painter = QPainter(self)

        painter.setOpacity(0.4)
        painter.setBrush(Qt.black)
        painter.setPen(QPen(Qt.white))
        painter.drawRect(self.rect())


class ImageWidget(QWidget):
    def __init__(self, surface, parent=None):
        super(ImageWidget, self).__init__(parent)
        w = surface.get_width()
        h = surface.get_height()
        self.data = surface.get_buffer().raw
        self.image = QImage(self.data, w, h, QImage.Format_RGB32)

    def paintEvent(self, event):
        my_paint = QPainter()
        # the definitions for PyQt4 and PyQt5 use QtGui.QPainter()
        my_paint.begin(self)
        my_paint.drawImage(0, 0, self.image)
        my_paint.end()


# app = QApplication(sys.argv)

# init PyGame
pygame.init()
my_surface = pygame.Surface((800, 600))
my_surface.fill((0, 0, 255, 176))
pygame.draw.circle(my_surface, (0, 0, 127, 255), (76, 76), 76)
pygame.draw.ellipse(my_surface, (127, 0, 0, 0), (0, 0, 12, 76))

app = QApplication(sys.argv)
window = CustomWindow(my_surface)

window.setWindowFlags(Qt.FramelessWindowHint)
window.setAttribute(Qt.WA_NoSystemBackground, True)
window.setAttribute(Qt.WA_TranslucentBackground, True)


# Run the application
window.showFullScreen()
sys.exit(app.exec_())
