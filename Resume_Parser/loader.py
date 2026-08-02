from langchain_community.document_loaders import PyMuPDFLoader

def data_extraction():
    content = ""
    loader = PyMuPDFLoader(file_path = r"C:\Users\Admin\Desktop\projects\Agentic AI\Tushar Khitoliya resume.pdf")
    docs = loader.load()
    content = "".join(doc.page_content for doc in docs)
    return content