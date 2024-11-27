from RAG.data_load_split import Document
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

import os


class VectorStore:
    def __init__(self, doc, embeddings_dir,
                 source,
                 embeddings_model='text-embedding-ada-002',
                 search_type='mmr',
                 k=10):
        """
        Initializes the VectorStore class.

        Args:
            doc (Document): Instance of the Document class with preloaded documents.
            embeddings_dir (str): Directory path for storing the Chroma vector database.
            embeddings_model (str): Name of the OpenAI embeddings model.
            search_type (str): Type of search, e.g., 'mmr' (Maximum Marginal Relevance).
            k (int): Number of top results to retrieve during a search.
        """
        self.doc = doc
        self.embeddings = OpenAIEmbeddings(model=embeddings_model)
        self.embeddings_dir = embeddings_dir
        self.search_type = search_type
        self.k = k
        self.vectorstore = None  # To store the Chroma instance
        self.source = source

    def store_embeddings(self):
        """
        Creates and persists a Chroma vector database from the documents.
        """
        self.vectorstore = Chroma.from_documents(
            documents=self.doc,
            embedding=self.embeddings,
            persist_directory=self.embeddings_dir
        )

    def get_embeddings(self):
        """
        Initializes or loads the vector database embeddings.
        """
        if self.vectorstore is None:  # Load or create embeddings only once
            if not os.path.exists(self.embeddings_dir) or not os.listdir(self.embeddings_dir):
                # If the embeddings directory does not exist or is empty, create it
                self.store_embeddings()
            else:
                # Load the existing vector store
                self.vectorstore = Chroma(
                    persist_directory=self.embeddings_dir,
                    embedding_function=self.embeddings
                )

    def retrieve_embeddings(self):
        """
        Retrieves the embeddings using the specified search type.

        Returns:
            Retriever: A retriever object for querying the vector database.
        """
        # Ensure embeddings are initialized
        self.get_embeddings()

        # Set up the retriever with the specified search type and parameters
        retriever = self.vectorstore.as_retriever(
            search_type=self.search_type,
            search_kwargs={'k': self.k,
                           'lambda_mult': 0.2, 'filter': {'source': self.source}}
        )
        return retriever

# #
data_path = "/Users/omarelkhashab/PycharmProjects/SurveyAnalysisRAG/Data"
embeddings_dir = "/Users/omarelkhashab/PycharmProjects/SurveyAnalysisRAG/Data/Text_Embeddings"

documents = Document(data_path)
documents.process()  # Loads and processes all documents
docs = documents.get_documents()

vectorstore = VectorStore(doc=docs, embeddings_dir=embeddings_dir,source ="Dataset 1 (Sustainability Research Results)",
embeddings_model="text-embedding-ada-002",
                           )

# # Add embeddings to the vector store
#
# vector = vectorstore.retrieve_embeddings()
# doczs = vector.invoke("How important is sustainability to consumers?")
#
# def pretty_print_docs(docs):
#     print(
#         f"\n{'-' * 100}\n".join(
#             [f"Document {i + 1}:\n\n" + d.page_content for i, d in enumerate(docs)]
#         )
#     )
#
#
# pretty_print_docs(doczs)
