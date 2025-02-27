from langchain_community.document_loaders import UnstructuredExcelLoader
from unstructured.cleaners.core import clean_extra_whitespace
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os


class Document:
    def __init__(self, file_path):
        self.path = file_path
        self.documents = []
        self.docs_split = []

    def load_documents(self):
        """
        Loads the documents from the Excel file using UnstructuredExcelLoader.
        """
        loaders = [UnstructuredExcelLoader(os.path.join(self.path, folder), post_processors=[clean_extra_whitespace])
                   for folder in os.listdir(self.path)
                   if folder.endswith(".xlsx")]

        for loader in loaders:
            self.documents.extend(loader.load())

    def split_document(self, chunk_size=100, chunk_overlap=10):
        """
        Splits the loaded documents using RecursiveCharacterTextSplitter.
        """

        rec_text_splitter = RecursiveCharacterTextSplitter()
        self.docs_split = rec_text_splitter.split_documents(self.documents)

        return self.docs_split

    def process(self):
        """
        Processes the entire document loading, adding metadata, cleaning content, and splitting.
        """
        # Load the documents once
        self.load_documents()
        # Adjust metadata and clean page content

        for docs in self.documents:
            source = os.path.basename(docs.metadata.get('source', '')).split(".")[0]
            docs.metadata['source'] = source  # Update the source metadata
            docs.page_content = " ".join(docs.page_content.split())  # Clean extra whitespace

        # Split the documents

    def get_documents(self):
        """
        Returns the split documents.

        Returns:
            list: A list of split documents.
        """
        return self.split_document()