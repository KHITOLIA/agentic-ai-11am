# import all libraries and
# 1. load the data from pdf file.
# 2. chunks them into pieces decide the chunk size based on the number of pages in the pdf file.
# 3. store them into vector store not into database.
# 4. make an vector store object for similarity search according to the query.


from langchain_classic.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()
def load_data():
    loader = PDFPlumberLoader(file_path = r"C:\Users\Admin\Desktop\projects\Agentic AI\invoice_bot\data\dummy_invoice_practice.pdf")
    docs = loader.load()
    return docs

def split_docs(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 400,
        chunk_overlap = 30
    )
    chunks = splitter.split_documents(docs)
    return chunks

def ingestion(chunks):
    embedding_model = HuggingFaceEmbeddings(model = "sentence-transformers/all-MiniLM-L6-v2")
    vector_store = Chroma(
        embedding_function = embedding_model,
        persist_directory = "chroma_db"
    )
    vector_store.add_documents(chunks)
    return vector_store


def pipeline():
    docs = load_data()
    chunks = split_docs(docs)
    vector_store = ingestion(chunks)
    return vector_store
vector_store = pipeline()
query = "what is total revenue"
print(vector_store.similarity_search(query, 5))