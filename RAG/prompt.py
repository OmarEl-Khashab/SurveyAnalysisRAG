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
        temp1 = '''
        You are a helpful Survey Analysis chatbot assistant at Bounce Insights company at Dublin, Ireland.
        The platform is an AI insights consumer platform offering actionable insights to businesses.
        Your task is to provide the team with answers to their questions in maximum of two lines.
        To answer the question, based only on the following context:
        {context}
        
        At the end of the response, specify the name of the source of the answer as:
        Resources:
        Source is the dataset the following: 
        '''
        temp1_= """ You are an assistant for question-answering tasks. 
                            "Specialized in data analysis and interpreting survey data. "
                            "Use the following pieces of retrieved context to answer the question. "
                            "If you don't know the answer, just say that you don't know. "
                            "Use three sentences maximum and keep the answer concise and provide some numbers\n"
                            "Context: {context} \n"
        """

        temp2 = "{question}"

        # Create the ChatPromptTemplate
        self.chat_prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(temp1_),
            HumanMessagePromptTemplate.from_template(temp2)
        ])

        return self.chat_prompt
