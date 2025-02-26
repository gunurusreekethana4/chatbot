from src.helper import load_pdf_file,text_split,download_hugging_face_embeddings
import pinecone
from pinecone import ServerlessSpec
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
import os



load_dotenv()

PINECONE_API_KEY =os.environ.get('PINECONE_API_KEY')
OPENAI_API_KEY =os.environ.get('OPENAI_API_KEY')


import pinecone
from pinecone import ServerlessSpec
YOUR_API_KEY
# pc = pinecone.Pinecone(api_key="aptlry")

pc.create_index(
    name="sree",
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    )
   
    
)


import os
os.environ['PINECONE_API_KEY']='apikey]'
os.environ['OPENAI_API_KEY']="apikey"



from langchain_pinecone import PineconeVectorStore

docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    embedding=embeddings,
    index_name="sree"  
)



