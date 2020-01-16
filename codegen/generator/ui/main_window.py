import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

from codegen.generator.ui.widget.main_window import Ui_MainWindow

app = QApplication(sys.argv)

# 配置窗口属性
window_main = QMainWindow()

window_main.setMinimumSize(800, 600)

# window_main.setWindowOpacity(1)
# window_main.setWindowFlags(Qt.CustomizeWindowHint)
# window_main.setAttribute(Qt.WA_TranslucentBackground)

ui = Ui_MainWindow()
ui.setupUi(window_main)

p = window_main.takeCentralWidget()
del p

window_main.setDockNestingEnabled(True)


window_main.show()
sys.exit(app.exec_())
