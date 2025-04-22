import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSplitter, QSplitterHandle, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class CustomSplitter(QSplitter):
    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)
        self.widgets_visibility = [True] * 3  # 保存每个 widget 的可见性状态

    def createHandle(self):
        # 使用自定义的 SplitterHandle
        return CustomSplitterHandle(self.orientation(), self)

    def toggleWidget(self, index):
        """隐藏或显示指定的 QWidget"""
        if 0 <= index < self.count():
            widget = self.widget(index)
            if self.widgets_visibility[index]:
                widget.setMaximumWidth(0)
                widget.setMinimumWidth(0)
            else:
                widget.setMaximumWidth(16777215)  # 恢复默认宽度
                widget.setMinimumWidth(50)  # 设置一个合理的最小宽度
            self.widgets_visibility[index] = not self.widgets_visibility[index]


class CustomSplitterHandle(QSplitterHandle):
    def __init__(self, orientation, parent):
        super().__init__(orientation, parent)

    def mouseDoubleClickEvent(self, event):
        splitter = self.parentWidget()  # 获取父 QSplitter
        handle_index = splitter.indexOf(self)  # 获取分隔条的位置
        print(handle_index)
        if handle_index == 1:  # 左侧分隔条
            splitter.toggleWidget(0)  # 隐藏/显示左侧的 QWidget
        elif handle_index == 2:  # 右侧分隔条
            splitter.toggleWidget(2)  # 隐藏/显示右侧的 QWidget
        super().mouseDoubleClickEvent(event)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个水平的 CustomSplitter
        splitter = CustomSplitter(Qt.Horizontal)

        # 创建第一个 QWidget，设置背景颜色为红色
        widget1 = QWidget()
        widget1.setStyleSheet("background-color: red;")
        layout1 = QVBoxLayout(widget1)
        label1 = QLabel("Widget 1")
        layout1.addWidget(label1)
        widget1.setLayout(layout1)

        # 创建第二个 QWidget，设置背景颜色为绿色
        widget2 = QWidget()
        widget2.setStyleSheet("background-color: green;")
        layout2 = QVBoxLayout(widget2)
        label2 = QLabel("Widget 2")
        layout2.addWidget(label2)
        widget2.setLayout(layout2)

        # 创建第三个 QWidget，设置背景颜色为蓝色
        widget3 = QWidget()
        widget3.setStyleSheet("background-color: blue;")
        layout3 = QVBoxLayout(widget3)
        label3 = QLabel("Widget 3")
        layout3.addWidget(label3)
        widget3.setLayout(layout3)

        # 将 QWidget 添加到 CustomSplitter
        splitter.addWidget(widget1)
        splitter.addWidget(widget2)
        splitter.addWidget(widget3)

        # 设置 QSplitter 为 QMainWindow 的中心小部件
        self.setCentralWidget(splitter)

        # 设置窗口标题和大小
        self.setWindowTitle("QSplitter 示例 - 双击隐藏控件")
        self.resize(800, 600)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
