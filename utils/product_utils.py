def extract_product_info(item):
    try:
        title = item.query_selector("h2 span").inner_text()
        price_elem = item.query_selector("span.a-price-whole")
        price = int(price_elem.inner_text().replace(",", "")) if price_elem else None
        link = item.query_selector("h2 a").get_attribute("href")
        return {
            "title": title,
            "price": price,
            "link": f"https://www.amazon.in{link}" if link else ""
        }
    except:
        return {}


def extract_flipkart_info(item):
    try:
        title_elem = item.query_selector("._4rR01T") or item.query_selector("a.s1Q9rs")
        price_elem = item.query_selector("._30jeq3")

        title = title_elem.inner_text().strip() if title_elem else None
        price_text = price_elem.inner_text().strip() if price_elem else None
        price = int(price_text.replace("₹", "").replace(",", "")) if price_text else None
        link = title_elem.get_attribute("href") if title_elem else None

        if title and price and link:
            return {
                "title": title,
                "price": price,
                "link": f"https://www.flipkart.com{link}"
            }

    except Exception as e:
        print(f"   → Skipped card (error: {e})")
        return {}


def extract_flight_info(page, site):
    try:
        if site == "makemytrip":
            cards = page.query_selector_all("div.fli-list")
            results = []
            for card in cards:
                name_elem = card.query_selector("span.airlineInfo-sctn") or card.query_selector("span.flightName")
                price_elem = card.query_selector("p.blackText.fontSize18.blackFont.white-space-no-wrap")

                name = name_elem.inner_text().strip() if name_elem else ""
                price_text = price_elem.inner_text().replace("₹", "").replace(",", "").strip() if price_elem else ""
                price = int(price_text) if price_text.isdigit() else None

                if name and price:
                    results.append({
                        "flight": name,
                        "price": price,
                        "source": site.capitalize()
                    })
            return results

        elif site == "yatra":
            cards = page.query_selector_all("div.flight-det")
            results = []
            for card in cards:
                name_elem = card.query_selector("span.name")
                price_elem = card.query_selector("div.price span.amount")

                name = name_elem.inner_text().strip() if name_elem else ""
                price_text = price_elem.inner_text().replace(",", "").strip() if price_elem else ""
                price = int(price_text) if price_text.isdigit() else None

                if name and price:
                    results.append({
                        "flight": name,
                        "price": price,
                        "source": site.capitalize()
                    })
            return results

        else:
            print(f"❌ Unsupported site: {site}")
            return []

    except Exception as e:
        print(f"⚠️ Error in extract_flight_info for {site}: {e}")
        return []

