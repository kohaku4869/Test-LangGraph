from src.models import model
from src.graph.state import BlogPostState

def plan_node(state: BlogPostState) -> BlogPostState:
    print("--Planning--")
    msg = f"Lập dàn ý ngắn gọn về 3 mục chính về chủ đề {state.topic} cho bài blog. Chỉ trả lời dàn ý, không trả lời thêm thông tin khác."
    response = model.invoke(msg)
    state.outline = response.content
    return state

