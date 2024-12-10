from dotenv import load_dotenv
import os
load_dotenv()

import requests

headers = {
    'Content-type': 'application/json',
}

json_data = {
    'text': 'Hello, slack!a',
}

response = requests.post(
    f'https://hooks.slack.com/services/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/{os.environ.get("SLACK_ID")}',
    headers=headers,
    json=json_data,
)

print(response)

