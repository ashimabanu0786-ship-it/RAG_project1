from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from streaming import completion_llm

embeddings = OllamaEmbeddings(model="llama3.2:1b")

url="https://f9cfe0a7-8633-4bf1-a107-23de993f23c2.us-east4-0.gcp.cloud.qdrant.io:6333"
api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.LMlBZ1E8U09iMMZL-s_Tav0lVzotv2igubmYgZ57J-I"

question = input("Enter your question: ")

qdrant = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    collection_name="bitcoin",
    url=url,
    api_key=api_key
)

response = qdrant.similarity_search(
    question, k=2
)

prompt=f"""
Question:{question}
contect:{response}
you are a helpful assistant that can answer questions about the context provided."""

completion_llm(prompt)
