from langchain_ollama import OllamaEmbeddings
embedding_model = OllamaEmbeddings(model = 'bge-m3')
query = "Delhi is the capital of India"
vector = embedding_model.embed_query(query)
print(vector)