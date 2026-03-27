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
    print("\nSUTRA ENGINE: LOCAL COMMAND CONSOLE")
    
    print("Modes: 1: Goal | 2: Policy | 3: Crisis")
    choice = input("Select Mission Mode (1-3): ")
    modes = {"1": "Goal", "2": "Policy", "3": "Crisis"}
    selected_task = modes.get(choice, "Goal")

    query = input(f"Enter {selected_task} Query: ")

    initial_state = {
        "query": query,
        "task_type": selected_task,
        "messages": [],
        "agent_insights": {},
        "thinking_logs": {},
        "final_report": ""
    }

        

    print(f"\n[SYSTEM]: Activating Specialist Nodes in {selected_task} mode...")
    print("-" * 30 + "\nLIVE THOUGHT STREAM\n" + "-" * 30)

    final_state_data = None

    for output in sutra_engine.stream(initial_state):
        for key, value in output.items():
            if "thinking_logs" in value:
                logs = value["thinking_logs"].get(key, [])
                for log in logs:
                    print(f"[{key.upper()}]: {log}")
            
            if key == "supervisor":
                final_state_data = value

    if final_state_data:
        print("\n" + "="*60 + "\nFINAL STRATEGIC REPORT\n" + "="*60)
        print(final_state_data.get("final_report", "No report generated."))