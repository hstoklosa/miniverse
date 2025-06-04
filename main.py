import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialise OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)


def start_conversation(assistant1_config, assistant2_config, topic, turns=10):
    messages = [{ 
        "role": "system", 
        "content": f"This is a conversation about: {topic}. Do not use markdown formatting." 
    }]
    curr_assistant = assistant1_config

    for _ in range(turns):
        # Select the current assistant config
        if curr_assistant == assistant1_config:
            assistant_config = assistant1_config
        else:
            assistant_config = assistant2_config

        # Add the assistant prompt to the messages
        messages.append({ "role": "system", "content": assistant_config["instructions"] })

        print(f"{assistant_config['name']}: ", end="", flush=True)
        
        # Generate a response from the current assistant with streaming
        full_response = ""
        response = client.chat.completions.create(
            model=assistant_config["model"],
            messages=messages,
            temperature=0.7,
            stream=True,
        )
        
        # Process the streaming response
        for chunk in response:
            if not chunk.choices[0].delta.content:
                continue

            content = chunk.choices[0].delta.content
            full_response += content
            print(content, end="", flush=True)
        
        print("\n")
        
        # Add the assistant's response to the messages
        messages.append({ "role": "assistant", "content": full_response })

        # Switch to the next assistant
        curr_assistant = assistant2_config if curr_assistant == assistant1_config else assistant1_config

    return messages


if __name__ == "__main__":
    assistant1_config = {
        "name": "TechOptimist",
        "instructions": "expertise in technology, friendly, informative",
        "model": "openai/gpt-4o-mini"
    }
    
    assistant2_config = {
        "name": "CriticalThinker",
        "instructions": "skeptical, questions assumptions, thoughtful, critical perspective",
        "model": "openai/gpt-4o-mini"
    }
    
    topic = "The future of artificial intelligence"
    
    start_conversation(assistant1_config, assistant2_config, topic)