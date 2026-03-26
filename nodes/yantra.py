from nodes.factory import create_thought_node
from tools import fetch_indian_news


yantra_node = create_thought_node([fetch_indian_news], "You are Yantra. Focus on digital infrastructure and deep-tech.", "yantra")