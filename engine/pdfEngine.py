import os
import pypdf
from pprint import pprint

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
    
    def generate_pdfs(self, pdf_dict):
        output_dir = "C:\\GitHub\\"
        # output_dir = pdf_dict['output_dir']
        for doc_key, doc_val in pdf_dict.items():
            pdf_write_obj = pypdf.PdfWriter()
            if doc_key == "output_dir":
                continue
            
            for index in range(len(doc_val)):
                input_page = doc_val[index][0]
                input_doc = open(doc_val[index][1], "rb")
                pdf_write_obj.append(
                    fileobj=input_doc, pages=(input_page-1, input_page ))
            
            output = open(os.path.join(output_dir, doc_key + ".pdf"), "wb")
            pdf_write_obj.write(output)
            pdf_write_obj.close()
            output.close()


# test
# test_pdf = {'ANNEXURE-E filled': [(1, 'C:/Users/shobh/Documents/ANNEXURE-E filled.pdf'),
#                                   (1, 'C:/Users/shobh/Documents/Accounts Overview.pdf')],
#             'output_dir': "C:\\GitHub\\"}
# test_pdf_engine = PdfEngine()
# test_pdf_engine.generate_pdfs(test_pdf)




    


        


