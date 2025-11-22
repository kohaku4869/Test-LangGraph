from .models import model
from .graph import State

def plan_node(state: State) -> State:
    print("--Planning--")
    msg = f"Lập dàn ý về chủ đề {state.topic}"
