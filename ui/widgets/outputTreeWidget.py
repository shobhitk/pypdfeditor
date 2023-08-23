# # This Python file uses the following encoding: utf-8
import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic

ON_ITEM = QtWidgets.QAbstractItemView.DropIndicatorPosition.OnItem
ABOVE_ITEM = QtWidgets.QAbstractItemView.DropIndicatorPosition.AboveItem
BELOW_ITEM = QtWidgets.QAbstractItemView.DropIndicatorPosition.BelowItem

class OutputTreeWidgetItem(QtWidgets.QTreeWidgetItem):
    def __init__(self, text, document=None, page=0, *args):
        super(OutputTreeWidgetItem, self).__init__(*args)
        if self.parent():
            self.setFlags(self.flags() & QtCore.Qt.ItemFlag.ItemIsDragEnabled |
                          ~QtCore.Qt.ItemFlag.ItemIsDropEnabled & ~QtCore.Qt.ItemFlag.ItemIsEditable)
        else:
            self.setFlags(self.flags() & ~QtCore.Qt.ItemFlag.ItemIsDragEnabled |
                          QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsEditable)
            
        self.setText(0, text)
        self.document = document
        self.page = page
        self.setExpanded(True)


class OutputTreeWidget(QtWidgets.QTreeWidget):
    page_selected = QtCore.pyqtSignal(str, int)

    def __init__(self, parent=None):
        super(OutputTreeWidget, self).__init__(parent=parent)
        self.setHeaderLabel("PDF Output")
        self.header().setDefaultAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.setDragDropMode(
            QtWidgets.QAbstractItemView.DragDropMode.InternalMove)
        
        if parent:
            self.pdf_engine = parent.pdf_engine
        
        self.itemDoubleClicked.connect(self.clear_text)
        self.itemClicked.connect(self.emit_page_selected)

    def has_items(self):
        return self.topLevelItemCount() > 0


    def get_mime_data(self, event):
        data = event.mimeData()
        source_item = QtGui.QStandardItemModel()
        source_item.dropMimeData(
            data, QtCore.Qt.DropAction.MoveAction, 0, 0, QtCore.QModelIndex())
        return source_item.item(0, 0).text()

    
    def set_stylesheet_for_position(self, position):
        if position == ON_ITEM:
            self.setStyleSheet("""QTreeView::item:hover { background-color: #656565;}""")
        else:
            self.setStyleSheet("""QTreeView::item:hover { background-color: None;}""")


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
            if touching.contains(pos, False):
                indicator = ON_ITEM
        return indicator


    def dragMoveEvent(self, event: QtGui.QDragMoveEvent) -> None:
        drag_index = self.indexAt(event.pos())
        drag_item = self.itemFromIndex(drag_index)
        if not drag_item:
            return

        drag_position = self.check_position(
            event.pos(),
            self.visualItemRect(self.itemFromIndex(drag_index))
        )

        self.set_stylesheet_for_position(drag_position)

        if (drag_position == ON_ITEM and drag_item.parent()) or \
                (drag_position in [ABOVE_ITEM, BELOW_ITEM] and not drag_item.parent()):
            event.ignore()

        else:
            super().dragMoveEvent(event)


    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        # Chech what's the drop-destination.
        # Accept if Drop destination is a document.
        # Reject if Drop destination is a page.
        drop_index = self.indexAt(event.pos())
        drop_target_item = self.itemFromIndex(drop_index)
        if not drop_target_item:
            return

        drop_position = self.check_position(
            event.pos(),
            self.visualItemRect(drop_target_item)
        )

        self.set_stylesheet_for_position(drop_position)

        if (drop_position == ON_ITEM and drop_target_item.parent()) or \
                (drop_position in [ABOVE_ITEM, BELOW_ITEM] and not drop_target_item.parent()):
            event.ignore()

        else:
            super().dropEvent(event)



    def emit_page_selected(self, item):
        self.page_selected.emit(item.document, item.page)


    def clear_text(self, item):
        if item.page == 0:
            item.setText(0, "")

    
    def clear_document(self, path):
        root = self.invisibleRootItem()
        for doc_index in range(root.childCount()):
            document_item = root.child(doc_index)
            page_count = document_item.childCount()

            if not page_count:
                continue

            for page_index in range(page_count):
                page_item = document_item.child(page_index)
                if page_item.document == path:
                    document_item.removeChild(page_item)


    def add_documents(self, documents):
        for document in documents:
            pages = self.pdf_engine.get_pdf_pages(document)

            doc_base = os.path.basename(document).split(".")[0]
            doc_item = OutputTreeWidgetItem(doc_base, "", 0, self)
            for page_num in range(len(pages)):
                page_name = "{0}->{1}".format(page_num + 1, doc_base)
                page_item = OutputTreeWidgetItem(
                    page_name, document, page_num + 1, doc_item)
            self.addTopLevelItem(doc_item)
            doc_item.setExpanded(True)


    def load_setup_output(self, pdf_dict):
        for doc_key, doc_val in pdf_dict.items():
            if doc_key == "output_dir":
                continue

            doc_base = os.path.basename(doc_key).split(".")[0]
            doc_item = OutputTreeWidgetItem(doc_base, "", 0, self)

            for page_key in sorted(doc_val.keys()):
                page_val = doc_val[page_key]
                page_name = "{0}->{1}".format(next(iter(page_val)) + 1, doc_base)
                page_item
    
    def return_documents_dict(self, output_dir):
        # return documents dict
        root = self.invisibleRootItem()
        document_dict = {"output_dir": output_dir}
        for doc_index in range(root.childCount()):
            page_dict = {}
            document_item = root.child(doc_index)
            page_count = document_item.childCount()
            if not page_count:
                continue

            for page_index in range(page_count):
                page_item = document_item.child(page_index)
                page_dict[page_index + 1] = {page_item.page: page_item.document}

            document_dict[document_item.text(0)] = page_dict
        
        return document_dict

    def add_new_document(self):
        pass


    def remove_document(self):
        pass


# TEST CASE
# class TestWindow(QtWidgets.QDialog):
#     def __init__(self):
#         super().__init__()
#         self.setLayout(QtWidgets.QvBoxLayout())
#         self.output_tree_widget = OutputTreeWidget()
#         test_item1 = OutputTreeWidgetItem(
#             "Doc1", "Doc1", 0,  self.output_tree_widget)
#         test_item1_1 = OutputTreeWidgetItem(
#             "page1-doc1", "page1", 1, test_item1)
#         test_item1_2 = OutputTreeWidgetItem(
#             "page2-doc1", "page2", 0, test_item1)
#         test_item2 = OutputTreeWidgetItem("Doc2", "Doc2", 0, self.output_tree_widget)
#         test_item2_1 = OutputTreeWidgetItem(
#             "page1-doc2", "page1", 0, test_item2)
#         test_item2_2 = OutputTreeWidgetItem(
#             "page2-doc2", "page2", 0, test_item2)
#         self.output_tree_widget.addTopLevelItems([test_item1, test_item2])
#         self.layout().addWidget(self.output_tree_widget)
#         self.gen_button = QtWidgets.QPushButton("Gen")
#         self.gen_button.clicked.connect(self.print_test)
#         self.layout().addWidget(self.gen_button)
#         self.show()

#     def print_test(self):
#         from pprint import pprint
#         pprint(self.output_tree_widget.return_documents_dict())


# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#     widget = TestWindow()
#     widget.show()
#     sys.exit(app.exec())
