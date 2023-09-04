from textbase import bot, Message
from textbase.models import OpenAI
from typing import List

# Load your OpenAI API key
OpenAI.api_key = "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"

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """You are chatting with an AI.
"""

@bot()
def on_message(message_history: List[Message], state: dict = None):

    # Generate GPT-3.5 Turbo response
    bot_response = OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history, # Assuming history is the list of user messages
        model="gpt-3.5-turbo",
    )

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": "Plese type proper Input."
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }