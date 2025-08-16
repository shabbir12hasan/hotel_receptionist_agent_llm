import os
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

# # Dynamically set the project path
# project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
# # Add the src directory to the Python path
# sys.path.append(project_path)

# from hotel_receptionist_agent.utils.db_utils import remove_directory
from utils.db_utils import remove_directory

def setup_vector_database(
        chroma_db_path="hotel_receptionist_agent/hotel_receptionist_agent/data/embeddings/chroma_db"
        ,input_raw_documents="hotel_receptionist_agent/hotel_receptionist_agent/data/raw_data/company_faqs.txt"
        ,remove_old_db_flag=True
        ):
    """
    Creates and populates a dummy vector database with company FAQs.
    """

    # Reset the database by removing the persistence directory    
    if remove_old_db_flag:
        remove_directory(chroma_db_path)

    # Load the text data
    loader = TextLoader(input_raw_documents)
    documents = loader.load()

    # Create a vector store from the documents
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    # Initialize Chroma without documents to check if it's empty
    vector_db_check = Chroma(persist_directory=chroma_db_path, embedding_function=embeddings)
    print(f"Number of items in Chroma DB before loading: {vector_db_check._collection.count()}")
    
    # Create the vector store from the documents
    vector_db = Chroma.from_documents(documents, embeddings, chroma_db_path)

    # Check the number of items after loading
    print(f"Number of items in Chroma DB after loading: {vector_db._collection.count()}")

    # Save the database
    vector_db.persist()

    print("Vector database populated successfully with company data.")

if __name__ == "__main__":
    setup_vector_database()