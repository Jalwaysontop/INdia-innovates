from nodes.factory import llm_8b
from state import SutraState

def get_synthesis_instructions(task_type):
    
    instructions = {
        "Goal": """
            STYLE: Strategic Roadmap.
            FOCUS: Milestones, resource allocation, and policy requirements.
            HEADERS: 'TARGET FEASIBILITY', 'MINISTERIAL ALIGNMENT', and '5-STEP IMPLEMENTATION ROADMAP'.
        """,
        "Policy": """
            STYLE: Impact Prediction.
            FOCUS: Success vs. Failure probability, unintended consequences, and historical precedents.
            HEADERS: 'PREDICTED OUTCOME', 'STRESS-TEST ANALYSIS', and 'SWOT ANALYSIS (Strengths, Weaknesses, Opportunities, Threats)'.
        """,
        "Crisis": """
            STYLE: Emergency Executive Brief.
            FOCUS: Immediate damage control, risk of escalation, and survival metrics.
            HEADERS: 'IMMEDIATE IMPACT ASSESSMENT', 'VIKRITI RISK ALERTS', and 'EMERGENCY MITIGATION STEPS'.
        """
    }
    return instructions.get(task_type, "Provide a general strategic summary.")

def supervisor_node(state: SutraState):
    task = state.get("task_type", "Goal")
    insights = state.get("agent_insights", {})
    critique = state.get("adversary_critique", "")
    user_query = state.get("query", "")

    thought = [
        f"Samanvaya is synthesizing reports for the '{task}' mission...", 
        f"Countering Vikriti's vulnerabilities with ministerial data."
    ]

    task_style = get_synthesis_instructions(task)
    
    summary_prompt = f"""
    You are the Sutra Samanvaya (Chief National Coordinator). 
    MISSION TYPE: {task}
    
    CORE QUERY: {user_query}
    MINISTER REPORTS: {insights}
    ADVERSARIAL CRITIQUE: {critique}
    
    YOUR INSTRUCTIONS:
    {task_style}
    
    MANDATORY: Address Vikriti's critique directly. If Vikriti found a fatal flaw, 
    propose a solution or acknowledge the high risk of the current path.
    """

    response = llm_8b.invoke(summary_prompt)

    return {
        "final_report": response.content,
        "thinking_logs": {"supervisor": thought}
    }