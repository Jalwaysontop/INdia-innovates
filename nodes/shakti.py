from nodes.factory import create_thought_node
from tools import get_resource_status, fetch_indian_news

shakti_node = create_thought_node([get_resource_status, fetch_indian_news],"shakti")