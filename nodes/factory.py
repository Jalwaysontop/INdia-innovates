import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()

llm_8b = ChatGroq(
    model="llama-3.1-8b-instant", 
    temperature=0.1, 
    groq_api_key=os.getenv("GROQ_API_KEY")
)

def create_thought_node(tools, system_prompt, name):
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="messages"),
    ])
    
    chain = prompt | llm_8b.bind_tools(tools)

    def node(state):
        thought = [f"{name.capitalize()} is analyzing the situation..."]
        
        result = chain.invoke(state)
        
        return {
            "messages": [result],
            "agent_insights": {name: result.content},
            "thinking_logs": {name: thought}
        }
    return node