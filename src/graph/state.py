from pydantic import BaseModel
from typing import List,Dict, Optional
from langgraph.graph.message import add_messages

class BlogPostState(BaseModel):
    topic: str

    outline: Optional[str] = None
    research_data: Optional[str] = None
    draft_content: Optional[str] = None
    fix_content: Optional[str] = None
    final_content: Optional[str] = None

    revision_count: int = 0
    reviewer_feedback: str = ""
    reviewer_score: int = 0


