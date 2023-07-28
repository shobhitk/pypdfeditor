import sys
from PyQt5 import QtWidgets
from ui.main import PyPdfEditor

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = PyPdfEditor()
    widget.show()
    sys.exit(app.exec())
