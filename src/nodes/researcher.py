from src.models import model
from src.graph.state import BlogPostState

def research_node(state: BlogPostState) -> BlogPostState:
    print("--Researching--")
    msg = f"Dựa trên dàn ý này {state.outline}, cung cấp 3 sự thật thú vị hoặc số liệu liên quan"
    response = model.invoke(msg)
    state.research_data = response.content
    return state
