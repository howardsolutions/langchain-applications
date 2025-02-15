from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI 

from dotenv import load_dotenv
import os 

information = """
Elon Reeve Musk (born June 28, 1971) is a businessman and U.S. special government employee, best known for his key roles in Tesla, Inc., SpaceX, and the Department of Government Efficiency (DOGE), and his ownership of Twitter. Musk is the wealthiest individual in the world; as of February 2025, Forbes estimates his net worth to be US$397 billion.
"""

if __name__ == '__main__':
    load_dotenv()
    os.environ["LANGCHAIN_TRACING_V2"] = "false"
    print("Hello Langchain")

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
    
    print(res)