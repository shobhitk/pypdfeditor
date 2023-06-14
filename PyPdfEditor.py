import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import traceback

class PyPdfEditor(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setLayout(QtWidgets.QGridLayout())
        self.file_browser = QtWidgets.QListWidget()
        self.output_tree_widget = QtWidgets.QTreeWidget()
        self.add_doc_button = QtWidgets.QPushButton()
        self.remove_doc_button = 


        


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = PyPdfEditor()
    w.show()
    sys.exit(app.exec_())
