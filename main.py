from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import date, timedelta
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List

app = FastAPI(title="Smart Task Planner", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GoalRequest(BaseModel):
    goal: str = Field(..., example="Launch a product in 2 weeks")

class Task(BaseModel):
    task: str
    depends_on: Optional[str] = None
    duration_days: int
    start: str
    end: str

class PlanResponse(BaseModel):
    goal: str
    prompt_used: str
    tasks: List[Task]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate_plan/", response_model=PlanResponse)
def generate_plan(goal_request: GoalRequest):
    goal_text = goal_request.goal
    prompt_used = "Break down this goal into actionable tasks with suggested deadlines and dependencies."

    tasks = [
        {
            "task": "Define project scope",
            "depends_on": None,
            "duration_days": 2,
            "start": str(date.today()),
            "end": str(date.today() + timedelta(days=2)),
        },
        {
            "task": "Design prototype",
            "depends_on": "Define project scope",
            "duration_days": 3,
            "start": str(date.today() + timedelta(days=2)),
            "end": str(date.today() + timedelta(days=5)),
        },
        {
            "task": "Test and launch",
            "depends_on": "Design prototype",
            "duration_days": 5,
            "start": str(date.today() + timedelta(days=5)),
            "end": str(date.today() + timedelta(days=10)),
        },
    ]

    return {"goal": goal_text, "prompt_used": prompt_used, "tasks": tasks}
