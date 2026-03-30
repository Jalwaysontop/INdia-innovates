import os
import re
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from state import SutraState
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()

llm_8b = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.1,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

def get_dynamic_prompt(agent_name, task_type):
    base_instruction = (
        f"You are {agent_name}. ONLY use the provided tools. "
        "If you need to call multiple tools, call them ONE BY ONE. "
        "Do not concatenate multiple tool calls in a single turn. "
        "Wait for the output of one tool before requesting the next."
    )

    prompts = {
        "Goal": f"{base_instruction} Focus on long-term strategy for this goal.",
        "Policy": f"{base_instruction} Analyze the impact and success probability.",
        "Crisis": f"{base_instruction} Prioritize immediate resource status and damage control."
    }

    return prompts.get(task_type, base_instruction)


def create_thought_node(tools, name):
    def node(state: SutraState):
        task = state.get("task_type", "Goal")
        name_key = name.lower()

        all_logs = {
            "artha":      ["Analyzing fiscal multipliers", "Scanning knowledge graph", "Optimizing capital flow"],
            "raksha":     ["Modeling strategic deterrence", "Scanning knowledge graph", "Assessing border integrity"],
            "samaj":      ["Monitoring social sentiment", "Scanning knowledge graph", "Evaluating welfare impact"],
            "shakti":     ["Mapping energy sustainability", "Scanning knowledge graph", "Optimizing power grids"],
            "yantra":     ["Scanning tech scalability", "Scanning knowledge graph", "Auditing automation"],
            "vikriti":    ["Identifying structural decay", "Scanning knowledge graph", "Simulating chaos vectors"],
            "supervisor": ["Synthesizing reports", "Scanning knowledge graph", "Aligning ministerial goals"]
        }

        thoughts = all_logs.get(name_key, ["Processing", "Scanning knowledge graph"])
        thought_str = " | ".join(thoughts)

        sys_prompt = (
            f"You are {name.capitalize()}. Use provided tools ONLY. "
            "CRITICAL: Do not use asterisks (*), bolding, or markdown. "
            "Provide your response as a single, clean paragraph of plain text."
        )

        prompt_template = ChatPromptTemplate.from_messages([
            ("system", sys_prompt),
            MessagesPlaceholder(variable_name="messages"),
        ])

        chain = prompt_template | llm_8b.bind_tools(tools)
        result = chain.invoke(state)

        clean_text = result.content.replace("*", "").strip()
        full_string = f"{name.capitalize()}: [{thought_str}] >> {clean_text}"

        return {
            "messages": [result],
            "agent_insights": {name.capitalize(): full_string},
            "thinking_logs": {name.capitalize(): thoughts}
        }
    return node