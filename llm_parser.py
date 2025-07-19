import os
import ast
import re
from groq import Groq
from dotenv import load_dotenv

# Load env vars
load_dotenv()

# Initialize Groq client with your GROQ_API_KEY
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def parse_query(user_query: str) -> dict:
    prompt = f"""
You are an intelligent query parser. Convert the user's shopping or flight request into a structured Python dictionary with keys:
- category (e.g., 'laptop', 'smartphone', or 'flight')
- max_price (integer in INR, if mentioned)
- sites (list of sites like ['amazon', 'flipkart', 'makemytrip', 'yatra'])
- from_city (for flights)
- to_city (for flights)
- date (YYYY-MM-DD, if available)

Example return:
{{"category": "laptop", "max_price": 50000, "sites": ["amazon", "flipkart"]}}

Only output the dictionary, no explanation.
User query: {user_query}
"""

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192"
    )

    content = response.choices[0].message.content.strip()
    print("🔍 LLM Raw Output:\n", content)

    # Try to extract dictionary using regex
    match = re.search(r"\{.*?\}", content, re.DOTALL)

    try:
        return ast.literal_eval(match.group()) if match else {}
    except Exception as e:
        print("❌ Error parsing response:", e)
        return {}
