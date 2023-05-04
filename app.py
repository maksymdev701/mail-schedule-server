import base64

from utils.loader import parse_json_file
from utils.func import check_whether_schedule, calc_time, predict_reply, sort_messages
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


def replay_all():
    json_iterator = parse_json_file(
        "./resources/example_emails/json/veronica_emails.json")

    for obj in json_iterator:
        # Loop through each message in the thread and prints its content.
        print(len(obj['messages']))
        for message in obj['messages']:
            # Extract the raw message payload and decode it from base64.
            payload = message['payload']
            # Decode the message content from base64 and display it.
            flag = False
            for header in payload['headers']:
                if header["name"] != "Delivered-To":
                    continue
                if header["value"] == "chelsea@tribecap.co" or header["value"] == "veronica@tribecap.co":
                    flag = True
                    break
            if flag == True:
                parts = payload
                partFlag = False
                while parts['mimeType'] != 'text/plain':
                    if parts['mimeType'] == 'text/html':
                        partFlag = True
                        break
                    parts = parts['parts'][0]
                if not partFlag:
                    data = parts['body']['data']
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
                        print("Virtual reply ---> " + predict_reply(content))
                    print("\n====================================\n")


def extract_threads():
    json_iterator = parse_json_file(
        "./resources/example_emails/json/veronica_emails.json")

    obj = next(json_iterator)

    # for obj in json_iterator:
    # Loop through each message in the thread and prints its content.
    # print(len(obj['messages']))
    for message in obj['messages']:
        # Extract the raw message payload and decode it from base64.
        payload = message['payload']
        # Decode the message content from base64 and display it.
        flag = False
        sender = None
        sendtime = None
        for header in payload['headers']:
            if header["name"] == "From":
                sender = header["value"]
            if header["name"] == "Date":
                sendtime = header["value"]
            if header["name"] != "Delivered-To":
                continue
            if header["value"] == "chelsea@tribecap.co" or header["value"] == "veronica@tribecap.co":
                flag = True
        if flag == True:
            parts = payload
            partFlag = False
            while parts['mimeType'] != 'text/plain':
                if parts['mimeType'] == 'text/html':
                    partFlag = True
                    break
                parts = parts['parts'][0]
            if not partFlag:
                data = parts['body']['data']
                content = base64.urlsafe_b64decode(data).decode('utf-8')
                content = content.replace("> ", "")
                print("\n==================================\n")
                lines = content.split("\n")
                temp_unit = []

                beautified_list = []

                for line in lines:
                    while line.startswith(">"):
                        line = line[1:]
                    if line != "\r":
                        line = line.replace("\r", "")
                        temp_unit.append(line)
                    else:
                        result = " ".join(temp_unit)
                        if not "Disclaimer" in result and not "CONFIDENTIALITY" in result:
                            beautified_list.append(result)
                        temp_unit.clear()

                beautified_message = "\n".join(beautified_list)

                # print(len(beautified_message))
                print(sort_messages(beautified_message, sender, sendtime))


if __name__ == "__main__":
    # replay_all()
    extract_threads()
