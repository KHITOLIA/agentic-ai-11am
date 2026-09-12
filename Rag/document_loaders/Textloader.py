# from langchain_classic.document_loaders import TextLoader

# loader = TextLoader(file_path = r"C:\Users\Admin\Desktop\projects\Agentic AI\data\ml.txt")

# docs = loader.load()
# print(docs[0].page_content)


from langchain_classic.document_loaders import PyPDFLoader

loader = PyPDFLoader(file_path=r"C:\Users\Admin\Desktop\projects\Agentic AI\data\Machine learning System Design.pdf")
docs = loader.load()

print(docs[0].page_content)