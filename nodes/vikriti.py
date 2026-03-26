from nodes.factory import llm_8b

def vikriti_node(state):
    thought = ["Vikriti is stress-testing the current plan for vulnerabilities..."]
    
    insights = state.get("agent_insights", {})
    prompt = f"Analyze these insights for risks: {insights}. Identify one major flaw."
    
    result = llm_8b.invoke(prompt)
    
    return {
        "adversary_critique": result.content,
        "thinking_logs": {"vikriti": thought}
    }