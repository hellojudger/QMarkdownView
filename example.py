from QMarkdownView import MarkdownView, LinkMiddlewarePolicy
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.widget = MarkdownView()
        self.widget.setExtensions(["markdown.extensions.tables", "markdown.extensions.extra"])
        self.widget.setLinkMiddlewarePolicy(LinkMiddlewarePolicy.OpenNew)
        self.btn = QPushButton("Load")
        self.lay = QVBoxLayout()
        self.lay.addWidget(self.widget)
        self.lay.addWidget(self.btn)
        self.btn.clicked.connect(lambda x : self.widget.setValue(open("README.md", "r", encoding="utf-8").read()))
        self.setLayout(self.lay)

app = QApplication([])
win = Window()
win.show()
app.exec()