from llm_parser import parse_query
from amazon_scraper import scrape_amazon
from flipkart_scraper import scrape_flipkart
from flight_scraper import scrape_flight_prices
from excel_writer import write_to_excel

def main():
    query = input("Enter your search query: ")
    parsed = parse_query(query)
    print("🔍 Parsed query:", parsed)

    results = []

    if parsed.get("category") == "flight":
        print("Estimating flight prices via Groq…")
        results = scrape_flight_prices(
            parsed.get("from_city"),
            parsed.get("to_city"),
            parsed.get("date")
        )
    else:
        if "amazon" in [s.lower() for s in parsed.get("sites", [])]:
            print("Scraping Amazon...")
            results += scrape_amazon(parsed.get("category"), parsed.get("max_price"))

        if "flipkart" in [s.lower() for s in parsed.get("sites", [])]:
            print("Scraping Flipkart...")
            results += scrape_flipkart(parsed.get("category"), parsed.get("max_price"))

    print("Results:\n", results)

    if results:
        write_to_excel(results)
    else:
        print("⚠️ No data to write.")

if __name__ == "__main__":
    main()
