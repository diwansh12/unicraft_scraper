import argparse
import json
from search import get_urls_from_query
from scraper import extract_company_info
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


def run_scraper(query=None, urls=None):
    if query:
        urls = get_urls_from_query(query)
    elif urls:
        urls = [url.strip() for url in urls.split(',')]
    else:
        print("❗ Provide either --query or --urls.")
        return

    results = []
    for url in urls:
        info = extract_company_info(url)
        results.append(info)

    with open("output.json", "w") as f:
        json.dump(results, f, indent=4)

    print(f"\n✅ Scraped {len(results)} companies. Results saved to output.json")


def scheduled_job():
    print(f"\n⏰ Running scheduled scrape at {datetime.now()}")
    run_scraper(query="top SaaS companies India")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Unicraft Scraper")
    parser.add_argument('--query', help='Search query (e.g., "top SaaS companies India")')
    parser.add_argument('--urls', help='Comma-separated seed URLs')
    parser.add_argument('--schedule', action='store_true', help='Run this scraper on schedule')
    args = parser.parse_args()

    if args.schedule:
        scheduler = BlockingScheduler()
        scheduler.add_job(scheduled_job, 'interval', hours=6)
        print("🔁 Scheduler started. Scraping every 6 hours...")
        scheduler.start()
    else:
        run_scraper(query=args.query, urls=args.urls)
