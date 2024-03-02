# # This Python file uses the following encoding: utf-8
import os
import logging
logger = logging.getLogger()


from PyQt5 import QtCore, QtGui, QtWidgets, uic

class InputWidget(QtWidgets.QListWidget):
    files_added = QtCore.pyqtSignal(list)
    document_selected = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.document_list = []
        self.setAcceptDrops(True)
        self.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DropOnly)
        self.setSelectionMode(
            QtWidgets.QListWidget.SelectionMode.ExtendedSelection)
        self.itemClicked.connect(self.emit_document_selected)


    def get_document_list(self):
        return self.document_list


    def dragEnterEvent(self, event: QtGui.QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            super().dragEnterEvent(event)

    def dragMoveEvent(self, event: QtGui.QDragMoveEvent):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            super().dragMoveEvent(event)


    def dropEvent(self, event: QtGui.QDropEvent):
        if event.mimeData().hasUrls():
            event.accept()
            files = [str(url.toLocalFile()) for url in event.mimeData().urls() if not os.path.isdir(str(url.toLocalFile())) and str(url.toLocalFile()).endswith(".pdf")]
            self.add_files(files)

        else:
            super().dropEvent(event)


    def add_files(self, document_list, emit=True):
        # TO DO: Maybe make this a helper function
        for f in document_list:
            self.addItem(f)

        self.document_list.extend(document_list)
        self.document_list = list(set(self.document_list))
        if emit:
            self.files_added.emit(document_list)

    
    def emit_document_selected(self, item):
        self.document_selected.emit(item.text())
