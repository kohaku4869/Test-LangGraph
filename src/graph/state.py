from pydantic import BaseModel
from typing import List,Dict, Annotated
from langgraph.graph.message import add_messages

class State(BaseModel):
    topic: str

    outline: Optional[str] = None
    research_data: Optional[str] = None
    draft_content: Optional[str] = None
    fix_content: Optional[str] = None
    final_content: Optional[str] = None



