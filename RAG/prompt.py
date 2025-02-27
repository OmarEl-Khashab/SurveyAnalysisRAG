from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate


class ChatPrompt:
    def __init__(self):
        """
        Initializes the ChatPrompt class. No arguments are needed during initialization.
        """
        self.chat_prompt = None

    def get_template(self):
        """
        Creates and returns a ChatPromptTemplate with a system and human message prompt.
        """
        # temp1_ = """ You are an assistant for question-answering tasks.
        #                    "Specialized in data analysis and interpreting survey data. "
        #                    "Use the following pieces of retrieved context to answer the question. "
        #                    "If you don't know the answer, just say that you don't know. "
        #                   "Use three sentences maximum and keep the answer concise and provide some numbers\n"
        #                   "Context: {context} \n"
        # """

        temp2_ = """ You are an assistant for question-answering tasks. 
                                    "Specialized in data analysis and interpreting survey data. "
                                    "Use the following pieces of retrieved context Context: {context} to answer 
                                    the question. "
                                    "If you don't know the answer, just say that you don't know. "
                                    "Use maximum 25 words to describe keep the answer focused and provide 
                                    some numbers \n"
                                     \n"
        """
        temp2 = "{question}"

        # Create the ChatPromptTemplate
        self.chat_prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(temp2_),
            HumanMessagePromptTemplate.from_template(temp2)
        ])

        return self.chat_prompt
