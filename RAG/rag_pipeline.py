import openai
from RAG.data_load_split import Document
from RAG.vector_store import VectorStore
from RAG.generation import Generator


class RAGPipeline:
    def __init__(self, doc_path, embeddings_dir, source, embeddings_model="text-embedding-ada-002",
                 model_name="gpt-4o-mini"):
        self.doc_path = doc_path
        self.embeddings_dir = embeddings_dir
        self.embeddings_model = embeddings_model
        self.model_name = model_name
        self.source = source
        self.documents = None
        self.generator = None
        self.vector_store = None
        self.retriever = None

    def process_documents(self):
        doc_loader = Document(self.doc_path)
        doc_loader.process()
        self.documents = doc_loader.get_documents()
        print(f"Documents processed: {len(self.documents)}")

    def build_vector_store(self):
        self.vector_store = VectorStore(
            doc=self.documents,  # Correct parameter name
            embeddings_dir=self.embeddings_dir,
            embeddings_model=self.embeddings_model,
            source=self.source
        )
        print("Vector store built successfully.")

    def setup_generator(self):
        self.retriever = self.vector_store.retrieve_embeddings()
        print("Retriever initialized.")
        self.generator = Generator(model_name=self.model_name, retriever=self.retriever)

    def run(self, query):
        self.process_documents()
        self.build_vector_store()
        self.setup_generator()

        try:
            response = self.generator.generate(query)
            print(f"Question: {query}\nResponse: {response}")
            return response
        except Exception as e:
            print(f"Error during pipeline run: {e}")
            return None


if __name__ == "__main__":
    data_path = "/Users/omarelkhashab/PycharmProjects/SurveyAnalysisRAG/Data"
    embeddings_dir = "/Users/omarelkhashab/PycharmProjects/SurveyAnalysisRAG/Data/Text_Embeddings"
#
    rag_pipeline = RAGPipeline(data_path, embeddings_dir, source="Dataset 1 (Sustainability Research Results)")
    output = rag_pipeline.run(query="How important is sustainability to consumers?")

# response = gen.generate_response(query="How important is sustainability to consumers?")

# documents = Document(file_path=data_path)
# vectorstore = VectorStore(document=documents, embeddings_model="text-embedding-ada-002",
#                           embeddings_dir=embeddings_dir)

# vectorstore.store_embeddings()  # Add embeddings to the vector store

# vector = vectorstore.retrieve_embeddings()

# gen = Generator(model_name="gpt-4", retriever=vector)
