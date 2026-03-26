from nodes.factory import create_thought_node
from tools import fetch_indian_news

samaj_node = create_thought_node([fetch_indian_news], "You are Samaj. Focus on social cohesion and public welfare.", "samaj")