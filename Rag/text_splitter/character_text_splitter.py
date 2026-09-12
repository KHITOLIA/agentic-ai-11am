from langchain_text_splitters import CharacterTextSplitter
from langchain_classic.document_loaders import TextLoader
loader = TextLoader(file_path = r"C:\Users\Admin\Desktop\projects\Agentic AI\data\ml.txt")

docs = loader.load()

splitter = CharacterTextSplitter(chunk_size = 1500, 
                                 separator = ' ')

chunks = splitter.split_documents(documents= docs)
# print(len(docs) , len(chunks))

print(chunks[0].page_content)