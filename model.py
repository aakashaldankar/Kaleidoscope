from qdrant_client import QdrantClient
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core import StorageContext, VectorStoreIndex
from llama_index.core import TreeIndex
from llama_index.core import get_response_synthesizer

embedding_model =HuggingFaceEmbedding(model_name="sentence-transformers/all-mpnet-base-v2")
qdrant_local_path ="Qdrant_db"
collection_name ="keleidoscope"
qdrant_client =QdrantClient(path=qdrant_local_path)

# Reuse the existing collection
qdrant_vector_store = QdrantVectorStore(
    client=qdrant_client,
    collection_name=collection_name
)

vector_index = VectorStoreIndex.from_vector_store(vector_store=qdrant_vector_store, embed_model=embedding_model)