import requests
import base64


def image_to_base64(url):
    response = requests.get(url)
    if response.status_code == 200:
        base64_str = base64.b64encode(response.content).decode("utf-8")
        return base64_str
    else:
        raise Exception(f"Failed to fetch image: {response.status_code}")
