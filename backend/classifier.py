import google.generativeai as genai
import json
import os

# Set your Gemini API Key (Get it from Google AI Studio)
GEMINI_API_KEY = "AIzaSyDvjPP1w9WYqi0jDZw3AFi1fvt2goDu6XQ"  # Replace with your actual API key

# Initialize Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Predefined request types and sub-requests
REQUEST_TYPES = {
    "Adjustment": ["Reallocation Fees", "Amendment Fees", "Reallocation Principle"],
    "Commitment Change": ["Cashless Roll", "Decrease", "Increase"],
    "Fee Payment": ["Ongoing Fee", "Letter of Credit Fee"],
    "Money Movement - Inbound": ["Principal", "Interest", "Principal + Interest", "Principal + Interest + Fee"],
    "Money Movement - Outbound": ["Timebound", "Foreign Currency"],
    "AU Transfer":	[""],
    "Closing Notice":	[""]
}

def classify_email(subject: str, body: str):
    prompt = f"""
    You are an AI that classifies loan servicing emails. Identify the request type and sub-request type from the given email.
    Also extract the deal name, expiration date and the amount. Return empty string if value not found.
    Available Request Types:
    {json.dumps(REQUEST_TYPES, indent=2)}

    Email Subject: {subject}
    Email Body: {body}

    Provide your response in JSON format:
    {{
        "request_type": "<Request Type>",
        "sub_request_type": "<Sub Request Type>",
        "deal_name": "<Deal Name>,
        "expiration_date": "<expiration date>,
        "amount": "<Amount>,
    }}
    """

    try:
        model = genai.GenerativeModel("gemini-2.0-flash")  # Use the correct model
        response = model.generate_content(prompt) 
        classification = json.loads(response.text.strip()[8:-3])
        return classification
    except Exception as e:
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    example_email = {
        "subject": "Request for Adjustment - Reallocation Fees",
        "body": "Dear Support Team, \n\nWe need to request an adjustment for reallocation fees for Deal XYZ. The amount is $25,000."
    }
    
    result = classify_email(example_email["subject"], example_email["body"])
    print(result)
