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
    },
    
    {
        "type": "function",
        "function": {
            "name": "add_calendar_event",
            "description": "Add an event to the user's Google Calendar. Use this when a user wants to schedule an appointment, meeting, or any other event. Collect all necessary details like date, time, title, and duration in a natural conversation.",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "The title or name of the event"
                    },
                    "date": {
                        "type": "string",
                        "description": "The date of the event in YYYY-MM-DD format"
                    },
                    "start_time": {
                        "type": "string",
                        "description": "The starting time of the event in HH:MM format (24-hour)"
                    },
                    "end_time": {
                        "type": "string",
                        "description": "The ending time of the event in HH:MM format (24-hour)"
                    },
                    "description": {
                        "type": "string",
                        "description": "Optional description of the event"
                    }
                },
                "required": ["title", "date", "start_time", "end_time"]
            },
            "say": "I'll schedule that event for you. Just a moment while I add it to your calendar."
        }
    }
]

