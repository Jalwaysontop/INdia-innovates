from nodes.factory import create_thought_node
from tools import get_economic_indicators, fetch_indian_news

artha_node = create_thought_node(
    tools=[get_economic_indicators, fetch_indian_news],
    system_prompt="You are Artha (Econ). Use indicators and news to analyze India's economic health.",
    name="artha"
)