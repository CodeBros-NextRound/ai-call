tools = [
    {
        "type": "function",
        "function": {
            "name": "transfer_call",
            "description": "Transfer call to a human representative only if the user explicitly requests to speak with a person or if you cannot solve their problem.",
            "parameters": {
                "type": "object",
                "properties": {}
            },
            "say": "I'll transfer you to a human representative who can help you further. Please hold the line for a moment."
        }
    },    
    
    {
        "type": "function",
        "function": {
            "name": "end_call",
            "description": "End the current call. Use this when the conversation has reached a natural conclusion, the user's query has been fully addressed, or the user asks to end the call.",
            "parameters": {
                "type": "object",
                "properties": {}
            },
            "say": "Thank you for calling. Have a great day! Goodbye."
        }
    }
]
