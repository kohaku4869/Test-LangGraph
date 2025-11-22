from .models import model
from .graph import State

def publish_node(state: State) -> State:
    print("--Publishing--")
    msg = f"""
    Bài viết đã xong: {state.draft_content}
    Hãy làm 2 việc:
    1. Đặt một tiêu đề thật kêu (Clickbait).
    2. Format bài viết thành Markdown chuẩn đẹp.
    """
    response = model.invoke(msg)
    state.published_content = response
    return state