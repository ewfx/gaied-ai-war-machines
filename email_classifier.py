import json

# Define possible request types and sub-types
REQUEST_TYPES = {
    "Adjustment": ["Reallocation Fees", "Amendment Fees", "Reallocation Principle"],
    "Commitment Change": ["Cashless Roll", "Decrease", "Increase"],
    "Fee Payment": ["Ongoing Fee", "Letter of Credit Fee"],
    "Money Movement - Inbound": ["Principle", "Interest", "Principle + Interest", "Principle + Interest + Fee"],
    "Money Movement - Outbound": ["Timebound", "Foreign Currency"]
}

def classify_email(email_body):
    for request_type, sub_requests in REQUEST_TYPES.items():
        if request_type.lower() in email_body.lower():
            for sub_request in sub_requests:
                if sub_request.lower() in email_body.lower():
                    return request_type, sub_request
    return "Unknown", "Unknown"

def process_mock_emails():
    with open("mock_emails.json", "r") as f:
        emails = json.load(f)

    classified_emails = []
    for email in emails:
        request_type, sub_request_type = classify_email(email["body"])
        classified_emails.append({
            "id": email["id"],
            "sender": email["sender"],
            "request_type": request_type,
            "sub_request_type": sub_request_type,
            "body": email["body"]
        })

    return classified_emails