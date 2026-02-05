from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Auto Project Manager AI")

class ProjectRequest(BaseModel):
    goal: str
    duration_days: int
    team_size: int

@app.get("/")
def root():
    return {
        "message": "Auto Project Manager AI backend is running",
        "status": "active"
    }

@app.post("/generate-plan")
def generate_plan(req: ProjectRequest):
    tasks = [
        {
            "name": "Requirement Analysis",
            "priority": "High",
            "estimated_days": 3,
            "depends_on": []
        },
        {
            "name": "System Design",
            "priority": "High",
            "estimated_days": 4,
            "depends_on": ["Requirement Analysis"]
        },
        {
            "name": "Core Development",
            "priority": "Medium",
            "estimated_days": req.duration_days - 10,
            "depends_on": ["System Design"]
        },
        {
            "name": "Testing & Bug Fixes",
            "priority": "Medium",
            "estimated_days": 3,
            "depends_on": ["Core Development"]
        },
        {
            "name": "Deployment",
            "priority": "High",
            "estimated_days": 2,
            "depends_on": ["Testing & Bug Fixes"]
        }
    ]

    return {
        "goal": req.goal,
        "team_size": req.team_size,
        "duration_days": req.duration_days,
        "tasks": tasks
    }
