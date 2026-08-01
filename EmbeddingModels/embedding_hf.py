from langchain_huggingface import HuggingFaceEmbeddings
model_name = "sentence-transformers/all-MiniLM-L6-V2" 

embedding_model = HuggingFaceEmbeddings(
    model = model_name
)
query = "What is machine learning"
vector = embedding_model.embed_query(query)
print(len(vector))
