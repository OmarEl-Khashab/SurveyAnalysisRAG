from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from RAG.prompt import ChatPrompt


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
