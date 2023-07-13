# # This Python file uses the following encoding: utf-8
import os
import re
from pathlib import Path
import sys
from PyQt6.QtWidgets import QTreeWidgetItem
import pypdf

from PyQt6 import QtCore, QtGui, QtWidgets, uic

ON_ITEM = QtWidgets.QAbstractItemView.DropIndicatorPosition.OnItem
ABOVE_ITEM = QtWidgets.QAbstractItemView.DropIndicatorPosition.AboveItem
BELOW_ITEM = QtWidgets.QAbstractItemView.DropIndicatorPosition.BelowItem

class OutputTreeWidgetItem(QtWidgets.QTreeWidgetItem):
    def __init__(self, text, *args):
        super(OutputTreeWidgetItem, self).__init__(*args)
        self.setText(0, text)
        if self.parent():
            self.setFlags(self.flags() & QtCore.Qt.ItemFlag.ItemIsDragEnabled |
                          ~QtCore.Qt.ItemFlag.ItemIsDropEnabled & ~QtCore.Qt.ItemFlag.ItemIsEditable)
        else:
            self.setFlags(self.flags() & ~QtCore.Qt.ItemFlag.ItemIsDragEnabled |
                          QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsEditable)
        

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

    def check_position(self, pos, rect):
        indicator = QtWidgets.QAbstractItemView.DropIndicatorPosition.OnViewport
        if not self.dragDropOverwriteMode():
            margin = int(max(2, min(rect.height() / 5.5, 12)))
            if pos.y() - rect.top() < margin:
                indicator = ABOVE_ITEM
            elif rect.bottom() - pos.y() < margin:
                indicator = BELOW_ITEM
            elif rect.contains(pos, True):
                indicator = ON_ITEM
        else:
            touching = rect.adjust(-1, -1, 1, 1)
            if touching.contains(pos.toPoint(), False):
                indicator = ON_ITEM
        return indicator

    
    def dragMoveEvent(self, event: QtGui.QDragMoveEvent) -> None:
        drag_index = self.indexAt(event.position().toPoint())
        drag_item = self.itemFromIndex(drag_index)
        drag_position = self.check_position(
                event.position().toPoint(),
                self.visualItemRect(self.itemFromIndex(drag_index))
                )

        if (drag_position == ON_ITEM and drag_item.parent()) or \
            (drag_position in [ABOVE_ITEM, BELOW_ITEM] and not drag_item.parent()):
            event.ignore()

        else:
            super().dragMoveEvent(event)

    
    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        # Chech what's the drop-destination.
        # Accept if Drop destination is a document.
        # Reject if Drop destination is a page.
        drop_index = self.indexAt(event.position().toPoint())
        drop_target_item = self.itemFromIndex(drop_index)
        if not drop_target_item:
            return
        
        drop_position = self.check_position(
                event.position().toPoint(),
                self.visualItemRect(drop_target_item)
                )
        
        if (drop_position == ON_ITEM and drop_target_item.parent()) or \
            (drop_position in [ABOVE_ITEM, BELOW_ITEM] and not drop_target_item.parent()):
            event.ignore()

        else:
            super().dropEvent(event)


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
