# Step-1: Import necessary libraries

from langchain.chains import RetrievalQAWithSourcesChain
from langchain import OpenAI
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPEN_API_KEY"] = os.environ.get('OPENAI_API_KEY')

embeddings = OpenAIEmbeddings()

docsearch = Chroma(persist_directory="db", embedding_function=embeddings)

chain = RetrievalQAWithSourcesChain.from_chain_type(OpenAI(temperature=0),
                                                    chain_type="stuff",
                                                    retriver=docsearch.as_retriever(search_kwargs={"k":1}))

def get_analysis(user_input):
    result = chain({"question": user_input}, return_only_outputs=True)
    return result["answer"]
