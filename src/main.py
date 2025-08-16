from src.primary_agent.primary_agent import initialize_primary_agent

def main():
    """
    The main loop for the agent application.
    """
    try:
        # Initialize the agent
        agent_executor = initialize_primary_agent()
    except ValueError as e:
        print(f"Error initializing agent: {e}")
        return

    print("Agent is ready. Enter your queries. Type 'exit' to quit.")

    while True:
        user_query = input("You: ")
        if user_query.lower() == 'exit':
            break

        # Invoke the agent with the user's query
        try:
            response = agent_executor.invoke({"input": user_query})
            print(f"Agent: {response['output']}")
        except Exception as e:
            print(f"Agent: Sorry, an error occurred. {e}")

if __name__ == "__main__":
    main()

