# chatbot medical kethana


This project is a medical chatbot built using LangChain and Hugging Face models. It processes medical PDFs by splitting them into text chunks, converting the text into vector embeddings using Hugging Face's sentence-transformers/all-miniLM-L6-v2 model, and storing the embeddings in Pinecone for efficient retrieval. When a user asks a question, the chatbot retrieves relevant information from Pinecone and generates a response using OpenAI's GPT model. The system is powered by Flask, providing a user-friendly web interface for seamless interaction. This project showcases the integration of NLP, vector databases, and generative AI to create an intelligent, domain-specific chatbot.

This chatbot is specially designed for medical problems, allowing users to ask health-related questions and receive accurate answers. If a question is outside the scope of medicine, the chatbot responds with, "I don't know." The project was initially built using OpenAI's GPT model, which requires API keys and incurs costs. To make it more accessible and cost-effective, I am now transitioning to open-source alternatives while retaining the option to use OpenAI for enhanced performance. Additionally, I am working on expanding the dataset to improve the chatbot's knowledge and accuracy, ensuring it can handle a wider range of medical queries. This dual approach combines the power of both proprietary and open-source technologies to create a robust, intelligent, and domain-specific medical chatbot.

project repo : https:// github.com/

###step1 create a condo envirnment after opening the repo


conda create -n medicalapp python=3.9 -y







###step2 install requiments

pip install -r requirements.txt

# chatbot
