from nodes.factory import llm_8b
from state import SutraState

def get_adversarial_prompt(task_type, insights):

    prompts = {
        "Goal": f"Identify why these strategies are UNREALISTIC or mathematically impossible. Focus on resource gaps: {insights}",
        "Policy": f"Identify the UNINTENDED CONSEQUENCES of this policy. How will it backfire or be exploited? Insights: {insights}",
        "Crisis": f"Identify the ESCALATION RISKS. Why is this response too slow or likely to make the problem worse? Insights: {insights}"
    }
    return prompts.get(task_type, f"Find the fatal flaw in these insights: {insights}")

def vikriti_node(state: SutraState):
    task = state.get("task_type", "Goal")
    insights = state.get("agent_insights", {})

    attack_prompt = get_adversarial_prompt(task, insights)
    
    thought = [f"Vikriti is scanning for '{task}' vulnerabilities...", 
               "Executing a red-team assault on the ministerial consensus."]

    result = llm_8b.invoke(attack_prompt)

    return {
        "adversary_critique": result.content,
        "thinking_logs": {"vikriti": thought}
    }