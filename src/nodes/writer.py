from src.models import model
from src.graph.state import BlogPostState

def write_node(state: BlogPostState) -> BlogPostState:
    print("--Writing--")
    msg = f"Viết bài blog về chủ đề {state.topic} với dàn ý {state.outline} và dữ liệu nghiên cứu {state.research_data}"
    response = model.invoke(msg)
    state.draft_content = response.content
    return state

