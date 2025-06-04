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

model = "openai/gpt-4o-mini"


def start_conversation(assistant1_prompt, assistant2_prompt, topic, turns=10):
    messages = [{ 
        "role": "system", 
        "content": f"This is a conversation about: {topic}. Do not use markdown formatting." 
    }]
    curr_assistant = assistant1_prompt

    for t in range(turns):
        # Select the current assistant prompt
        if curr_assistant == assistant1_prompt:
            assistant_prompt = assistant1_prompt
            assistant_name = "Assistant 1"
        else:
            assistant_prompt = assistant2_prompt
            assistant_name = "Assistant 2"

        # Add the assistant prompt to the messages
        messages.append({ "role": "system", "content": assistant_prompt })

        # Generate a response from the current assistant
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7,
        )
        assistant_response = response.choices[0].message.content

        print(f"{assistant_name}: {assistant_response}\n")
        
        # Add the assistant's response to the messages
        messages.append({ "role": "assistant", "content": assistant_response })

        # Switch to the next assistant
        curr_assistant = assistant2_prompt if curr_assistant == assistant1_prompt else assistant1_prompt

    return messages


if __name__ == "__main__":
    assistant1_prompt = "expertise in technology, friendly, informative"
    assistant2_prompt = "skeptical, questions assumptions, thoughtful, critical perspective"
    topic = "The future of artificial intelligence"
    
    start_conversation(assistant1_prompt, assistant2_prompt, topic)