from classifier import classify_email
from ocr_extractor import extract_text_from_attachment
from deduplicator import check_duplicate

def process_email(email):
    # Step 1: Classify email
    classification = classify_email(email["subject"], email["body"])

    # Step 2: Extract relevant fields
    extracted_data = {
        "deal_name": extract_deal_name(email["body"]),
        "amount": extract_amount(email["body"]),
        "expiration_date": extract_expiry(email["body"])
    }

    # Step 3: OCR for attachments
    attachment_texts = []
    for attachment in email.get("attachments", []):
        attachment_texts.append(extract_text_from_attachment(f"data/attachments/{attachment}"))

    # Step 4: Check for duplicates
    is_duplicate = check_duplicate(email)
    
    if is_duplicate:
        return {"email_id": email["email_id"], "status": "Duplicate request ignored"}

    # Step 5: Return structured JSON
    return {
        "email_id": email["email_id"],
        "request_type": classification["request_type"],
        "sub_request_type": classification["sub_request_type"],
        "extracted_data": extracted_data,
        "attachments_processed": attachment_texts
    }
