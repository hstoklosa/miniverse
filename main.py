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

        # Generate a response from the current assistant
        response = client.chat.completions.create(
            model=assistant_config["model"],
            messages=messages,
            temperature=0.7,
        )
        assistant_response = response.choices[0].message.content

        print(f"{assistant_config['name']}: {assistant_response}\n")
        
        # Add the assistant's response to the messages
        messages.append({ "role": "assistant", "content": assistant_response })

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