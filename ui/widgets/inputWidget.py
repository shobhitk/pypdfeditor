# # This Python file uses the following encoding: utf-8
import os

from PyQt5 import QtCore, QtGui, QtWidgets, uic

class InputWidget(QtWidgets.QListWidget):
    files_added = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.file_list = []
        self.setAcceptDrops(True)
        self.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DragDrop)
        self.setSelectionMode(
            QtWidgets.QListWidget.SelectionMode.ExtendedSelection)

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
        if event.mimeData().hasUrls():
            event.accept()
        else:
            super().dragEnterEvent(event)
    def dragMoveEvent(self, event: QtGui.QDragMoveEvent) -> None:
        if event.mimeData().hasUrls():
            event.accept()
        else:
            super().dragMoveEvent(event)

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        if event.mimeData().hasUrls():
            event.accept()
            files = [str(url.toLocalFile()) for url in event.mimeData().urls() if not os.path.isdir(str(url.toLocalFile())) and str(url.toLocalFile()).endswith(".pdf")]
            self.add_files(files)

        else:
            super().dropEvent(event)

    def add_files(self, file_list) -> None:
        # TO DO: Maybe make this a helper function
        file_bases = [os.path.basename(f).split(".")[0]
                      for f in file_list]
        
        self.addItems(file_bases)

        self.file_list.extend(file_list)
        self.file_list = list(set(self.file_list))
        self.files_added.emit(file_list)