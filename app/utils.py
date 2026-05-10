import numpy as np
from PIL import Image

MAX_URL_LEN = 200
MAX_HTML_LEN = 1000
VOCAB_SIZE = 128


def encode(text, max_len):
    arr = [ord(c) for c in str(text) if ord(c) < VOCAB_SIZE]
    return arr[:max_len] + [0]*(max_len-len(arr))


def get_html_content(url):
    try:
        if "secure-login-bank-update" in url:
            with open("frontend/index.html", "r", encoding="utf-8") as f:
                return f.read()
        return ""
    except:
        return ""


def get_demo_image(url):
    try:
        if "secure-login-bank-update" in url:
            img = Image.new("RGB", (64,64), color=(40,82,152))
            return np.array(img)/255.0

        return np.ones((64,64,3))

    except:
        return np.ones((64,64,3))
