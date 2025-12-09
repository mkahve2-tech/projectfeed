import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Kaynak URL (Archaeology projects sayfası)
URL = "https://researchportal.helsinki.fi/en/organisations/archaeology/projects/"
html = requests.get(URL).text
soup = BeautifulSoup(html, "lxml")

items = []
for proj in soup.select(".rendering_upmproject_short"):
    # Başlık
    title = proj.select_one(".title span").text.strip()
    # Link
    link = proj.select_one(".title a")["href"]
    # Dönem bilgisi
    period = proj.select_one(".period").text.strip() if proj.select_one(".period") else ""
    # Yayın tarihi (şu anki zaman)
    pubDate = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

    items.append(f"""
    <item>
