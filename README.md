# AI Query Automation

Welcome to **AI Query Automation**, your personal shopping and travel assistant powered by Groq. This tool lets you ask in plain English for product recommendations on Amazon and Flipkart, or flight price estimates—all without the headaches of web scraping.

## 🚀 What It Does

* **Understands your queries**: Ask for products (e.g., “smartphones under ₹20,000”) or flights (e.g., “ticket from Bangalore to SF on 2025-07-25”).
* **Groq‑powered parsing**: Converts your words into structured data (category, price limit, sites, or flight details).
* **Estimates results**: Uses Groq to generate plausible product lists or flight prices in JSON format.
* **Excel reports**: Saves your results as a neat `output.xlsx`, ready to review or share.

## 🛠️ Setup & Installation

1. **Clone this repo**:

   ```bash
   git clone https://github.com/your-username/ai-query-automation.git
   cd ai-query-automation
   ```
2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```
3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```
4. **Add your Groq API key**:

   * Create a file named `.env` in the project root.
   * Add this line:

     ```ini
     GROQ_API_KEY=your_groq_api_key_here
     ```

## ▶️ How to Use

1. **Run the main script**:

   ```bash
   python main.py
   ```
2. **Type your query** when prompted. Examples:

   * `Find me smartphones under ₹20000 on Amazon`
   * `Show me laptops under ₹50000 on Flipkart`
   * `What’s the price of ticket from Bangalore to SF on 2025-07-25`
3. **Review your results**:

   * The console shows the parsed query and generated results.
   * Check `output.xlsx` for a formatted report.

## 🔍 Example Output

| Title              | Price | Link                                                      | Source       |
| ------------------ | ----- | --------------------------------------------------------- | ------------ |
| Samsung Galaxy M12 | 14999 | [https://www.amazon.in/](https://www.amazon.in/)...       | Amazon       |
| Mi Redmi Note 10   | 11999 | [https://www.flipkart.com/](https://www.flipkart.com/)... | Flipkart     |
| IndiGo 6E-101      | 4899  | Groq Estimate                                             | GroqEstimate |

## 🛡️ Tips & Troubleshooting

* **Empty results**: If nothing appears, double‑check your query or API key. Groq needs clear instructions.
* **Flight fields missing**: You’ll be prompted for origin, destination, or date if Groq doesn’t pick them up.
* **API errors**: Ensure your Groq key has quota and is valid.

## 💡 Next Steps

* Swap in real APIs for live data (SerpApi, RapidAPI, Skyscanner) while keeping Groq parsing.
* Add hotel search, round‑trip flights, or product comparisons.
* Cache responses to reduce API calls and speed up results.

---

Made with ❤️ by Abhijit Maharana. Happy automating!
