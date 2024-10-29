# * import libraries
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


class Ollama:
    def __init__(self):
        # model choice
        self.llm = OllamaLLM(model="mistral")

    def chat(self, messages: list) -> str:
        '''
        get response of LLM

        :param messages: list of chat messages
        :return: LLM response
        '''

        print(messages)

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "Tu es un assistant qui doit répondre au question de l'utilisateur."
                )
            ]
        )

        for message in messages:
            prompt.append((message['role'], message['content']))

        chain = prompt | self.llm
        response = chain.invoke({})

        return response