from langchain_community.document_loaders import PyMuPDFLoader

def data_extraction(resume_file_path):
    content = ""
    loader = PyMuPDFLoader(file_path = resume_file_path)
    docs = loader.load()
    content = "".join(doc.page_content for doc in docs)
    return content