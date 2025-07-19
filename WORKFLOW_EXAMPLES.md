# Workflow Examples

This file demonstrates three real‑world scenarios showing how a user query flows through our system—from natural language to Groq parsing, browser/API automation, and Excel output.

---

## 📄 Example 1: Amazon Laptops Under ₹50,000

**User Query:**

```
Find me laptops under ₹50000 on Amazon
```

**Groq Parses To:**

```json
{
  "category": "laptop",
  "max_price": 50000,
  "sites": ["amazon"]
}
```

**Automation Steps (Playwright MCP):**

1. Navigate to `https://www.amazon.in/s?k=laptop`
2. Wait for results container: `div.s-main-slot[data-component-type='s-search-result']`
3. Scroll the page to load dynamic items
4. Extract top 10 product cards via `extract_product_info()`

**Sample Excel Output (`output.xlsx`):**

| Title            | Price | Link                                                            | Source |
| ---------------- | ----- | --------------------------------------------------------------- | ------ |
| HP Pavilion 15   | 47999 | [https://www.amazon.in/dp/B08](https://www.amazon.in/dp/B08)... | Amazon |
| Dell Inspiron 14 | 49900 | [https://www.amazon.in/dp/B07](https://www.amazon.in/dp/B07)... | Amazon |

---

## 📄 Example 2: Flipkart Smartphones Under ₹20,000

**User Query:**

```
Find me smartphones under ₹20000 on Flipkart
```

**Groq Parses To:**

```json
{
  "category": "smartphone",
  "max_price": 20000,
  "sites": ["flipkart"]
}
```

**Automation Steps (Groq‑only estimate):**

1. Send prompt to Groq asking for top‑selling smartphones under ₹20000.
2. Groq returns a Python list of dicts, e.g.:

```python
[
  {"title": "Redmi Note 11", "price": 15999, "link": "https://www.flipkart.com/...", "source": "Flipkart"},
  {"title": "Realme Narzo 50", "price": 12999, "link": "https://www.flipkart.com/...", "source": "Flipkart"}
]
```

**Sample Excel Output:**

| Title           | Price | Link                                                      | Source   |
| --------------- | ----- | --------------------------------------------------------- | -------- |
| Redmi Note 11   | 15999 | [https://www.flipkart.com/](https://www.flipkart.com/)... | Flipkart |
| Realme Narzo 50 | 12999 | [https://www.flipkart.com/](https://www.flipkart.com/)... | Flipkart |

---

## 📄 Example 3: Flight Ticket Price from Bangalore to SF

**User Query:**

```
What’s the price of ticket from Bangalore to SF on 2025-08-01
```

**Groq Parses To:**

```json
{
  "category": "flight",
  "from_city": "Bangalore",
  "to_city": "SF",
  "date": "2025-08-01",
  "sites": ["makemytrip", "yatra"]
}
```

**Automation Steps (Groq‑only estimate):**

1. Send prompt to Groq for flight estimates.
2. Groq returns a list of estimated flights, e.g.:

```python
[
  {"flight": "IndiGo 6E-101", "price": 4899, "source": "GroqEstimate"},
  {"flight": "Air India AI-172", "price": 5499, "source": "GroqEstimate"}
]
```

**Sample Excel Output:**

| Flight           | Price | Source       |
| ---------------- | ----- | ------------ |
| IndiGo 6E-101    | 4899  | GroqEstimate |
| Air India AI-172 | 5499  | GroqEstimate |

---

Feel free to adapt these workflows or add more scenarios to cover other query types!
