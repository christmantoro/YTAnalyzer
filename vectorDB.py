# Step-2: Import Libraries 

from langchain.embeddings.openai import openaiembeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma 
import os 

# Step-3: Setup OpenAi API key 
os.environ["OPENAI_API_KEY"] = "sk-"

# Step-4: open and read text file
with open("mytextdoc.txt") as f: 
    text_doc=f.read


# Step-5: Create instance of CharacterSplitter
text_splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

# Step-6: Split the text in chunks 
texts = text_splitter.split_text(text_doc)

# Step-7: Create instance of the OpenAIEmbeddings
embeddings = OpenAIEmbeddings()

# Step-8: Create instance of the chroma object 
docsearch = Chroma.from_texts(text)



