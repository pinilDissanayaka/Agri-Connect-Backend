import os
from dotenv import load_dotenv
from langchain_groq.chat_models import ChatGroq
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate,HumanMessagePromptTemplate,SystemMessagePromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')


llm = ChatGroq(model="llama3-8b-8192", temperature=0.7)
    
def get_solution(disease:str):
    template ="""
    You are an expert in plant pathology. 
    I have a specific plant disease called {DISEASE}. 
    Could you provide a more detailed description of this disease, including symptoms, causes, affected plant species, and effective treatment methods? 
    Please focus on both chemical and natural remedies for treatment, and mention any preventive measures that can be taken.
    If you can make a answer in the sinhala and tamil language.
    """
    
    prompt=ChatPromptTemplate.from_template(template=template)
    
    chain=(
        {"DISEASE" : RunnablePassthrough()} |
        prompt |
        llm | 
        StrOutputParser()
    )
    
    solution=chain.invoke({"DISEASE" : disease})
    
    return solution
