# # This Python file uses the following encoding: utf-8
import os
from pathlib import Path
from pprint import pprint

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets, uic

from engine.pdfEngine import PdfEngine
from ui.widgets.inputWidget import InputWidget
from ui.widgets.outputTreeWidget import OutputTreeWidget, OutputTreeWidgetItem

os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--enable-logging --log-level=3"


class WebPage(QtWebEngineWidgets.QWebEnginePage):
    def javaScriptConsoleMessage(self, *args):
        pass

class PyPdfEditor(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        uic.loadUi(path, self)
        self.setCentralWidget(self.main_frame)
        self.centralWidget().layout().setContentsMargins(3,3,3,3)
        # self.central_widget.layout().setContentsMargins(0,0,0,0)
        # self.central_widget.layout().addWidget(self.main_frame)
        self.top_splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.top_splitter.addWidget(self.input_frame)
        self.top_splitter.addWidget(self.output_frame)
        self.top_frame.layout().addWidget(self.top_splitter)
        self.pdf_engine = PdfEngine()
        self.input_list_widget = InputWidget(self)
        self.input_frame.layout().addWidget(self.input_list_widget)
        self.output_tree_widget = OutputTreeWidget(self)
        self.output_frame.layout().addWidget(self.output_tree_widget, 0,0,0,0)
        self.pdf_web_view = QtWebEngineWidgets.QWebEngineView()
        self.pdf_web_page = WebPage()
        self.pdf_web_view.setPage(self.pdf_web_page)
        self.pdf_web_view.setHtml("""
<html>
    <head>
        <style>
            body {
                background-color: #404040;
            }
        </style >
    </head >
</html>
""")
        
        self.pdf_web_view.show()
        self.pdf_web_view.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        self.pdf_web_view.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PdfViewerEnabled, True)
        self.pdf_view_frame.layout().addWidget(self.pdf_web_view)
        self.pdf_view_frame.setMinimumWidth(500)
        self.make_connections()

    
    def make_connections(self):
        self.input_list_widget.files_added.connect(self.populate_output)
        self.action_add_pdfs.triggered.connect(self.add_docs)
        self.output_tree_widget.page_selected.connect(self.show_page)
        self.browse_button.clicked.connect(self.set_output_folder)
        self.generate_button.clicked.connect(self.generate_documents)
        self.close_button.clicked.connect(self.close)

    
    def set_output_folder(self):
        result = QtWidgets.QFileDialog.getExistingDirectory(
            None, 
            caption='Select Directory',
            options=QtWidgets.QFileDialog.ShowDirsOnly)

        self.output_line_edit.setText(result)


    def open_setup(self):
        setup_file, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Open Setup file", "", "JSON (*.json)")
        self.populate_ui_from_file(setup_file)

    
    def add_docs(self):
        file_names, _ = QtWidgets.QFileDialog.getOpenFileNames(
            None, "Open files", "", "PDF (*.pdf)")
        self.input_list_widget.add_files(file_names)

    def populate_ui_from_file(self, setup_file):
        pass


    def populate_output(self, files):
        self.output_tree_widget.add_documents(files)

    
    def show_page(self, document, page):
        url_str = self.pdf_engine.get_pdf_url(document, page)
        self.pdf_web_view.load(QtCore.QUrl(url_str))


    def show_success_dialog(self, result):
        msg = QtWidgets.QMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("These PDF files were successfully generated:\n", "\n".join(result))
        msg.setWindowTitle("Success!")
        msg.show()


    def show_confirm_dialog(self, files_exist):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        # msg.setText("Overwrite Files?")
        msg.setText("These files already exist,\n" +
                               "\n".join(files_exist) +
                               "\nAre you sure you want to continue?")
        msg.setWindowTitle("Overwrite Files?")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        result = msg.exec_()
        if result == QtWidgets.QMessageBox.Ok:
            return True
        return False


    def confirm_output(self, output_dict):
        output_dir = output_dict['output_dir']
        files_exist = []
        for doc_key in output_dict.keys():
            out_file = os.path.join(output_dir, doc_key + ".pdf")
            if os.path.exists(out_file):
                files_exist.append(out_file)
        
        if files_exist:
            return self.show_confirm_dialog(files_exist)

        return True


    
    def generate_documents(self):
        output_dir = self.output_line_edit.text()
        output_dict = self.output_tree_widget.return_documents_dict(output_dir)
        # print(output_dict)
        confirm = self.confirm_output(output_dict)
        if not confirm:
            return

        result = self.pdf_engine.generate_pdfs(output_dict)
        if result:
            self.show_success_dialog(result)




    






