from nodes.factory import create_thought_node
from tools import get_economic_indicators, fetch_indian_news

artha_node = create_thought_node(
    tools=[fetch_indian_news, get_economic_indicators],
    name="artha"
)