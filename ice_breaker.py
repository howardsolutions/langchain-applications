from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI 
# from langchain_ollama import ChatOllama
# from langchain.output_parsers import StrOutputParser

from dotenv import load_dotenv
import os

from third_parties.linkedin import scrape_linkedin_profile 

if __name__ == '__main__':
    load_dotenv()
    os.environ["LANGCHAIN_TRACING_V2"] = "false"
    print("Hello Langchain")

    summary_template = """
    given the Linkedin information {information} about a person from I want you to create:
    1. a short summary 
    2. two interesting facts about them
    """

    # Create a prompt templateo[pzxc.,m]
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    # Create an instance of LLM with chat openAI
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    # llm = ChatOllama(model="llama3.2")
    
    chain = summary_prompt_template | llm 
    
    linkedin_data = scrape_linkedin_profile(linked_in_profile_url="https://www.linkedin.com/in/eden-marco", mock=True)
    
    res = chain.invoke(input={"information": linkedin_data })
    
    print(res)