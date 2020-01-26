import sys

from PyQt5.QtWidgets import QApplication

from pride.widgets import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())
