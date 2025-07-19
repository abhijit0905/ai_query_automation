# flipkart_scraper.py

import os, re, ast
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def scrape_flipkart(category, max_price=None):
    """
    Uses Groq to “estimate” Flipkart’s top 5 products for the given category/price.
    Returns a list of dicts: {title, price, link, source}.
    """
    prompt = f"""
You are a highly informed shopping assistant with real‑time knowledge of Flipkart.com.
List up to 5 top‑selling items in the category "{category}" priced under ₹{max_price if max_price else 'any'}.
Return ONLY a Python list of dictionaries, each with:
- title (string)
- price (integer)
- link (full Flipkart URL)
- source: "Flipkart"

Example:
[{{"title":"Mi Redmi Note 10","price":11999,"link":"https://www.flipkart.com/...","source":"Flipkart"}}, ...]

Now please list the products.
"""
    # call Groq
    resp = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a knowledgeable e‑commerce assistant."},
            {"role": "user",   "content": prompt}
        ],
        temperature=0.2
    )

    raw = resp.choices[0].message.content.strip()
    print("🔍 Groq Flipkart Raw Output:\n", raw)

    # extract the Python list literal
    match = re.search(r"\[.*\]", raw, re.DOTALL)
    try:
        return ast.literal_eval(match.group()) if match else []
    except Exception as e:
        print("❌ Failed to parse Flipkart LLM output:", e)
        return []
