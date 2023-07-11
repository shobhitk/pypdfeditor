# # This Python file uses the following encoding: utf-8
import os
import re
from pathlib import Path
import sys
import pypdf

from PyQt6 import QtCore, QtGui, QtWidgets, uic

class OutputTreeWidgetItem(QtWidgets.QTreeWidgetItem):
    def __init__(self, text, *args):
        super(OutputTreeWidgetItem, self).__init__(*args)
        self.setText(0, text)
        if str(self.parent()) == "OutputTreeWidget":
            self.setFlags(QtCore.Qt.ItemIsDragEnabled)
        

class OutputTreeWidget(QtWidgets.QTreeWidget):
    def __init__(self, parent=None):
        super(OutputTreeWidget, self).__init__(parent=parent)
        self.setHeaderLabel("PDF Output")
        self.header().setDefaultAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.InternalMove)
    
    def __str__(self) -> str:
        return "OutputTreeWidget"

    def get_mime_data(self, event):
        data = event.mimeData()
        source_item = QtGui.QStandardItemModel()
        source_item.dropMimeData(
            data, QtCore.Qt.DropAction.MoveAction, 0, 0, QtCore.QModelIndex())
        return source_item.item(0, 0).text()


    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
        data = self.get_mime_data(event)
        # Chech what's being moved.
        # Reject if Document is being moved.
        # Accept if Page is being moved.
        if re.match(r"^[a-zA-Z]+[a-zA-Z0-9_\-\ ]*", data):
            return

        return super().dragEnterEvent(event)

    
    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        data = self.get_mime_data(event)
        # Chech what's being dropped.
        # Reject if Document is being dropped.
        # Accept if Page is being dropped.
        if re.match(r"^[a-zA-Z]+[a-zA-Z0-9_\-\ ]*", data):
            return

        # A page can only be dropped under a document.
        # check if item has a parent.
        # If it does, then reject
        # Else Accept.
        drop_index = self.indexAt(event.position().toPoint())
        print('Item:', self.itemFromIndex(drop_index).text(0))
        if self.itemFromIndex(drop_index).parent():
            print('Parent:', self.itemFromIndex(drop_index).parent().text(0))
            if self.itemFromIndex(drop_index).parent().parent():
                print('Grandparent:', self.itemFromIndex(drop_index).parent().text(0))

        if not drop_index.parent().isValid():
            return super().dropEvent(event)


class InputListWidget(QtWidgets.QListWidget):
    files_added = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.file_list = []
        self.setAcceptDrops(True)
        self.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DragDrop)
        self.setSelectionMode(QtWidgets.QListWidget.SelectionMode.ExtendedSelection)

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
            self.add_files([str(url.toLocalFile()) for url in event.mimeData().urls()])
            
        else:
            super().dropEvent(event)

    def add_files(self, file_list) -> None:
        self.file_list.extend(file_list)
        self.file_list = list(set(self.file_list))
        file_bases = [os.path.basename(f).split(".")[0] for f in self.file_list]
        self.addItems(file_bases)
        self.files_added.emit(self.file_list)


class PyPdfEditor(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        path = os.fspath(Path(__file__).resolve().parent / "ui/form.ui")
        uic.loadUi(path, self)
        self.input_list_widget = InputListWidget()
        self.input_frame.layout().addWidget(self.input_list_widget)
        self.output_tree_widget = OutputTreeWidget()
        test_item1 = OutputTreeWidgetItem("Doc1", self.output_tree_widget)
        test_item1_1 = OutputTreeWidgetItem("1", test_item1)
        test_item1_2 = OutputTreeWidgetItem("2", test_item1)
        test_item2 = OutputTreeWidgetItem("Doc2", self.output_tree_widget)
        test_item2_1 = OutputTreeWidgetItem("3", test_item2)
        test_item2_2 = OutputTreeWidgetItem("4", test_item2)
        self.output_tree_widget.addTopLevelItems([test_item1, test_item2])
        self.output_tree_frame.layout().addWidget(self.output_tree_widget, 0,0,0,0)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = PyPdfEditor()
    widget.show()
    sys.exit(app.exec())
