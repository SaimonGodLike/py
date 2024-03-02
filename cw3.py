import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QGridLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize

class CustomButton(QPushButton):
    def __init__(self, s1, s2, s3, parent=None):
        super(CustomButton, self).__init__(parent)
        self.normal_icon = QIcon(s1)
        self.hover_icon = QIcon(s2)
        self.pressed_icon = QIcon(s3)
        self.setMouseTracking(True)
        self.setStyleSheet("border: none;")
        self.updateIcon(self.normal_icon)

    def updateIcon(self, icon):
        self.setIcon(icon)
        self.setIconSize(icon.actualSize(QSize(64, 64)))  # Примерный размер иконки

    def enterEvent(self, event):
        self.updateIcon(self.hover_icon)

    def leaveEvent(self, event):
        self.updateIcon(self.normal_icon)

    def mousePressEvent(self, event):
        self.updateIcon(self.pressed_icon)

    def mouseReleaseEvent(self, event):
        self.updateIcon(self.hover_icon)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.button = CustomButton("start.png", "start1.png", "start.png")
        self.button.clicked.connect(self.showCalculator)
        self.layout.addWidget(self.button)

    def showCalculator(self):
        # Clear layout
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        # Add calculator
        calculator_layout = QGridLayout()
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        positions = [(i, j) for i in range(4) for j in range(4)]
        for position, button_label in zip(positions, buttons):
            button = QPushButton(button_label)
            calculator_layout.addWidget(button, *position)
        self.layout.addLayout(calculator_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 400, 300)
    window.show()
    sys.exit(app.exec_())
