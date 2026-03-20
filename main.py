from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="LinkShield AI")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Input schema
class URLInput(BaseModel):
    url: str

def extract_features(url):
    return [
        url.count('.'),
        url.count('-'),
        url.count('_'),
        url.count('/'),
        url.count('?'),
        url.count('='),
        url.count('@'),
        url.count('&'),
        url.count('!'),
        url.count(' '),
        url.count('~'),
        url.count(','),
        url.count('+'),
        url.count('*'),
        url.count('#'),
        url.count('$')
    ]

@app.get("/")
def home():
    return {"message": "LinkShield AI Running"}

@app.post("/predict")
def predict(data: URLInput):
    url = data.url

    # 🔥 RULE 1: Trusted domains
    if "google.com" in url or "github.com" in url or "microsoft.com" in url:
        return {"result": "Safe"}

    # 🔥 RULE 2: HTTPS check
    if url.startswith("https://") and len(url) < 50:
        return {"result": "Safe"}

    # ML prediction
    features = extract_features(url)
    prediction = model.predict([features])[0]

    return {
        "result": "Phishing" if prediction == 1 else "Safe"
    }