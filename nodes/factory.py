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

def get_dynamic_prompt(agent_name, task_type):
    
    prompts = {
        "Goal": f"You are {agent_name}. A national goal has been set. Suggest specific strategies and policies to achieve it.",
        "Policy": f"You are {agent_name}. Evaluate this proposed policy. Predict its real-world success or failure based on current data.",
        "Crisis": f"You are {agent_name}. A live crisis is occurring. Analyze the immediate damage and long-term risks to your sector."
    }
    return prompts.get(task_type, f"You are {agent_name}, a national strategic analyst.")

def create_thought_node(tools, name):
    
    def node(state):
        task = state.get("task_type", "Goal")
        
        dynamic_sys_prompt = get_dynamic_prompt(name.capitalize(), task)
        
        prompt_template = ChatPromptTemplate.from_messages([
            ("system", dynamic_sys_prompt),
            MessagesPlaceholder(variable_name="messages"),
        ])
        
        chain = prompt_template | llm_8b.bind_tools(tools)
        
       
        process_steps = {
            "Goal": [
                f"{name.capitalize()} is identifying key growth drivers for this target...",
                f"Checking resource feasibility for national implementation...",
                f"Formulating a {task}-oriented strategic briefing."
            ],
            "Policy": [
                f"{name.capitalize()} is cross-referencing past policy outcomes...",
                f"Running simulation on '{task}' success probability...",
                f"Identifying potential sector-specific bottlenecks."
            ],
            "Crisis": [
                f"{name.capitalize()} is calculating immediate damage impact...",
                f"Assessing escalation risks in the '{task}' sector...",
                f"Prioritizing urgent mitigation protocols."
            ]
        }
        
        
        thought = process_steps.get(task, [f"{name.capitalize()} is analyzing the situation..."])

        result = chain.invoke(state)
        
        return {
            "messages": [result],
            "agent_insights": {name: result.content},
            "thinking_logs": {name: thought} 
        }
    return node
