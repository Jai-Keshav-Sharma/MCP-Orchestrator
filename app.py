import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient
import warnings

# Suppress ResourceWarnings for cleaner CLI output
warnings.filterwarnings("ignore", category=ResourceWarning)

async def run_memory_chat():
    # Load environment variables from .env file
    load_dotenv()
    # Set the GROQ API key from environment variables
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    config_file = "browser_mcp.json"  # Path to MCP client configuration

    print("Initialising Chat...")

    # Initialize the MCP client and language model
    client = MCPClient.from_config_file(config_file)
    llm = ChatGroq(model="llama3-8b-8192")

    # Create the MCP agent with memory enabled for conversational context
    agent = MCPAgent(llm=llm, client=client, max_steps=15, memory_enabled=True)

    # Print instructions for the user
    print("\n==== Interactive MCP Chat ====")
    print("Enter 'exit' to end the conversation.")
    print("Type 'clear' to clear conversation history.")
    print("================================")

    try:
        while True:
            # Prompt user for input
            user_input = input("\nYou: ")

            # Exit the chat loop if user types 'exit'
            if user_input.lower() == "exit":
                print("Ending conversation...")
                break

            # Clear conversation history if user types 'clear'
            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Conversation history cleared.")
                continue

            print("\nAssistant: ", end="", flush=True)
            try:
                # Get response from the agent asynchronously
                response = await agent.run(user_input)
                print(response)
            except Exception as e:
                # Print any errors encountered during agent response
                print(f"\nError: {e}")
    except Exception as e:
        # Print any errors encountered in the main chat loop
        print(f"\nError: {e}")

    # Ensure all client sessions are closed before exiting
    if client and getattr(client, 'sessions', None):
        await client.close_all_sessions()

if __name__ == "__main__":
    # Run the chat application using asyncio event loop
    asyncio.run(run_memory_chat())


