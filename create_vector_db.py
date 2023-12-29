from langchain.embeddings.openai import OpenAIEmbeddings 
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
import youtube_transcriptor as trans
import shutil
from dotenv import load_dotenv
import requests_cache
from langchain.chains import RetrievalQAWithSourcesChain
from langchain import OpenAI
import os
import shutil


load_dotenv()


def create_db_and_analyze(video_url):
    """
    Create a database from the transcript of a video and analyze it.

    Args:
        video_url (str): The URL of the video.

    Returns:
        str: The summarized content of the video.
    """

    # Set the OpenAI API key
    os.environ["OPENAI_API_KEY"] = os.environ.get('OPENAI_API_KEY')

    # Remove the existing 'db' directory if it exists
    if os.path.exists('db'):
        shutil.rmtree('db')

    # Clear the requests cache
    requests_cache.clear()

    # Get the transcript of the video
    transcript = trans.get_transcript(video_url)

    # Split the transcript into smaller chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_text(transcript)

    # Create embeddings for the text chunks and store them in a database
    embeddings = OpenAIEmbeddings()
    db = Chroma.from_texts(texts, 
                           embeddings, 
                           metadatas=[{"source": f"Text chunk {i} of {len(texts)}"} for i in range(len(texts))], 
                           persist_directory="db")
    db.persist()

    # Create a Chroma instance for searching in the database
    docsearch = Chroma(persist_directory="db", embedding_function=embeddings)

    # Create a retrieval QA chain for answering questions based on the database
    chain = RetrievalQAWithSourcesChain.from_chain_type(OpenAI(temperature=0), 
                                                        chain_type="stuff", 
                                                        retriever=docsearch.as_retriever(search_kwargs={"k": 1}))
    
    # Ask a question about the content and get the answer from the chain
    user_query = "Tulis Wawasan yang Dapat Diaplikasikan dalam Bahasa Indonesia dengan gaya bercerita tentang konten, kemudian tulis blog singkat."
    result = chain({"question": user_query}, return_only_outputs=True)
    print(result["answer"])

    # Clean up and return the answer
    db = None
    return result["answer"]



    
 