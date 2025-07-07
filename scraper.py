import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def load_dynamic_page(url):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(3)
        html = driver.page_source
    finally:
        driver.quit()
    return html

def extract_tech_stack(html):
    known_techs = ['React', 'Next.js', 'Angular', 'Vue', 'Node.js', 'Django', 'Flask', 'Laravel', 'MongoDB', 'PostgreSQL', 'MySQL', 'Firebase', 'AWS', 'Azure', 'GCP']
    return [tech for tech in known_techs if tech.lower() in html.lower()]

def extract_focus_areas(soup):
    focus_keywords = ['solution', 'product', 'service', 'platform', 'focus', 'offering']
    sections = soup.find_all(['h1', 'h2', 'h3', 'p'])
    focus = []
    for section in sections:
        text = section.get_text(strip=True).lower()
        if any(keyword in text for keyword in focus_keywords):
            focus.append(section.get_text(strip=True))
    return list(set(focus))[:5]


def extract_market_positioning(soup):
    tags = soup.find_all(['p', 'h1', 'h2', 'h3'])
    for tag in tags:
        text = tag.get_text(strip=True)
        if any(phrase in text.lower() for phrase in ['leading', 'trusted by', '#1', 'top']):
            return text
    return ""

def extract_competitors(html):
    competitors = []
    pattern = r'(?:vs\.|alternative to|compared to)\s+([A-Za-z0-9\s&]+)'
    matches = re.findall(pattern, html, re.IGNORECASE)
    for match in matches:
        competitors.append(match.strip())
    return list(set(competitors))


def extract_company_info(url):
    info = {'url': url}
    try:
        res = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(res.text, 'html.parser')

       
        info['company_name'] = soup.title.string.strip() if soup.title else ''
        info['emails'] = re.findall(r"[\w\.-]+@[\w\.-]+", res.text)
        info['phones'] = re.findall(r"\+?\d[\d\s\-]{8,}\d", res.text)
        desc = soup.find('meta', attrs={"name": "description"})
        info['description'] = desc['content'].strip() if desc and desc.get('content') else ''
        social_links = []
        for a in soup.find_all('a', href=True):
            if any(site in a['href'] for site in ['linkedin.com', 'twitter.com', 'facebook.com']):
                social_links.append(a['href'])
        info['social_links'] = list(set(social_links))


        info['tech_stack'] = extract_tech_stack(res.text)
        info['focus_areas'] = extract_focus_areas(soup)
        info['market_positioning'] = extract_market_positioning(soup)

        
        info['competitors'] = extract_competitors(res.text)

    except Exception as e:
        info['error'] = str(e)

    return info
