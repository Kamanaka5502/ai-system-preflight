from pydantic import BaseModel
from typing import List


class SystemIntent(BaseModel):
    system_name: str
    goal: str
    inputs: List[str]
    outputs: List[str]
    invariants: List[str]
    failure_modes: List[str]
    observability_plan: List[str]
    evaluation_criteria: List[str]

