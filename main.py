import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any, Optional

from graph import sutra_engine
from state import SutraState

app = FastAPI(
    title="IntelGraph Sovereign API",
    description="Strategic Intelligence Bridge for National Policy Analysis",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StrategicRequest(BaseModel):
    query: str
    task_type: str 

@app.post("/analyze")
async def run_strategic_analysis(request: StrategicRequest):
    
    initial_state = {
        "query": request.query,
        "task_type": request.task_type,
        "messages": [],
        "raw_data": {},
        "agent_insights": {},
        "risk_scores": {},
        "thinking_logs": {},
        "adversary_critique": "",
        "final_report": ""
    }

    try:
        final_state = sutra_engine.invoke(initial_state)
        
        return final_state

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Strategic Engine Error: {str(e)}")

@app.get("/health")
async def health_check():
    return {"status": "Sovereign Cabinet is Online", "engine": "Llama-3.1-8b-Groq"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)