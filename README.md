# 🕵️‍♂️ Unicraft Scraper

A powerful, extensible Python scraper that:

- Searches DuckDuckGo or uses seed URLs
- Scrapes company info: emails, phones, descriptions, social links
- Extracts tech stack, market focus, positioning, and competitors
- Handles dynamic (JavaScript) content using Selenium
- Crawls internal pages (like /about, /products)
- Supports command-line usage and automatic scheduling (via APScheduler)

---

## 🚀 Features

- 🔍 DuckDuckGo search integration
- ⚙️ Advanced scraping with BeautifulSoup + Selenium
- 📊 Multi-level insights (tech, focus, market)
- 🔁 Scheduled scraping every 6 hours
- 📦 Outputs clean JSON file (`output.json`)

---

## 🛠 Installation

1. **Clone the repo**:

```bash
git clone https://github.com/YOUR_USERNAME/unicraft_scraper.git
cd unicraft_scraper
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Add `chromedriver.exe`**

- Download from: https://sites.google.com/chromium.org/driver/
- Match it to your installed Chrome version
- Place the `.exe` in the project root

---

## ⚙️ Usage

### Run once with a query:
```bash
python main.py --query "top SaaS companies India"
```

### Run with seed URLs:
```bash
python main.py --urls "https://zerodha.com, https://cred.club"
```

### Run every 6 hours (scheduled):
```bash
python main.py --schedule
```

---

## 📂 Output Format (`output.json`)
```json
{
  "url": "https://example.com",
  "company_name": "Example Inc.",
  "emails": ["info@example.com"],
  "phones": ["+91 12345 67890"],
  "description": "India’s top SaaS platform...",
  "social_links": ["https://linkedin.com/company/example"],
  "tech_stack": ["React", "Node.js", "AWS"],
  "focus_areas": ["Payment automation", "Digital banking"],
  "market_positioning": "Trusted by 200+ businesses",
  "competitors": ["Zoho", "Freshworks"]
}
```

---

## 🧪 Dev Tips

- 🧼 Don't commit `chromedriver.exe` or `output.json`
- Add new tech terms to `extract_tech_stack()` in `scraper.py`
- Add new patterns in `extract_focus_areas()` to improve results

---

## 📌 License

MIT © 2025 Diwansh Sood
