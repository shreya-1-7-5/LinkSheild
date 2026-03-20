from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import pandas as pd
import pickle

# ── Load Model ─────────────────────────────────────────────
model = pickle.load(open("model.pkl", "rb"))

# ── FastAPI App ────────────────────────────────────────────
app = FastAPI()

# ── CORS (important for local + safety) ────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Serve Static Files ─────────────────────────────────────
app.mount("/static", StaticFiles(directory="static"), name="static")

# ── Input Schema ───────────────────────────────────────────
class URLRequest(BaseModel):
    url: str

# ── Feature Extraction (SIMPLE VERSION) ────────────────────
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
        url.count(' ')
    ]

# ── Home Route (SERVES FRONTEND) ───────────────────────────
@app.get("/")
def serve_frontend():
    return FileResponse("static/index.html")

# ── Prediction Route ───────────────────────────────────────
@app.post("/predict")
def predict(data: URLRequest):
    features = extract_features(data.url)

    # Adjust based on your model training features
    df = pd.DataFrame([features])

    prediction = model.predict(df)[0]

    if prediction == 1:
        result = "Phishing"
    else:
        result = "Safe"

    return {"result": result}
