# # This Python file uses the following encoding: utf-8
import os
from pathlib import Path
from pprint import pprint

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets, uic

from engine.pdfEngine import PdfEngine
from ui.widgets.inputWidget import InputWidget
from ui.widgets.outputTreeWidget import OutputTreeWidget, OutputTreeWidgetItem

class WebPage(QtWebEngineWidgets.QWebEnginePage):
    def javaScriptConsoleMessage(self, level, msg, line, sourceID):
        pass

class PyPdfEditor(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        uic.loadUi(path, self)
        self.pdf_engine = PdfEngine()
        self.input_list_widget = InputWidget(self)
        self.input_frame.layout().addWidget(self.input_list_widget)
        self.output_tree_widget = OutputTreeWidget(self)
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
        self.pdf_web_view = QtWebEngineWidgets.QWebEngineView()
        self.pdf_web_page = WebPage()
        self.pdf_web_view.setPage(self.pdf_web_page)
        self.pdf_web_view.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        self.pdf_web_view.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PdfViewerEnabled, True)
        self.pdf_view_frame.layout().addWidget(self.pdf_web_view)
        self.pdf_view_frame.setMinimumWidth(500)
        self.make_connections()

    
    def make_connections(self):
        self.input_list_widget.files_added.connect(self.populate)
        self.output_tree_widget.page_selected.connect(self.show_page)
        self.generate_button.clicked.connect(self.generate_documents)


    def populate(self, files):
        self.output_tree_widget.add_documents(files)

    
    def show_page(self, document, page):
        self.pdf_web_view.load(QtCore.QUrl(self.pdf_engine.get_pdf_url(document, page)))

    
    def generate_documents(self):
        output_dir = self.output_line_edit.text()
        return_dict = self.output_tree_widget.return_documents_dict(output_dir)
        pprint(return_dict)





    






