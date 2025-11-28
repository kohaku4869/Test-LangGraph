from src.models import model
from src.graph.state import BlogPostState

def write_node(state: BlogPostState) -> BlogPostState:
    print("--Writing--")
    if state.reviewer_feedback:
        print(f"   (Đang sửa bài lần {state.revision_count + 1})")
        msg = f"""
        Đây là bài viết cũ của bạn: {state.draft_content}
        
        Nhà phê bình đã chê: "{state.reviewer_feedback}"
        
        HÃY VIẾT LẠI BÀI NÀY TỐT HƠN, khắc phục các điểm bị chê.
        Giữ nguyên chủ đề: {state.topic}.
        """
        # Tăng biến đếm để tránh lặp vô tận
        state.revision_count += 1
    else:
        msg = f"Viết bài blog về chủ đề {state.topic} với dàn ý {state.outline} và dữ liệu nghiên cứu {state.research_data}"
    
    response = model.invoke(msg)
    state.draft_content = response.content
    return state

