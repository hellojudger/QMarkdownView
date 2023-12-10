from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, QObject, Slot
from PySide6.QtWebChannel import QWebChannel
import markdown, base64, urllib.parse
from QMarkdownView.resources import qInitResources
import webbrowser, copy
from enum import Enum


__all__ = ["MarkdownView", "LinkMiddlewarePolicy"]


class LinkMiddlewarePolicy(Enum):
    OpenNewTab = 0
    Open = 1
    OpenNew = 2


class MarkdownView(QWebEngineView):
    extensions = None
    value = ""

    class LinkMiddleware(QObject):
        policy = None

        @Slot(str)
        def open_external(self, url):
            if url is None:
                return
            if self.policy == LinkMiddlewarePolicy.Open:
                webbrowser.open(url)
            if self.policy == LinkMiddlewarePolicy.OpenNew:
                webbrowser.open_new(url)
            else:
                webbrowser.open_new_tab(url)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.load(QUrl("qrc:/markdown_view/page.html"))
        self.channel = QWebChannel()
        self.page().setWebChannel(self.channel)
        self.link_middleware = self.LinkMiddleware()
        self.extensions = list()
        self.channel.registerObject("link_middleware", self.link_middleware)
        self.setLinkMiddlewarePolicy(LinkMiddlewarePolicy.OpenNewTab)

    def setValue(self, value: str):
        self.value = value
        extensions = self.getExtensions()
        body_html = markdown.markdown(value, extensions=extensions)
        bs64 = base64.b64encode(urllib.parse.quote(body_html).encode()).decode()
        script = "setValue({});".format(repr(bs64))
        self.page().runJavaScript(script)

    def getValue(self) -> str:
        return self.value

    def contextMenuEvent(self, arg__1) -> None:
        arg__1.ignore()

    def setLinkMiddlewarePolicy(self, policy) -> None:
        self.link_middleware.policy = policy

    def getLinkMiddlewarePolicy(self):
        return self.link_middleware.policy

    def setExtensions(self, extensions: list[str]) -> None:
        self.extensions = copy.deepcopy(extensions)

    def getExtensions(self) -> list[str]:
        return copy.deepcopy(self.extensions)

    def addExtension(self, extension: str) -> None:
        self.extensions.append(extension)
