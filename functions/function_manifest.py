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
        "name": "schedule_meet",
        "description": "Schedules a meeting in the user's Google Calendar only when the user provides a specific date, start time, end time, and purpose always wait for all these parameters only then call this function dont make you parameters on your own make sure it is accurate and only use this function when all information required is there are confirmed",
        "parameters": {
            "type": "object",
            "properties": {
                "date": {
                    "type": "string",
                    "format": "date",
                    "description": "The date of the meeting in ISO 8601 format (YYYY-MM-DD) you can give output like today, tomorrow, day after tomorrow too if the user says so"
                },
                "starttime": {
                    "type": "string",
                    "format": "time",
                    "description": "The start time of the meeting in 24-hour format (HH:MM:SS)."
                },
                "endtime": {
                    "type": "string",
                    "format": "time",
                    "description": "The end time of the meeting in 24-hour format (HH:MM:SS)."
                },
                "purpose": {
                    "type": "string",
                    "description": "The purpose or title of the meeting."
                },
            },
            "required": ["date", "starttime", "endtime", "purpose"]
        },
        "say": "I have successfully scheduled a meeting for you."
    }
}

]
