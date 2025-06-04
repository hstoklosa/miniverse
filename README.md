# Miniverse: a playground for AI conversations

Miniverse is a simple Python script that simulates playful conversations between two AI assistants with different personalities on a specified topic. It uses the OpenAI API (via OpenRouter) to generate the back-and-forth conversations.

## How it works

### Features

- OpenRouter as an API gateway
- Topic-focused conversations
- Customisable assistant personalities
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

### Usage

Run the script with default settings:

```
python main.py
```

To customise the conversation, modify the assistant prompts and topic in the `main.py` file:

```python
assistant1_prompt = "expertise in technology, friendly, informative"
assistant2_prompt = "skeptical, questions assumptions, thoughtful, critical perspective"
topic = "The future of artificial intelligence"
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
