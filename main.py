import sys
import random
from PyQt6 import QtWidgets, QtGui, uic
from PyQt6.QtCore import Qt

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Circle Drawer')
        self.pushButton.clicked.connect(self.draw_circles)
        self.pixmap = QtGui.QPixmap(self.label.size())
        self.pixmap.fill(Qt.GlobalColor.white)
        self.label.setPixmap(self.pixmap)

    def draw_circles(self):
        painter = QtGui.QPainter(self.pixmap)
        for _ in range(5):
            diameter = random.randint(10, 100)
            x = random.randint(0, self.label.width() - diameter)
            y = random.randint(0, self.label.height() - diameter)
            painter.setBrush(QtGui.QColor(255, 255, 0))
            painter.drawEllipse(x, y, diameter, diameter)
        painter.end()
        self.label.setPixmap(self.pixmap)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
