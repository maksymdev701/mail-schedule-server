import base64

from loader import parse_json_file, process_part
from func import check_whether_schedule
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    json_iterator = parse_json_file("./example_emails/json/veronica_emails.json")

    # for obj in json_iterator:
    obj = next(json_iterator)
    total_content = ''
    # Loop through each message in the thread and prints its content.
    for message in obj['messages']:
        # Extract the raw message payload and decode it from base64.
        payload = message['payload']

        # Recursively process each part of the message payload.
        if 'parts' in payload:
            for part in payload['parts']:
                content = process_part(part)
                print(content)
                print("Length ---> " + str(len(content)))
                print("Is scheduling mail ---> " + check_whether_schedule(content))
                print("\n====================================\n")
        else:
            # Decode the message content from base64 and display it.
            data = payload['body']['data']
            content = base64.urlsafe_b64decode(data).decode('utf-8')
            print(content)
            print("Length ---> " + str(len(content)))
            print("Is scheduling mail ---> " + check_whether_schedule(content))
            print("\n====================================\n")

    print(total_content)