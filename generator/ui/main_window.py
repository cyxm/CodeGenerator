import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

from generator.ui.ui_main_container import Ui_MainWindow

app = QApplication(sys.argv)
# MainWindow = QMainWindow(None, Qt.FramelessWindowHint)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

# MainWindow.setWindowOpacity(1)
# MainWindow.setWindowFlags(Qt.FramelessWindowHint)
# MainWindow.setAttribute(Qt.WA_TranslucentBackground)

MainWindow.show()
sys.exit(app.exec_())
