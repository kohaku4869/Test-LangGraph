from langgraph.graph import StateGraph, END, START
from src.graph import BlogPostState
# Import 5 nodes
from src.nodes import plan_node, research_node, write_node, edit_node, publish_node

workflow = StateGraph(BlogPostState)

workflow.add_node("planner", plan_node)
workflow.add_node("researcher", research_node)
workflow.add_node("writer", write_node)
workflow.add_node("editor", edit_node)
workflow.add_node("publisher", publish_node)

workflow.set_entry_point("planner")

workflow.add_edge(START, "planner")
workflow.add_edge("planner", "researcher")
workflow.add_edge("researcher", "writer")
workflow.add_edge("writer", "editor")
workflow.add_edge("editor", "publisher")
workflow.add_edge("publisher", END)

app = workflow.compile()

if __name__ == "__main__":
    topic_input = input("Nhập chủ đề bạn muốn viết blog: ")
    
    initial_state = BlogPostState(topic=topic_input)
    
    print("\n>>> ĐANG VẬN HÀNH DÂY CHUYỀN SẢN XUẤT BLOG...\n")
    final_result = app.invoke(initial_state)
    
    print("\n" + "="*50)
    print("KẾT QUẢ CUỐI CÙNG: (Trong file post.md)")
    print("="*50)
    with open("post.md", "w", encoding="utf-8") as f:
        f.write(final_result['final_content'])