from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaEmbeddings
from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore:6333",
    prefer_grpc=True,


embeddings = OllamaEmbeddings(model="llama3.2:1b")

file_path = "D:/RAG/bitcoin.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load_and_split()

print(docs)


qdrant_client = QdrantClient(
    url="https://f9cfe0a7-8633-4bf1-a107-23de993f23c2.us-east4-0.gcp.cloud.qdrant.io:6333",
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.LMlBZ1E8U09iMMZL-s_Tav0lVzotv2igubmYgZ57J-I",
)



print(qdrant_client.get_collections())

qdrant = QdrantVectorStore.from_documents(
    docs,
    embeddings,
    url="https://f9cfe0a7-8633-4bf1-a107-23de993f23c2.us-east4-0.gcp.cloud.qdrant.io
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.LMlBZ1E8U09iMMZL-s_Tav0lVzotv2igubmYgZ57J-I",
    collection_name="bitcoin",
)