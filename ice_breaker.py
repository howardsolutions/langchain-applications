from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI 

from dotenv import load_dotenv
import os 

information = """

"""

if __name__ == '__main__':
    load_dotenv()
    print("Hello Langchain")
    # print(os.environ['OPENAI_API_KEY'])

    summary_template = """
    given the information {information} about a person from I want you to create:
    1. a short summary 
    2. two interesting facts about them
    """

    # Create a prompt templateo[pzxc.,m]
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    # Create an instance of LLM with chat openAI
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    
    chain = summary_prompt_template | llm
    
    res = chain.invoke(input={"information": information })