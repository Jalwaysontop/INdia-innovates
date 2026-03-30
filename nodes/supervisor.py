import re
from nodes.factory import llm_8b
from state import SutraState

def clean_output(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r"\*{1,3}([^*]+)\*{1,3}", r"\1", text)
    text = text.replace("*", "")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    lines = [line.rstrip() for line in text.split("\n")]
    return "\n".join(lines).strip()


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

    summary_prompt = f"""You are the Sutra Samanvaya, India's Chief National Coordinator and strategic synthesis engine.

MISSION TYPE: {task}
CORE QUERY: {user_query}

MINISTER REPORTS:
{insights}

ADVERSARIAL CRITIQUE FROM VIKRITI:
{critique}

YOUR TASK:
{task_style}

FORMATTING RULES — STRICTLY FOLLOW THESE:
- Use plain section headers like "SECTION TITLE:" on their own line (ALL CAPS, followed by a colon).
- Under each header, write 2-4 concise sentences or a short numbered list.
- Do NOT use markdown asterisks, hashes (#), dashes for bullets, or any other markdown symbols.
- Separate sections with a blank line.
- End with a section called "SUTRA VERDICT:" that summarises in 2 sentences.
- MANDATORY: Address Vikriti's critique directly in one of your sections. If a fatal flaw was found, propose a concrete countermeasure or acknowledge the high risk.
"""

    response = llm_8b.invoke(summary_prompt)
    cleaned = clean_output(response.content)

    return {
        "final_report": cleaned,
        "thinking_logs": {"supervisor": thought}
    }