from nodes.factory import create_thought_node
from tools import fetch_indian_news, get_resource_status

raksha_node = create_thought_node(
    tools=[fetch_indian_news, get_resource_status],
    name="raksha"
)
