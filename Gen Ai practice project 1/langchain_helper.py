#langchain_helper
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# gemini key
os.environ['GOOGLE_API_KEY'] = "Your api key"

# we have to specify which model we use
llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash",
    temperature=0.6,
    max_output_tokens=100
)

def restaurant_name_dishes_generator(cuisine):
    # Chain 1: Restaurant name
    name_prompt = PromptTemplate(
        input_variables=["cuisine"],
        template="Suggest a fancy restaurant name for {cuisine} food."
    )
    name_chain = LLMChain(llm=llm, prompt=name_prompt, output_key='restaurant_name')

    # Chain 2: Menu items
    menu_prompt = PromptTemplate(
        input_variables=["restaurant_name"], 
        template="Suggest menu items for {restaurant_name}. Return comma separated."
    )
    menu_chain = LLMChain(llm=llm, prompt=menu_prompt, output_key='menu_items')

    # combine the chain 
    full_chain = SequentialChain(
        chains=[name_chain, menu_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"],
        verbose=True
    )

    result = full_chain({"cuisine": cuisine})
    return result
