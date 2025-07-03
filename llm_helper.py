from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Access the API key from the environment variable
api_key = os.getenv("GROQ_API_KEY")  # Ensure the key is correctly named in the .env file

if api_key is None:
    raise ValueError("API Key not found. Please set the 'GROQ_API_KEY' in the environment variables.")

# Initialize the ChatGroq client with the API key
llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama-3.3-70b-versatile"  # Updated to currently supported model
)

if __name__ == "_main_":
    response = llm.invoke("Two most important ingredients in samosa are ")
    print(response.content)