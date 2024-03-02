# # This Python file uses the following encoding: utf-8
import os
import logging
logger = logging.getLogger()

from PyQt5 import QtCore, QtGui, QtWidgets, uic

ON_ITEM = QtWidgets.QAbstractItemView.DropIndicatorPosition.OnItem
ABOVE_ITEM = QtWidgets.QAbstractItemView.DropIndicatorPosition.AboveItem
BELOW_ITEM = QtWidgets.QAbstractItemView.DropIndicatorPosition.BelowItem

class OutputTreeWidgetItem(QtWidgets.QTreeWidgetItem):
    def __init__(self, name, source_document=None, source_page_num=0, *args):
        super(OutputTreeWidgetItem, self).__init__(*args)
        if self.parent():
            self.setFlags(self.flags() & QtCore.Qt.ItemFlag.ItemIsDragEnabled |
                          ~QtCore.Qt.ItemFlag.ItemIsDropEnabled & ~QtCore.Qt.ItemFlag.ItemIsEditable)
        else:
            self.setFlags(self.flags() & ~QtCore.Qt.ItemFlag.ItemIsDragEnabled |
                          QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsEditable)
            
        self.setText(0, name)
        self.source_document = source_document
        if self.source_document:
            self.setText(1, self.source_document)
        self.source_page_num = source_page_num
        self.setExpanded(True)


    def get_output_page_num(self):
        if self.parent():
            return self.parent().getIndexOfChild()


    def get_source_document(self):
        return self.source_document


    def get_source_page_num(self):
        return self.source_page_num


class OutputTreeWidget(QtWidgets.QTreeWidget):
    def __init__(self, parent=None):
        super(OutputTreeWidget, self).__init__(parent=parent)
        self.setHeaderLabel("PDF Output")
        self.header().setDefaultAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.setDragDropMode(
            QtWidgets.QAbstractItemView.DragDropMode.InternalMove)

        self.setColumnCount(2)
        self.setHeaderLabels(["Document/Page", "Source Document"])
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        
        if parent:
            self.pdf_engine = parent.pdf_engine
        
        self.setEditTriggers(QtWidgets.QTreeWidget.DoubleClicked)
        self.itemDoubleClicked.connect(self.clear_text)
        self.add_undocumented()
        self.expandAll()

    
    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        item = self.itemAt(event.pos())
        if item is not None:
            column_to_ignore = 1  # Adjust this according to the column you want to ignore
            column = self.currentColumn()
            if column != column_to_ignore:
                # Perform the default behavior for editing the item
                super().mouseDoubleClickEvent(event)

        else:
            super().mouseDoubleClickEvent(event)

    
    def _get_items(self, parent_item=None):
        """Method to return generator of items in the tree.

        Returns:
            TYPE: Python Generator of items in tree.
        """
        root = self.invisibleRootItem()
        if parent_item:
            root = parent_item
        child_count = root.childCount()
        item_gen = (root.child(i) for i in range(child_count))
        return item_gen
    

    def find_doc_items(self, item_text):
        item_text = os.path.basename(item_text).split(".")[0]
        for item in self._get_items():
            if item.text(0) == item_text:
                return item

        return None

    
    def _reparent_item(self, item, new_parent):
        item = item.parent().takeChild(item.parent().indexOfChild(item))
        new_parent.addChild(item)


    def add_undocumented(self):
        self.undocumented_item = OutputTreeWidgetItem("__UNDOCUMENTED__")
        self.insertTopLevelItem(0, self.undocumented_item)


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

    
    def clear_setup(self):
        self.clear()
        self.add_undocumented()


    def clear_text(self, item, column):
        if item.source_page_num == 0:
            item.setText(0, "")


    def add_documents(self, documents):
        for document in documents:
            pages = self.pdf_engine.get_pdf_pages(document)
            if not pages:
                logger.info("Unable to open document because it's encrypted: " + document)
                continue

            doc_base = self.pdf_engine.get_doc_basename(document)
            doc_item = OutputTreeWidgetItem(doc_base, None, 0, self)
            for page_num in range(len(pages)):
                page_name = "{0}".format(page_num + 1)
                page_item = OutputTreeWidgetItem(
                    page_name,
                    document, # source document
                    page_num + 1, # source page number
                    doc_item
                )
                
            self.addTopLevelItem(doc_item)
            doc_item.setExpanded(True)


    def load_setup(self, pdf_dict):
        for doc_key in pdf_dict.keys():
            if doc_key in ["output_dir"]:
                continue
            
            doc_val = pdf_dict[doc_key]
            doc_base = os.path.basename(doc_key).split(".")[0]
            doc_item = OutputTreeWidgetItem(doc_base, None, 0, self)
            for page_key in sorted(doc_val.keys()):
                page_val = doc_val[page_key]
                source_page_num = next(iter(page_val))
                page_name = "{}".format(source_page_num)
                page_item = OutputTreeWidgetItem(
                    page_name, 
                    page_val[source_page_num], # source_document
                    int(source_page_num), # source_page_num
                    doc_item
                )

    
    def get_current_setup(self, output_dir):
        # return documents dict
        root = self.invisibleRootItem()
        document_dict = {"output_dir": output_dir}
        for doc_index in range(root.childCount()):
            page_dict = {}
            document_item = root.child(doc_index)
            if document_item.text(0) == "__UNDOCUMENTED__":
                continue

            page_count = document_item.childCount()
            if not page_count:
                continue

            for page_index in range(page_count):
                page_item = document_item.child(page_index)
                page_dict[page_index + 1] = {page_item.source_page_num: page_item.source_document}

            document_dict[document_item.text(0)] = page_dict
        
        return document_dict


    def add_new_document(self):
        name, ok = QtWidgets.QInputDialog().getText(
            self,
            "Please Specify the document name.",
            "Document name:"
        )
        if not ok:
            return

        selected_items = [item for item in self.selectedItems() if item.get_source_document()]
        doc_item = OutputTreeWidgetItem(name, None, 0, self)
        self.addTopLevelItem(doc_item)
        if selected_items:
            for item in selected_items:
                self._reparent_item(item, doc_item)


    def remove(self, items=None, bypass_confirm=False):
        if not items:
            items = self.selectedItems()

        if not bypass_confirm:
            result = QtWidgets.QMessageBox.question(self,    
                "Delete Items",
                "This will delete the document and move all its pages to UNDOCUMENTED.\n Are you sure you want to continue?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        else:
            result = True

        if result == QtWidgets.QMessageBox.Yes or result == True:
            for item in items:
                if item.get_source_document():
                    self._reparent_item(item, self.undocumented_item)
                
                else:
                    # Reparent pages of doc item to undocumented_item
                    child_items = self._get_items()
                    if list(child_items):
                        for item in child_items:
                            self._reparent_item(item, self.undocumented_item)

                    # delete doc item pages
                    self.invisibleRootItem().removeChild(item)
                    


 