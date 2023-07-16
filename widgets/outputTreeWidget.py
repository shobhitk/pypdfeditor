# # This Python file uses the following encoding: utf-8
import os
import re
from pathlib import Path
import sys

from PyQt6 import QtCore, QtGui, QtWidgets, uic
import pypdf

ON_ITEM = QtWidgets.QAbstractItemView.DropIndicatorPosition.OnItem
ABOVE_ITEM = QtWidgets.QAbstractItemView.DropIndicatorPosition.AboveItem
BELOW_ITEM = QtWidgets.QAbstractItemView.DropIndicatorPosition.BelowItem

class OutputTreeWidgetItem(QtWidgets.QTreeWidgetItem):
    def __init__(self, text, document, page=0, *args):
        super(OutputTreeWidgetItem, self).__init__(*args)
        self.setText(0, text)
        if self.parent():
            self.setFlags(self.flags() & QtCore.Qt.ItemFlag.ItemIsDragEnabled |
                          ~QtCore.Qt.ItemFlag.ItemIsDropEnabled & ~QtCore.Qt.ItemFlag.ItemIsEditable)
        else:
            self.setFlags(self.flags() & ~QtCore.Qt.ItemFlag.ItemIsDragEnabled |
                          QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsEditable)
            
        self.document = document
        self.page = page
        self.setExpanded(True)


class OutputTreeWidget(QtWidgets.QTreeWidget):
    def __init__(self, parent=None):
        super(OutputTreeWidget, self).__init__(parent=parent)
        self.setHeaderLabel("PDF Output")
        self.header().setDefaultAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.setDragDropMode(
            QtWidgets.QAbstractItemView.DragDropMode.InternalMove)

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
        if not drag_item:
            return

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

    
    def add_documents(self, documents):
        for document in documents:

            pdf_read_obj = pypdf.PdfReader(document)
            pages = pdf_read_obj.pages

            # TO DO: Maybe make this a helper function
            doc_base = os.path.basename(document).split(".")[0]
            doc_item = OutputTreeWidgetItem(doc_base, document, self)
            for i in range(len(pages)):
                page_name = "{0}->{1}".format(i + 1, doc_base)
                page_item = OutputTreeWidgetItem(page_name, document, i + 1, doc_item)
            self.addTopLevelItem(doc_item)
            doc_item.setExpanded(True)

            




