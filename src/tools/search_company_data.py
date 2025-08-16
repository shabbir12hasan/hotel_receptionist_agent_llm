from langchain_core.tools import tool
import chromadb
from langchain_community.embeddings import SentenceTransformerEmbeddings


@tool
def search_company_data(query: str) -> str:
    """
    Searches an internal company vector database for relevant information.
    This tool is best for queries about company policies, hours, or internal processes.

    Args:
        query: The user's question to search for.

    Returns:
        The most relevant answer from the company knowledge base.
    """
    try:
        # Connect to the pre-populated vector database
        embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        db = chromadb.PersistentClient(path="./chroma_db")
        collection = db.get_collection(name="langchain")

        # Search the vector database
        results = collection.query(
            query_texts=[query],
            n_results=2,
            include=['documents']
        )

        # Check if any documents were found
        if results['documents']:
            return f"From company data: {results['documents'][0][0]}"
        # If no documents were found, return a default message
        else:
            return "No relevant company information found."
    
    # Handle exceptions related to the vector database
    except Exception as e:
        print(f"Error searching vector DB: {e}")
        return "An error occurred while searching internal data."