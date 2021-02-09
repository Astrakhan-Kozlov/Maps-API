import sys

import PyQt5.QtGui as QtGui
import requests
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout


class MainWindow(QWidget):
    x, y = 37.677751, 55.757718

    def __init__(self):
        super().__init__()
        self.hbox = QHBoxLayout(self)
        self.lbl = QLabel(self)
        self.hbox.addWidget(self.lbl)

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 600)
        self.show()
        self.get_map()

    def get_map(self):
        with open('newfile.jpg', 'wb') as target:
            params1 = {'ll': f"{MainWindow.x},{MainWindow.y}",
                       'spn': '0.016457,0.00619',
                       'l': 'map'}
            a = requests.get('https://static-maps.yandex.ru/1.x', params=params1)
            target.write(a.content)

        pixmap = QtGui.QPixmap("newfile.jpg")
        self.lbl.setPixmap(pixmap)

        self.setWindowTitle('API-Maps')
        self.show()

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        super().keyPressEvent(event)
        if event.key() == Qt.Key_Up:
            MainWindow.y += 0.001
        if event.key() == Qt.Key_Down:
            MainWindow.y -= 0.001
        if event.key() == Qt.Key_Left:
            MainWindow.x -= 0.001
        if event.key() == Qt.Key_Right:
            MainWindow.x += 0.001
        self.get_map()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
