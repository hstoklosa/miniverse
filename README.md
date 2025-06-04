# Miniverse: a playground for AI conversations

A simple script that simulates playful conversations between two AI assistants with different personalities on a specified topic by using the OpenAI SDK (via OpenRouter) to generate the back-and-forth conversations.

## How it works

Miniverse creates a simulated dialogue between two AI assistants, each with their own name, instructions, and model configuration. The conversation is streamed in real-time to the console, allowing you to watch as each assistant responds to the previous message. The assistants take turns responding to each other, creating an engaging and dynamic conversation on the specified topic.

```python
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
```

### Features

- OpenRouter as an API gateway
- Topic-focused conversations
- Customisable assistant configurations (name, instructions, model)
- Real-time streaming of responses
- Configurable number of conversation turns

## Getting started

### Prerequisites

- Python 3.x
- OpenRouter API key

### Installation

1. Clone this repository

   ```
   git clone git@github.com:hstoklosa/miniverse.git
   cd miniverse
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file based on `.env.sample` with your OpenRouter API key:

   ```
   mv .env.sample .env
   ```

### Setting up Environment Variables

Before running the script, you need to set up your OpenRouter API key within the `.env` file:

```
OPENROUTER_API_KEY=your_openrouter_api_key
```

### Usage

Run the script with default settings:

```
python main.py
```

You can customise the personalities and topics directly in the script or build upon the code to create a more interactive experience.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
