import os
import requests
import base64

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OWNER = "mandrain-test"
REPO = "mandraintext1"

def upload_file(path, content):
    encoded_content = base64.b64encode(content.encode()).decode()

    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{path}"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    data = {
        "message": f"auto upload {path}",
        "content": encoded_content
    }

    response = requests.put(url, json=data, headers=headers)
    print(response.json())