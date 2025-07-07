This is a lightweight web scraping tool built with Python to extract company details from either a search query or a list of seed URLs.

## 🚀 Features
- Input a search query (e.g., "top SaaS startups India") or paste seed URLs
- Extracts:
  - Company name
  - Website
  - Contact info (email, phone)
  - Meta description
  - Social media links (LinkedIn, Twitter, Facebook)
- Outputs results to `output.json`

## 🧰 Tech Stack
- Python 3
- `requests`, `BeautifulSoup` for scraping
- `duckduckgo_search` for query-based discovery

## 📦 Installation
```bash
pip install -r requirements.txt
```

## 📝 Usage
```bash
python main.py
```
Follow the prompts to enter a search query or paste URLs.

## 📁 Output
- A file named `output.json` will be generated with extracted company information.

## ✅ Example Output
```json
[
  {
    "url": "https://example.com",
    "company_name": "Example Corp",
    "emails": ["info@example.com"],
    "phones": ["+1 800 123 4567"],
    "description": "We help companies...",
    "social_links": ["https://linkedin.com/company/example"]
  }
]
```

## 🔧 Notes
- For dynamic JavaScript-heavy sites, consider adding Selenium
- This version focuses on core functionality; tech stack, projects, and competitors can be added in later enhancements

---

Feel free to expand with more scraping logic, UI, or data analysis features!

---

**Author**: Diwansh Sood
**Assignment**: Unicraft Tech Internship