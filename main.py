import sys
import random

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QPen, QColor


class FlagMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.data = []
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Фокус со словами')
        self.pushButton = QPushButton('Создать окружность', self)
        self.pushButton.setGeometry(280, 0, 201, 28)
        self.pushButton.resize(self.pushButton.sizeHint())
        self.pushButton.move(280, 0)
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_Ellipse(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_Ellipse(self, qp):
        self.data.append([random.randint(100, 800 - 200), random.randint(100, 600 - 200), random.randint(10, 180),
                          random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)])
        for i in self.data:
            pen = QPen(QColor(i[3], i[4], i[5]))
            qp.setPen(pen)
            qp.drawEllipse(i[0], i[1], i[2], i[2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlagMaker()
    ex.show()
    sys.exit(app.exec_())
