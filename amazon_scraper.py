# amazon_scraper.py

import os, re, ast
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def scrape_amazon(category, max_price=None):
    """
    Ask Groq to return a list of plausible Amazon products for `category`
    under `max_price`. Returns a list of dicts: {title, price, link, source}.
    """
    prompt = f"""
You are an assistant that knows the current Amazon.in catalog.
List up to 5 best-selling {category} under ₹{max_price if max_price else 'any price'}.
Return ONLY a Python list of dicts with keys:
- title (string)
- price (integer)
- link (full Amazon.in URL)
- source: "Amazon"

Example:
[{{"title":"Samsung Galaxy M12","price":9999,"link":"https://www.amazon.in/...","source":"Amazon"}}, ...]

Now list the products.
"""
    resp = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role":"system","content":"You are a knowledgeable shopping assistant."},
            {"role":"user","content":prompt}
        ],
        temperature=0.2
    )
    raw = resp.choices[0].message.content.strip()
    print("🔍 Groq Amazon Raw Output:\n", raw)

    m = re.search(r"\[.*\]", raw, re.DOTALL)
    try:
        return ast.literal_eval(m.group()) if m else []
    except Exception as e:
        print("❌ Failed to parse Amazon LLM output:", e)
        return []
