# # This Python file uses the following encoding: utf-8
import os
from pathlib import Path
from pprint import pprint
import logging
logger = logging.getLogger()

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets, uic

from ui.widgets.inputWidget import InputWidget
from ui.widgets.outputTreeWidget import OutputTreeWidget, OutputTreeWidgetItem
from engine.pdfEngine import PdfEngine

os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--enable-logging --log-level=3"

default_html = """
<html>
    <head>
        <style>
            body {
                background-color: #404040;
            }
        </style >
    </head >
</html>
"""     

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
        self.pdf_web_view.setHtml(default_html)  
        self.pdf_web_view.show()
        self.pdf_web_view.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        self.pdf_web_view.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PdfViewerEnabled, True)
        self.pdf_view_frame.layout().addWidget(self.pdf_web_view)
        self.pdf_view_frame.setMinimumWidth(500)
        self.output_line_edit.setText(os.path.expanduser("~\\Documents\\"))
        self.make_connections()

    
    def make_connections(self):
        self.action_new.triggered.connect(self.create_new_setup)
        self.action_open.triggered.connect(self.open_setup)
        self.action_save.triggered.connect(self.save_setup)

        self.action_add_pdfs.triggered.connect(self.add_pdfs)
        self.action_remove_pdfs.triggered.connect(self.remove_pdfs)

        self.action_merge_pdfs.triggered.connect(self.merge_pdfs)
        self.action_split_pdfs.triggered.connect(self.split_pdfs)
        
        # self.action_undo.triggered.connect(self.undo_operation)
        # self.action_redo.triggered.connect(self.redo_operation)

        self.action_new_document.triggered.connect(self.output_tree_widget.add_new_document)
        self.action_remove.triggered.connect(self.output_tree_widget.remove)

        self.input_list_widget.files_added.connect(self.output_tree_widget.add_documents)
        self.input_list_widget.document_selected.connect(self.show_document)
        self.browse_button.clicked.connect(self.set_output_folder)
        self.generate_button.clicked.connect(self.generate_documents)
        self.close_button.clicked.connect(self.close)

    
    def set_output_folder(self):
        result = QtWidgets.QFileDialog.getExistingDirectory(
            None, 
            caption='Select Directory',
            options=QtWidgets.QFileDialog.ShowDirsOnly)

        self.output_line_edit.setText(result)


    def get_output_folder(self):
        return self.output_line_edit.text()


    def create_new_setup(self):
        if self.output_tree_widget.has_items():
            window_title = "Save File?"
            confirm_text = "Do you want to save the current setup?"
            result = self.show_confirm_dialog(window_title, confirm_text)
            if result:
                self.save_setup()

        self.input_list_widget.clear()
        self.output_tree_widget.clear()
        self.output_tree_widget.add_undocumented()


    def open_setup(self):
        setup_file, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Open Setup file", "", "JSON (*.json)")

        if setup_file:
            pdf_dict = self.pdf_engine.load_setup(setup_file)
            input_files = self.pdf_engine.extract_input_files(pdf_dict)
            self.input_list_widget.add_files(input_files, emit=False)
            self.output_tree_widget.load_setup(pdf_dict)

        self.status_bar.showMessage("Setup Loaded.")
        

    def save_setup(self):
        data = self.output_tree_widget.get_current_setup(
            self.output_line_edit.text()
        )
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        file_dialog.setNameFilter("JSON Files (*.json)")
        if file_dialog.exec_() == QtWidgets.QDialog.Accepted:
            file_name = file_dialog.selectedFiles()[0]
            self.pdf_engine.save_setup(data, file_name)

        self.status_bar.showMessage("PDF Setup Changed.")

    
    def add_pdfs(self):
        file_names, _ = QtWidgets.QFileDialog.getOpenFileNames(
            None, "Open files", "", "PDF (*.pdf)")
        self.input_list_widget.add_files(file_names)
        self.status_bar.showMessage("Files Added.")


    def remove_pdfs(self):
        selected_pdfs = self.input_list_widget.selectedItems()
        for item in selected_pdfs:
            item_index = self.input_list_widget.row(item)
            removed_item = self.input_list_widget.takeItem(item_index)
            # clear all pages belonging to that document from the output_tree_widget
            item = self.output_tree_widget.find_doc_items(removed_item.text())
            if item:
                self.output_tree_widget.remove([item], bypass_confirm=True)

        self.clear_document_from_view()        
        self.status_bar.showMessage("Files Removed.")


    def merge_pdfs(self):
        document_list = self.input_list_widget.get_document_list()
        output_folder = self.get_output_folder()
        merge_dict = self.pdf_engine.generate_merged_dict(document_list, output_folder)
        self.output_tree_widget.clear_setup()
        self.output_tree_widget.load_setup(merge_dict)


    def split_pdfs(self):
        document_list = self.input_list_widget.get_document_list()
        output_folder = self.get_output_folder()
        split_dict = self.pdf_engine.generate_split_dict(document_list, output_folder)
        self.output_tree_widget.clear_setup()
        self.output_tree_widget.load_setup(split_dict)


    # def undo_operation(self):
    #     pass


    # def redo_operation(self):
    #     pass
        
    
    def clear_document_from_view(self):
        self.pdf_web_view.setHtml(default_html)  

    
    def show_document(self, document):
        url_str = self.pdf_engine.get_pdf_url(document)
        self.status_bar.showMessage(url_str)
        self.pdf_web_view.load(QtCore.QUrl(url_str))


    def show_success_dialog(self, result):
        msg = QtWidgets.QMessageBox(self)
        msg.setMinimumHeight(30)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("These PDF files were successfully generated:\n" + "\n".join(result))
        msg.setWindowTitle("Success!")
        msg.show()


    def show_confirm_dialog(self, window_title, confirm_text):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setMinimumHeight(30)
        msg.setWindowTitle(window_title)
        msg.setText(confirm_text)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        result = msg.exec_()
        return result == QtWidgets.QMessageBox.Ok


    def confirm_output(self, output_dict):
        output_dir = output_dict['output_dir']
        files_exist = []
        for doc_key in output_dict.keys():
            out_file = os.path.join(output_dir, doc_key + ".pdf")
            if os.path.exists(out_file):
                files_exist.append(out_file)
        
        if files_exist:
            window_title = "Overwrite Files?"
            confirm_text = "These files already exist,\n" + \
                            "\n".join(files_exist) + \
                            "\nAre you sure you want to continue?"
            return self.show_confirm_dialog(window_title, confirm_text)

        return True


    def generate_documents(self):
        output_dir = self.output_line_edit.text()
        output_dict = self.output_tree_widget.get_current_setup(output_dir)
        confirm = self.confirm_output(output_dict)
        if not confirm:
            return

        result = self.pdf_engine.generate_pdfs(output_dict)
        if result:
            self.show_success_dialog(result)

