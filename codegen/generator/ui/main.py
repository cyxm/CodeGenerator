import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton

from codegen.generator.ui.widget.main_window import Ui_MainWindow


class Main:
    # 主窗口
    window_main = None

    def main(self):
        app = QApplication(sys.argv)

        # 配置窗口属性
        window_main = QMainWindow()

        # window_main.setWindowOpacity(1)
        # window_main.setWindowFlags(Qt.CustomizeWindowHint)
        # window_main.setAttribute(Qt.WA_TranslucentBackground)

        ui = Ui_MainWindow()
        ui.setupUi(window_main)

        emptyWidget = QWidget()
        ui.vDockPlatform.setTitleBarWidget(emptyWidget)

        # 处理窗口样式
        p = window_main.takeCentralWidget()
        del p

        window_main.setDockNestingEnabled(True)

        ui.vPlatformTree.itemDoubleClicked['QTreeWidgetItem*', 'int'].connect(
            self.slotTreeItemClick)

        window_main.show()
        sys.exit(app.exec_())
        pass

    def slotTreeItemClick(self, item, p_int):
        itemName = item.getObjectName()
        pass


main = Main()
main.main()
