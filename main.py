# # This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import pypdf

from PyQt6 import QtCore, QtWidgets, uic

class OutputTreeWidgetItem(QtWidgets.QTreeWidgetItem):
    def __init__(self, parent=None):
        super(OutputTreeWidgetItem, self).__init__(parent=parent)

class OutputTreeWidget(QtWidgets.QTreeWidget):
    def __init__(self,parent=None):
        super(OutputTreeWidget, self).__init__(parent=parent)
        self.setHeaderLabel("PDF Output")
        self.header().setDefaultAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

class InputListWidget(QtWidgets.QListWidget):
    files_added = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):
        super(InputListWidget, self).__init__(parent=parent)
        self.file_list = []
        self.setAcceptDrops(True)
        self.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DragDrop)
        self.setSelectionMode(QtWidgets.QListWidget.SelectionMode.ExtendedSelection)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            super(InputListWidget, self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            super(InputListWidget, self).dragMoveEvent(event)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
            self.add_files([str(url.toLocalFile()) for url in event.mimeData().urls()])
            
        else:
            super(InputListWidget, self).dropEvent(event)

    def add_files(self, file_list):
        self.file_list.extend(file_list)
        self.file_list = list(set(self.file_list))
        file_bases = [os.path.basename(f).split(".")[0] for f in self.file_list]
        self.addItems(file_bases)
        self.files_added.emit(self.file_list)


class PyPdfEditor(QtWidgets.QDialog):
    def __init__(self):
        super(PyPdfEditor, self).__init__()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        uic.loadUi(path, self)
        self.input_list_widget = InputListWidget()
        self.input_frame.layout().addWidget(self.input_list_widget)
        self.output_tree_widget = OutputTreeWidget()
        self.output_tree_frame.layout().addWidget(self.output_tree_widget, 0,0,0,0)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = PyPdfEditor()
    widget.show()
    sys.exit(app.exec())
