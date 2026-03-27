import operator
from typing import Annotated, TypedDict, List, Dict, Any

def merge_dicts(left: dict, right: dict) -> dict:
    if not left:
        return right
    if not right:
        return left
    return {**left, **right}

class SutraState(TypedDict):
    query: str
    task_type:str
    messages: Annotated[List[Any], operator.add]
    raw_data: Annotated[Dict[str, Any], merge_dicts]
    agent_insights: Annotated[Dict[str, str], merge_dicts]
    risk_scores: Annotated[Dict[str, float], merge_dicts]
    thinking_logs: Annotated[Dict[str, List[str]], merge_dicts]
    adversary_critique: str
    final_report: str