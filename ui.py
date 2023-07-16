# # This Python file uses the following encoding: utf-8
import os
import re
from pathlib import Path
import sys

from PyQt6 import QtCore, QtGui, QtWidgets, uic
import pypdf

from widgets.inputWidget import InputWidget
from widgets.outputTreeWidget import OutputTreeWidget, OutputTreeWidgetItem

class PyPdfEditor(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        path = os.fspath(Path(__file__).resolve().parent / "ui/form.ui")
        uic.loadUi(path, self)
        self.input_list_widget = InputWidget()
        self.input_frame.layout().addWidget(self.input_list_widget)
        self.output_tree_widget = OutputTreeWidget()
        # TEST CONDITION ################### ####################################
        #################################### ####################################
        # test_item1 = OutputTreeWidgetItem("Doc1", self.output_tree_widget)
        # test_item1_1 = OutputTreeWidgetItem("1", test_item1)
        # test_item1_2 = OutputTreeWidgetItem("2", test_item1)
        # test_item2 = OutputTreeWidgetItem("Doc2", self.output_tree_widget)
        # test_item2_1 = OutputTreeWidgetItem("3", test_item2)
        # test_item2_2 = OutputTreeWidgetItem("4", test_item2)
        # self.output_tree_widget.addTopLevelItems([test_item1, test_item2])
        ################################### ###################################
        ################################### ###################################
        self.output_tree_frame.layout().addWidget(self.output_tree_widget, 0,0,0,0)
        self.make_connections()

    
    def make_connections(self):
        self.input_list_widget.files_added.connect(self.populate)


    def populate(self, files):
        self.output_tree_widget.add_documents(files)




    






