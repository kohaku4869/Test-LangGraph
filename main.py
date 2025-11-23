from langgraph.graph import StateGraph, END, START
from src.graph import BlogPostState
# Import 5 nodes
from src.nodes import plan_node, research_node, write_node, edit_node, publish_node

# 1. Khởi tạo Graph
workflow = StateGraph(BlogPostState)

# 2. Thêm 5 Nodes vào bảng mạch
workflow.add_node("planner", plan_node)
workflow.add_node("researcher", research_node)
workflow.add_node("writer", write_node)
workflow.add_node("editor", edit_node)
workflow.add_node("publisher", publish_node)

# 3. Nối dây (Flow tuyến tính)
# Start -> Planner
workflow.set_entry_point("planner")

# Planner -> Researcher -> Writer -> Editor -> Publisher -> END
workflow.add_edge(START, "planner")
workflow.add_edge("planner", "researcher")
workflow.add_edge("researcher", "writer")
workflow.add_edge("writer", "editor")
workflow.add_edge("editor", "publisher")
workflow.add_edge("publisher", END)

# 4. Compile
app = workflow.compile()

# --- CHẠY THỬ ---
if __name__ == "__main__":
    topic_input = input("Nhập chủ đề bạn muốn viết blog: ")
    
    # Khởi tạo state ban đầu (chỉ cần topic)
    initial_state = BlogPostState(topic=topic_input)
    
    # Chạy
    print("\n>>> ĐANG VẬN HÀNH DÂY CHUYỀN SẢN XUẤT BLOG...\n")
    final_result = app.invoke(initial_state)
    
    # In kết quả cuối cùng
    print("\n" + "="*50)
    print("KẾT QUẢ CUỐI CÙNG (TỪ PUBLISHER):")
    print("="*50)
    # Vì kết quả trả về là dict (do invoke), ta truy cập key 'final_content'
    print(final_result['final_content'])
    
    # Bạn cũng có thể xem lại quá trình (State vẫn lưu giữ đủ)
    print("\n--- (Debug Info) ---")
    print(f"Dàn ý gốc: {len(final_result['outline'])} ký tự")
    print(f"Số liệu tìm được: {len(final_result['research_data'])} ký tự")