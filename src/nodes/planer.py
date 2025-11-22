from .models import model
from .graph import State

def plan_node(state: State) -> State:
    print("--Planning--")
    msg = f"Lập dàn ý ngắn gọn về 3 mục chính về chủ đề {state.topic} cho bài blog. Chỉ trả lời dàn ý, không trả lời thêm thông tin khác."
    response = model.invoke(msg)
    state.plan = response
    return state
