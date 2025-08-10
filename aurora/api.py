from fastapi import FastAPI
from pydantic import BaseModel
from .celery_app import add

app = FastAPI(title="Aurora Orchestrator")

class AddReq(BaseModel):
    x: int
    y: int

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/enqueue/add")
def enqueue_add(req: AddReq):
    job = add.delay(req.x, req.y)
    return {"task_id": job.id}

@app.get("/result/{task_id}")
def get_result(task_id: str):
    res = add.AsyncResult(task_id)
    return {"state": res.state, "result": res.result if res.ready() else None}
