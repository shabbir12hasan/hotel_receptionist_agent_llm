from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# tools
from hotel_receptionist_agent.src.tools.search_company_data import search_company_data
from hotel_receptionist_agent.src.tools.search_llm_for_animal_color import search_llm_for_animal_color

def initialize_primary_agent() -> AgentExecutor:
    """
    Initializes the LangChain agent with its tools and LLM.

    Returns:
        An AgentExecutor instance ready to handle user queries.
    """
    
    # Load environment variables from .env file
    # from google.colab import userdata
    # load_dotenv()
    # GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')

    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY not found. Please set it in your .env file.")

    # 1. Define the LLM (Gemini)
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", google_api_key=GOOGLE_API_KEY)

    # 2. Define the tools the agent can use
    # tools = [get_current_weather, search_company_data, search_llm_for_animals]
    tools = [search_company_data, search_llm_for_animal_color]

    # You have access to tools to get real-time weather, search internal company data, and answer questions about animals.
    # 3. Define the prompt for the agent
    prompt = ChatPromptTemplate.from_messages([
        ("system", """
        You are a helpful assistant.
        You have access to tools to get search internal company data or answer questions about animals.

        If a query doesn't match any tools, reply with a statement 'I am afraid I cannot assist you with that.'

        Do not reply if you cannot find any relevant results, it's mandatory to not give wrong or additional information.
        """),
        MessagesPlaceholder("chat_history", optional=True),
        ("user", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ])

    # 4. Create the agent
    agent = create_tool_calling_agent(llm, tools, prompt)

    # 5. Create the AgentExecutor
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    return agent_executor

