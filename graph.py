from langgraph.graph import StateGraph, END
from state import SutraState

from nodes.artha import artha_node
from nodes.raksha import raksha_node
from nodes.shakti import shakti_node
from nodes.yantra import yantra_node
from nodes.samaj import samaj_node
from nodes.vikriti import vikriti_node
from nodes.supervisor import supervisor_node


workflow = StateGraph(SutraState)

workflow.add_node("artha", artha_node)
workflow.add_node("raksha", raksha_node)
workflow.add_node("shakti", shakti_node)
workflow.add_node("yantra", yantra_node)
workflow.add_node("samaj", samaj_node)
workflow.add_node("vikriti", vikriti_node)
workflow.add_node("supervisor", supervisor_node)

workflow.set_entry_point("artha")

workflow.add_edge("artha", "raksha")
workflow.add_edge("raksha", "shakti")
workflow.add_edge("shakti", "yantra")
workflow.add_edge("yantra", "samaj")

workflow.add_edge("samaj", "vikriti")

workflow.add_edge("vikriti", "supervisor")

workflow.add_edge("supervisor", END)

sutra_engine = workflow.compile()

if __name__ == "__main__":
    print("\n" + "="*60)
    print("SUTRA ENGINE: NATIONAL STRATEGIC INTELLIGENCE (2026)")
    print("="*60)

    while True:
        user_query = input("\nEnter National Query (or 'exit'): ")
        if user_query.lower() in ["exit", "quit"]:
            break

        
        initial_state = {
            "query": user_query,
            "messages": [],
            "agent_insights": {},
            "thinking_logs": {},
            "adversary_critique": "",
            "final_report": ""
        }

        print("\n[SYSTEM]: Activating Specialist Nodes...")
        
        
        final_state = sutra_engine.invoke(initial_state)

        
        print("\n" + "-"*30)
        print("LIVE THOUGHT STREAM")
        print("-"*30)
        
        for agent, thoughts in final_state["thinking_logs"].items():
            for thought in thoughts:
                print(f"[{agent.upper()}]: {thought}")

        print("\n" + "="*60)
        print("FINAL STRATEGIC REPORT")
        print("="*60)
        print(final_state["final_report"])
        print("="*60)