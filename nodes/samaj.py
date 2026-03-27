from nodes.factory import create_thought_node
from tools import fetch_indian_news, get_economic_indicators, get_resource_status

samaj_node = create_thought_node(
    tools=[fetch_indian_news, get_economic_indicators, get_resource_status], 
    name="samaj"
)