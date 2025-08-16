from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI



@tool
def search_llm_for_animal_color(query: str) -> str:
    """
    Use this tool to answer the color of the animal.
    It passes the query directly to the Gemini model.

    Args:
        query: The user's question about animals.

    Returns:
        The color of the animal, or an error message.

    """
    
    # Load environment variables from .env file
    # from google.colab import userdata
    # load_dotenv()
    # GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')

    if not GOOGLE_API_KEY:
        return "Google API key not found."

    # Initialize the LLM with the Google API key
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", google_api_key=GOOGLE_API_KEY)

    # Define the prompt for the LLM
    prompt = """You are an animal expert and your task is to reply the answer with one word.
              Use the most common answer if there are multiple answers or options.
              the following question: """
              
    # Invoke the LLM with the prompt and query
    response = llm.invoke(prompt+query)
    
    return response.content
