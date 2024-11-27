import openai
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from RAG.prompt import ChatPrompt
#
# from data_load_split import Document
# from vector_store import VectorStore


class Generator:
    def __init__(self, model_name, retriever):
        """
        Initializes the Generator class with model, retriever, and chat prompt.
        """
        self.chat = ChatOpenAI(model_name=model_name, model_kwargs={'seed': 365}, temperature=0.1, max_tokens=200)
        self.retriever = retriever
        self.prompt = ChatPrompt()

    @staticmethod
    def format_docs(docs):
        return "\n\n".join([d.page_content for d in docs])

    def generate(self, query):
        """
        Generates a response for the given query using the retriever and prompt template.
        Args:
            query (str): The user query.
        Returns:
            str: The response from the LLM.
        """
        # Retrieve context using the query
        relevant_docs = self.retriever

        chain = self.chain = (
                {"context": relevant_docs | self.format_docs,
                 "question": RunnablePassthrough(), }
                | self.prompt.get_template()
                | self.chat
                | StrOutputParser())

        response = chain.invoke(query)

        # Invoke the chain and return the response
        return response


#
#
# data_path = "/Users/omarelkhashab/PycharmProjects/SurveyAnalysisRAG/Data"
# # embeddings_dir = "/Users/omarelkhashab/PycharmProjects/SurveyAnalysisRAG/Data/Embeddings_Store"
# embeddings_dir = "/Users/omarelkhashab/PycharmProjects/SurveyAnalysisRAG/Data/Text_Embeddings"
# #
# documents = Document(data_path)
# documents.process()  # Loads and processes all documents
# docss = documents.get_documents()
#
# vectorstore = VectorStore(doc=docss, embeddings_model="text-embedding-ada-002",
#                           embeddings_dir=embeddings_dir, source="Dataset 1 (Sustainability Research Results)")
# # # Add embeddings to the vector store
# #
# vector = vectorstore.retrieve_embeddings()
#
# gen = Generator(model_name="gpt-4o-mini", retriever=vector)
# # #
# response = gen.generate(query="How important is sustainability to consumers?")
#
# print(response)
# for i in response:
#     print(i.content, end='')  # print horizntoal


#
# docs = vector.invoke(
#     "what media types get attention when consumers look for brands at Christmas time such as Radio and others ?")
# for d in docs:
#
#     print(d.metadata)
#
# # def pretty_print_docs(docs):
# #     print(
# #         f"\n{'-' * 100}\n".join(
# #             [f"Document {i + 1}:\n\n" + d.page_content for i, d in enumerate(docs)]
# #         )
# #     )
# #     print(docs.metdata)
# # #
#
# def format_docs(docs):
#     return "\n\n".join([d.metadata for d in docs])
#
#
# print(format_docs(docs))
