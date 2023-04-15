import json
import base64
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


def parse_json_file(filename):
    # Open the file for reading
    with open(filename, 'r', encoding='utf-8') as f:
        # Create a JSON decoder object
        decoder = json.JSONDecoder()

        # Read the file in chunks
        buffer = ''
        for chunk in f:
            buffer += chunk.strip()
            while buffer:
                # Try to decode a JSON object from the buffer
                try:
                    obj, idx = decoder.raw_decode(buffer)
                    yield obj
                    buffer = buffer[idx:].strip()
                except json.JSONDecodeError:
                    # Not enough data in the buffer to decode a JSON object yet
                    break


def decode_email():
    # Replace YOUR_EMAIL with the email address of the user whose email want to access.
    user_id = 'YOUR_EMAIL'

    # Replace THREAD_ID with the ID of the email thread you want to retrieve.
    thread_id = 'THREAD_ID'

    creds = {}
    service = build('gmail', 'v1', credentials=creds)

    # Retrieve a list of messages in the specified thread.
    thread = service.users().threads().get(userId=user_id, id=thread_id).execute()

    # Loop through the list of messages in the thread and extract content of each message.
    for message in thread['messages']:
        msg = service.users().messages().get(
            userId=user_id, id=message['id'], format='full').execute()

        # Extract the raw message payload and decode it from base64.
        payload = msg['payload']
        if 'parts' in payload:
            parts = payload['parts']
            print(parts)
            data = None
            for part in parts:
                if part['body'] and part['body']['data']:
                    data = part['body']['data']
                    break
        else:
            data = part['body']['data']

        # Decode the message content from base64 and print it.
        content = base64.urlsafe_b64decode(data).decode('utf-8')
        print(content)


def process_part(part):
    """
    Recursively process each part of a message payload.
    """
    # part_headers = part.get('headers')
    # part_content_type = next((v for k, v in part_headers if k == 'Content-Type'), '').lower()

    if 'parts' in part:
        # If this part has nested parts, process each one.
        content = ''
        for nested_part in part['parts']:
            content += process_part(nested_part)
    else:
        # Decode the message content from base64 and print it.
        if part['mimeType'] != 'text/plain':
            return ''
        data = part['body']['data']
        content = base64.urlsafe_b64decode(data).decode()
    return content
