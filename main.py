# # This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PyQt6 import QtWidgets, uic

class OutputTreeWidgetItem(QtWidgets.QTreeWidgetItem):
    def __init__(self, parent=None):
        super(OutputTreeWidgetItem, self).__init__(parent=parent)

class OutputTreeWidget(QtWidgets.QTreeWidget):
    def __init__(self,parent=None):
        super(OutputTreeWidget, self).__init__(parent=parent)

class PyPdfEditor(QtWidgets.QDialog):
    def __init__(self):
        super(PyPdfEditor, self).__init__()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        uic.loadUi(path, self)
        self.output_tree_widget = QtWidgets.QTreeWidget()
        self.output_tree_frame.layout().addWidget(self.output_tree_widget, 0,0,0,0)

        



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = PyPdfEditor()
    widget.show()
    sys.exit(app.exec())