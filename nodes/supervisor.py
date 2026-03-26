from nodes.factory import llm_8b
from state import SutraState

def supervisor_node(state: SutraState):
    
    thought = ["Samanvaya is synthesizing all 5 minister reports...", 
               "Integrating Vikriti's stress-test results into the final strategy."]

    insights = state.get("agent_insights", {})
    critique = state.get("adversary_critique", "")
    user_query = state.get("query", "")

    summary_prompt = f"""
    You are the Sutra Samanvaya (National Coordinator). 
    
    User Query: {user_query}
    
    Minister Insights: {insights}
    Adversarial Critique: {critique}
    
    Your Task:
    1. Summarize the collective findings.
    2. Address the flaws pointed out by Vikriti.
    3. Provide a clear, actionable National Strategy.
    
    Format the output with clear headers like 'ECONOMIC IMPACT', 'SECURITY CLEARANCE', and 'FINAL RECOMMENDATION'.
    """

    response = llm_8b.invoke(summary_prompt)

    return {
        "final_report": response.content,
        "thinking_logs": {"supervisor": thought}
    }