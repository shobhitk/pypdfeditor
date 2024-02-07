import os
import json
import pypdf
from pprint import pprint

class PdfEngine():
    def __init__(self):
        pass

    def get_doc_basename(self, document):
        return os.path.basename(document).split(".")[0]
    
    def get_pdf_pages(self, document):
        pdf_read_obj = pypdf.PdfReader(document)
        if pdf_read_obj.is_encrypted:
            pdf_read_obj.decrypt("AES-256")
        pages = pdf_read_obj.pages
        return pages


    def get_pdf_url(self, pdf_file):
        # <A HREF="file:////www.example.com/myfile.pdf#page=4">
        return "file:////{0}".format(pdf_file)

    
    def load_setup(self, load_file):
        with open(load_file, "r", encoding="utf-8") as f:
            pdf_dict = json.load(f)
        
        return pdf_dict


    def save_setup(self, data, save_file):
        if not os.path.isdir(os.path.dirname(save_file)):
            os.makedirs(os.path.dirname(save_file))
        with open(save_file, "w+") as f:
            json.dump(data, f, indent=4)

# {
#     "output_folder": "output",
#     "doc_1.pdf": {
#         "1": {"1": "a/b/doc_1.pdf"},
#         "2": {"1": "b/c/doc_2.pdf"}
#     },
#     "doc_2.pdf": {
#         "1": {"3": "a/b/doc_1.pdf"},
#         "2": {"4": "b/c/doc_2.pdf"}
#     }
# }

    def generate_merged_dict(self, document_list, output_folder):
        merged_doc_name = self.get_doc_basename(document_list[0]) + "_MERGED"
        merge_dict = {
            "output_folder": output_folder,
            merged_doc_name: {}
        }
        output_page_number = 1
        for document in document_list:
            pages = self.get_pdf_pages(document)
            for page_num in range(len(pages)):
                merge_dict[merged_doc_name][str(output_page_number)] = {str(page_num + 1): document}
                output_page_number += 1

        return merge_dict
    

    def generate_split_dict(self, document_list, output_folder):
        split_dict = {
            "output_folder": output_folder,
        }
        for document in document_list:
            pages = self.get_pdf_pages(document)
            for page_num in range(len(pages)):
                split_doc_name = self.get_doc_basename(document) + "_" + str(page_num + 1)
                split_dict[split_doc_name] = {"1": {str(page_num + 1): document}}

        return split_dict


    def extract_input_files(self, pdf_dict):
        files = []
        for doc_key, doc_val in pdf_dict.items():
            if doc_key == "output_dir":
                continue
            
            for page_key, page_val in doc_val.items():
                input_page = next(iter(page_val))
                input_doc = page_val[input_page]
                if input_doc not in files:
                    files.append(input_doc)

        return files

    
    def generate_pdfs(self, pdf_dict):
        output_dir = pdf_dict["output_dir"]
        out_paths = []
        for doc_key, doc_val in pdf_dict.items():
            pdf_write_obj = pypdf.PdfWriter()
            if doc_key == "output_dir":
                continue
            
            for page_key, page_val in doc_val.items():
                input_page = next(iter(page_val))
                input_doc = open(page_val[input_page], "rb")
                pdf_write_obj.append(
                    fileobj=input_doc, pages=(int(input_page)-1, int(input_page)))
            
            out_path = os.path.join(output_dir, doc_key + ".pdf")
            output = open(out_path, "wb")
            pdf_write_obj.write(output)
            pdf_write_obj.close()
            output.close()
            out_paths.append(out_path)
        
        return out_paths


# test
# test_pdf = {'Khinvasara-Shobhit-Passport': {
#     "1":{"1": "C:\\Users\\shobh\\Documents\\Shobhit PR Renewal\\Passport_copy_1.pdf"},
#     "2":{"1": "C:\\Users\\shobh\\Documents\\Shobhit PR Renewal\\Passport_copy_2.pdf"}},
#     'output_dir': "C:\\Users\\shobh\\Documents\\Shobhit PR Renewal"}
# test_pdf_engine = PdfEngine()
# test_pdf_engine.generate_pdfs(test_pdf)

