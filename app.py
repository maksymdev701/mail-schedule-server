import base64

from loader import parse_json_file, process_part
from func import check_whether_schedule, calc_time
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

if __name__ == "__main__":
    # Load email threads in json format
    json_iterator = parse_json_file(
        "./example_emails/json/veronica_emails.json")

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
                if content == '':
                    print("\n====================================\n")
                    continue
                is_schedule = check_whether_schedule(content)
                print("Is scheduling mail ---> " + is_schedule)
                if is_schedule == 'True':
                    meeting_time = calc_time(content)
                    print("Meeting time ---> " + meeting_time)
                print("\n====================================\n")
        else:
            # Decode the message content from base64 and display it.
            data = payload['body']['data']
            content = base64.urlsafe_b64decode(data).decode('utf-8')
            print(content)
            print("Length ---> " + str(len(content)))
            if content == '':
                print("\n====================================\n")
                continue
            is_schedule = check_whether_schedule(content)
            print("Is scheduling mail ---> " + is_schedule)
            if is_schedule == 'True':
                meeting_time = calc_time(content)
                print("Meeting time ---> " + meeting_time)
            print("\n====================================\n")

    print(total_content)
