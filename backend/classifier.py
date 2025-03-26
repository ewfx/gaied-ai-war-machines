from gpt4all import GPT4All

# Load the GPT4All model
model_path = "mistral-7b.gguf"  # Update this with your downloaded model file
gpt4all_model = GPT4All(model_path)

def classify_email(email_content):
    """Classify email content using GPT4All."""
    prompt = f"Classify this email and determine its request type: {email_content}"
    
    with gpt4all_model as model:
        response = model.generate(prompt, max_tokens=100)
    
    return response  # Returns the classification result
