import pypdf
import webbrowser

class PdfEngine():
    def __init__(self):
        pass
    
    def get_pdf_pages(self, document):
        pdf_read_obj = pypdf.PdfReader(document)
        pages = pdf_read_obj.pages
        return pages
    
    def write_pdf(self, pdf_dict):
        pdf_write_obj = pypdf.PdfWriter()
        pass

    def get_pdf_url(self, pdf_file, page=1):
        # <A HREF="file:////www.example.com/myfile.pdf#page=4">
        return "file:////{0}#page={1}".format(pdf_file, page)
    




    


        


