from .models import model
from .graph import State

def write_node(state: State) -> State:
    print("--Writing--")
    msg = f"Viết bài blog về chủ đề {state.topic} với dàn ý {state.plan} và dữ liệu nghiên cứu {state.research_data}"
    response = model.invoke(msg)
    state.draft_content = response
    return state
