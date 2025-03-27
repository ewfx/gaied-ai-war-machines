from classifier import classify_email
from ocr_extractor import extract_text_from_attachment
from deduplicator import check_duplicate

def process_email(email):
    is_duplicate = check_duplicate(email)
    if is_duplicate:
        return {"email_id": email["email_id"], "status": "Duplicate request ignored"}
    else:
    # Step 5: Return structured JSON
        if email["attachments"]:
            attachment_texts = extract_text_from_attachment(email["attachments"][0]["file_path"])
            email["body"] = email["body"] + attachment_texts

        classification = classify_email(email["subject"], email["body"])
        return {
            "email_id": email["email_id"],
            "request_type": classification["request_type"],
            "sub_request_type": classification["sub_request_type"],
            "expiration_date": classification["expiration_date"],
            "deal_name": classification["deal_name"],
            "amount": classification["amount"]
        }

if __name__ == "__main__":
    email = {
        "subject": "Request for Adjustment - Reallocation Fees",
        "body": "Dear Support Team, \n\nWe need to request an adjustment for reallocation fees for Deal XYZ. The amount is $25,000.",
        "email_id": "wkefb@gmail.com"
    }
    
    result = process_email(email)
    print(result)
