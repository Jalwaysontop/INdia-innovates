from nodes.factory import create_thought_node
from tools import fetch_indian_news

raksha_node = create_thought_node(
    tools=[fetch_indian_news],
    system_prompt="You are Raksha (Security). Analyze border security and cyber threats using news alerts.",
    name="raksha"
)