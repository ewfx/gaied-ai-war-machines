import openai

def classify_email(subject, body):
    prompt = f"""
    Classify this email into a request type and sub-request type.

    Subject: {subject}
    Body: {body}

    Available request types: Adjustment, AU Transfer, Closing Notice, Commitment Change, Fee Payment, Money Movement.
    Available sub-requests depend on the type.

    Output format:
    {{"request_type": "X", "sub_request_type": "Y"}}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": "You are an expert at classifying emails into predefined categories."},
                  {"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]
