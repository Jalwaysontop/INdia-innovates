from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from graph import sutra_engine  
import uuid

app = FastAPI(title="Sutra Sovereign API")

class QueryRequest(BaseModel):
    user_query: str

@app.post("/analyze")
async def analyze_query(request: QueryRequest):
    
    initial_state = {
        "query": request.user_query,
        "messages": [],
        "agent_insights": {},
        "thinking_logs": {},
        "adversary_critique": "",
        "final_report": ""
    }
    
    
    result = sutra_engine.invoke(initial_state)
    
    return {
        "report": result["final_report"],
        "logs": result["thinking_logs"],
        "insights": result["agent_insights"]
    }