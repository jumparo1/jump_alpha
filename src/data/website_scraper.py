import requests
from bs4 import BeautifulSoup

def scrape_project_website(url: str) -> dict:
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title else "N/A"
        meta_desc = soup.find("meta", attrs={"name": "description"})
        description = meta_desc["content"].strip() if meta_desc else "N/A"
        h1 = soup.find("h1")
        h1_text = h1.text.strip() if h1 else "N/A"
        first_p = soup.find("p")
        paragraph = first_p.text.strip() if first_p else "N/A"

        return {
            "title": title,
            "description": description,
            "headline": h1_text,
            "paragraph": paragraph
        }
    except Exception as e:
        return {
            "title": "Error",
            "description": str(e),
            "headline": "N/A",
            "paragraph": "N/A"
        } 