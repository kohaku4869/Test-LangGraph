from src.models import model
from src.graph.state import BlogPostState

def publish_node(state: BlogPostState) -> BlogPostState:
    print("--Publishing--")
    msg = f"""
    Bài viết đã xong: {state.fix_content}
    Hãy làm 2 việc:
    1. Đặt một tiêu đề thật kêu (Clickbait).
    2. Format bài viết thành Markdown chuẩn đẹp.
    3. Chỉ trả lời tiêu đề và bài viết, không trả lời thêm thông tin khác.
    """
    response = model.invoke(msg)
    state.final_content = response.content
    return state