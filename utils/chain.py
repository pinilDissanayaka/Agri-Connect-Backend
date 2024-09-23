import os
from dotenv import load_dotenv
from langchain_groq.chat_models import ChatGroq
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate,HumanMessagePromptTemplate,SystemMessagePromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

class Chain(object):
    def __init__(self) -> None:
        self.llm = ChatGroq(model="llama3-8b-8192", temperature=0.7)
    
    def getChain(self, question: str, num_questions: int = 1):
        template = """You are a teacher coming up with questions to ask on a quiz. 

                    Given the following document delimited by three backticks please generate {num_questions} questions based on that document.

                    A questions should be concise and based explicitly on the document's information. It should be asking about one thing at a time.

                    Try to generate a questions that can be answered by the whole document's important sections  not just an individual sentence.

                    Return just the text of the generated question, no more additional output. If there are several questions they should be separated by a newline character.

                    When formulating a question, don't reference the provided document or say "from the provided context", "as described in the document", "according to the given document" or anything similar.

                    ```{context_str}```
                """
                            
        chatPromptTemplate = ChatPromptTemplate.from_messages(
           [
               ("system",template),
               ("human",question,)
           ]
        )
        output_parser = StrOutputParser()
 
        chain = (
            chatPromptTemplate
            | self.llm
            | output_parser
        )
        
        return chain.invoke({"context_str": question, "num_questions": num_questions})
    

text ="your text here"
def main():
    chain = Chain()
    d = chain.getChain(question=text, num_questions=5)
    print(d)

if __name__ == "__main__":
    main()
