from .models import model
from .graph import State

def research_node(state: State) -> State:
    print("--Researching--")
    msg = f"Dựa trên dàn ý này {state.plan}, cung cấp 3 sự thật thú vị hoặc số liệu liên quan"
    response = model.invoke(msg)
    state.research_data = response
    return state
