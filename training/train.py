import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

from app.model import build_model
from app.utils import *


# PHISHING DATASET
phish_urls = [
    "http://secure-login-bank-update.local",
    "http://paypal-verification-login.local",
    "http://account-update-secure-login.local",
    "http://banking-alert-verify-user.local"
] * 500

phish_df = pd.DataFrame({
    'url': phish_urls,
    'label': 1
})

# LEGITIMATE DATASET
legit_urls = [
    "https://google.com",
    "https://amazon.com",
    "https://github.com",
    "https://wikipedia.org",
    "https://microsoft.com"
] * 500

legit_df = pd.DataFrame({
    'url': legit_urls,
    'label': 0
})

# COMBINE
full_df = pd.concat([phish_df, legit_df])
full_df = full_df.sample(frac=1).reset_index(drop=True)

# URL FEATURES
X_url = np.array([
    encode(u, MAX_URL_LEN)
    for u in full_df['url']
])

# HTML FEATURES
X_html = np.zeros((len(full_df), MAX_HTML_LEN))

# IMAGE FEATURES
X_img = np.array([
    np.random.rand(64,64,3)
    for _ in range(len(full_df))
])

y = full_df['label'].values

# SPLIT
X_url_tr, X_url_te, X_html_tr, X_html_te, X_img_tr, X_img_te, y_tr, y_te = train_test_split(
    X_url,
    X_html,
    X_img,
    y,
    test_size=0.2
)

# BUILD MODEL
model = build_model()

# TRAIN MODEL
model.fit(
    [X_url_tr, X_html_tr, X_img_tr],
    y_tr,
    epochs=4,
    batch_size=32
)

# SAVE MODEL
model.save("saved_model/phishing_model.h5")

print("✔ Model Saved")
