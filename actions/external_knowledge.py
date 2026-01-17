import requests
import wikipedia
import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# ---------------- DUCKDUCKGO ----------------
def search_duckduckgo(query):
    try:
        url = "https://api.duckduckgo.com/"
        params = {
            "q": query,
            "format": "json",
            "no_html": 1,
            "skip_disambig": 1
        }
        res = requests.get(url, params=params, timeout=5)
        data = res.json()

        if data.get("AbstractText"):
            return ("DuckDuckGo", data["AbstractText"])
    except:
        pass

    return None


# ---------------- WIKIPEDIA ----------------
def search_wikipedia(query):
    try:
        wikipedia.set_lang("en")
        summary = wikipedia.summary(query, sentences=2)
        return ("Wikipedia", summary)
    except:
        return None


# ---------------- NEWS API ----------------
def search_newsapi(query):
    if not NEWS_API_KEY:
        return None

    try:
        url = "https://newsapi.org/v2/everything"
        params = {
            "q": query,
            "apiKey": NEWS_API_KEY,
            "pageSize": 1,
            "language": "en",
            "sortBy": "relevancy"
        }

        res = requests.get(url, params=params, timeout=5)
        data = res.json()

        if data.get("articles"):
            article = data["articles"][0]
            text = f"{article['title']}\n{article['description']}"
            return ("NewsAPI", text)
    except:
        pass

    return None


# ---------------- MASTER CHAIN ----------------
def external_search(query):
    for search_fn in [search_duckduckgo, search_wikipedia, search_newsapi]:
        result = search_fn(query)
        if result:
            return result

    return None
