# flight_scraper.py

import os
import re
import ast
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def scrape_flight_prices(source, destination, date):
    """
    Uses Groq to “scrape” (i.e. estimate) flight prices from source to destination on date.
    Returns a list with one dict: {flight, price, source}.
    """
    if not source or not destination or not date:
        print("❌ Missing source/destination/date for flight query.")
        return []

    prompt = f"""
You are a flight‑price assistant. The user wants the current approximate cost in INR 
for a one‑way ticket from {source} to {destination} on {date}. 
Respond ONLY with a Python list of dictionaries, each with keys:
- flight: name or number
- price: integer INR
- source: "GroqEstimate"

Example:
[{{"flight": "IndiGo 6E-101", "price": 4899, "source": "GroqEstimate"}}]
"""

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that returns structured flight‑price estimates."},
            {"role": "user",   "content": prompt}
        ],
        temperature=0.0
    )

    raw = response.choices[0].message.content.strip()
    print("🔍 Groq Flight Raw Output:\n", raw)

    # Extract Python list literal
    match = re.search(r"\[.*\]", raw, re.DOTALL)
    try:
        return ast.literal_eval(match.group()) if match else []
    except Exception as e:
        print(f"❌ Failed to parse Groq output: {e}")
        return []
