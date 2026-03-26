import os
import requests
import wbgapi as wb
from langchain_core.tools import tool
from dotenv import load_dotenv

load_dotenv()

@tool
def fetch_indian_news(topic: str):
    
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?q=India+{topic}&sortBy=publishedAt&pageSize=3&apiKey={api_key}"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        if data.get("status") == "ok" and data.get("articles"):
            results = []
            for art in data["articles"]:
                results.append(f"Source: {art['source']['name']}\nHeadline: {art['title']}\nSnippet: {art['description']}")
            return "\n\n".join(results)
        return f"No recent news found for '{topic}'."
    except Exception as e:
        return f"Error fetching news: {str(e)}"

@tool
def get_economic_indicators():
    
    try:
        indicators = {'GDP_Growth': 'NY.GDP.MKTP.KD.ZG', 'Inflation': 'FP.CPI.TOTL.ZG'}
        data = wb.data.DataFrame(indicators.values(), 'IND', mrv=1) # Get Most Recent Value
        
        gdp = data.loc['IND', indicators['GDP_Growth']]
        inf = data.loc['IND', indicators['Inflation']]
        
        return f"Latest India Economic Data (World Bank):\n- Annual GDP Growth: {gdp:.2f}%\n- Annual Inflation: {inf:.2f}%"
    except Exception as e:
        return f"Economic Data Error: {str(e)}"

@tool
def get_resource_status(sector: str):
    stats = {
        "energy": "Grid Status: Stable. Renewable Share: 42%. Solar Capacity: 75GW (Target 100GW).",
        "water": "Groundwater Level: Critical in North India. Reservoir storage at 85% of 10-year average.",
        "agriculture": "Crop Health: Good. Monsoon impact: Normal. Fertilizer stocks: Sufficient for Kharif season."
    }
    return stats.get(sector.lower(), "Sector data not available.")