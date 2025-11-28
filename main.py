from langgraph.graph import StateGraph, END, START
from src.graph import BlogPostState
# Import 5 nodes
from src.nodes import plan_node, research_node, write_node, edit_node, publish_node, review_node

workflow = StateGraph(BlogPostState)
# Hàm điều hướng (Router)
def router_logic(state: BlogPostState):
    # Điều kiện 1: Nếu sửa quá 2 lần -> Mệt rồi, cho qua luôn (Dù bài dở)
    if state.revision_count >= 2:
        print("   >>> [ROUTER] Đã sửa quá 2 lần. Duyệt cưỡng ép!")
        return "approve"
    
    # Điều kiện 2: Nếu điểm cao >= 8 -> Duyệt
    if state.reviewer_score >= 8:
        print("   >>> [ROUTER] Điểm tốt. Duyệt!")
        return "approve"
    
    # Còn lại -> Điểm thấp -> Viết lại
    print("   >>> [ROUTER] Điểm thấp. Yêu cầu viết lại!")
    return "retry"

workflow.add_node("planner", plan_node)
workflow.add_node("researcher", research_node)
workflow.add_node("writer", write_node)
workflow.add_node("reviewer", review_node)
workflow.add_node("editor", edit_node)
workflow.add_node("publisher", publish_node)

# workflow.set_entry_point("planner")

workflow.add_edge(START, "planner")
workflow.add_edge("planner", "researcher")
workflow.add_edge("researcher", "writer")
workflow.add_edge("writer", "reviewer")

workflow.add_conditional_edges(
    "reviewer",        
    router_logic,     
    {
        "retry": "writer",      
        "approve": "editor"     
    }
)

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