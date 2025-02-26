from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
from langchain_openai import OpenAI
from langchain_pinecone import PineconeVectorStore
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Initialize OpenAI and Pinecone
def initialize_chatbot():
    # Initialize OpenAI model
    llm = OpenAI(
        temperature=0.4,
        max_tokens=500,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    # Initialize HuggingFace embeddings
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-miniLM-L6-v2')

    # Initialize Pinecone vector store
    docsearch = PineconeVectorStore.from_existing_index(
        embedding=embeddings,
        index_name="sree"  # Replace with your Pinecone index name
    )

    return llm, docsearch

# Initialize chatbot components
llm, docsearch = initialize_chatbot()

# Home route to render the chatbot interface
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle user messages
@app.route('/send_message', methods=['POST'])
def send_message():
    # Get user message from the frontend
    user_message = request.json['message']

    # Retrieve relevant documents from Pinecone
    retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    retrieved_docs = retriever.invoke(user_message)

    # Generate a response using OpenAI
    response = llm.invoke(f"Context: {retrieved_docs}\n\nQuestion: {user_message}")

    # Return the chatbot response
    return jsonify({'response': response})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)