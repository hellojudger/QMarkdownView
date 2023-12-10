from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="QMarkdownView",
    version="0.2",
    author="xiezheyuan",
    author_email="xiezheyuan09@163.com",
    description="a package based on PySide6 designed to help you preview Markdown documents.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hellojudger/QMarkdownView/",
    packages=find_packages(),
    install_requires=['PySide6', 'markdown'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: X11 Applications :: Qt",
        "Topic :: Text Processing :: Markup :: Markdown"
    ],
)
