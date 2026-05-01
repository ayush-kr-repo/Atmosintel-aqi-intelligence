import requests
import pandas as pd
from datetime import datetime
import os

TOKEN = os.getenv("WAQI_TOKEN")

if not TOKEN:
    raise RuntimeError("WAQI_TOKEN environment variable is not set.")

url = f"https://api.waqi.info/map/bounds/?token={TOKEN}&latlng=28.4,76.8,28.9,77.5"

response = requests.get(url, timeout=30)
response.raise_for_status()
data = response.json()

rows = []

for s in data["data"]:
    rows.append({
        "station": s["station"]["name"],
        "latitude": s["lat"],
        "longitude": s["lon"],
        "aqi": s["aqi"],
        "timestamp": datetime.now()
    })

df = pd.DataFrame(rows)

file_name = "data/aqi_data.csv"

if os.path.exists(file_name):
    old = pd.read_csv(file_name)
    df = pd.concat([old, df])

df.to_csv(file_name, index=False)
