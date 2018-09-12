import sys
from generator.ui.ui_window_main import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
