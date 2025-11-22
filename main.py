from src.nodes import test
from src.graph import State
from langgraph.graph import StateGraph, END, START

flow = StateGraph(State)
flow.add_node("test", test)
flow.add_edge(START, "test")
flow.add_edge("test", END)

app = flow.compile()
result = app.invoke({"messages": "Hello, how are you?"})
print(result["messages"])


