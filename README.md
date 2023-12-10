# QMarkdownView

## Description

QMarkdownView is a package based on PySide6 designed to help you preview Markdown documents.

Markdown by default supports code highlighting and LaTex mathematical formulas.

## How to use

Firstly, you need to introduce the QMarkdownView library.

```python
from QMarkdownView import MarkdownView, LinkMiddlewarePolicy
```

You can use the component class `MarkdownView`` we provide.

```python
widget = MarkdownView()
```
`MarkdownView` inherits from `QWebEngineView`.

You can change the Markdown rendering plugin through the `setExtension` member function. The markup rendering engine for this function library is `python-markdown`.

```python
widget.setExtensions(["markdown.extensions.tables", "markdown.extensions.extra"])
```

You can modify Markdown text through the setValue member function.

```python
widget.setValue("# Hello world!")
```

Warning: You need to call this function after the component is loaded.

