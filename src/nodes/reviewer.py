from src.models import model
from src.graph.state import BlogPostState
import time

def review_node(state: BlogPostState) -> BlogPostState:
    print(f"\n--- 🕵️ REVIEWER đang chấm bài (Lần thứ {state.revision_count + 1}) ---")
    time.sleep(2) 
    
    msg = f"""
    Bạn là một nhà phê bình văn học khó tính.
    Hãy đọc bài viết nháp sau đây:
    "{state.draft_content}"
    
    Nhiệm vụ:
    1. Chấm điểm trên thang 10.
    2. Đưa ra nhận xét ngắn gọn để cải thiện (nếu điểm thấp).
    
    Trả về định dạng duy nhất: "DIEM_SO | NHAN_XET"
    Ví dụ: "7 | Bài viết hơi ngắn, cần thêm ví dụ thực tế."
    """
    
    response = model.invoke(msg)
    content = response.content.strip()
    
    # Xử lý kết quả trả về (Cắt chuỗi đơn giản)
    try:
        parts = content.split("|")
        score = int(parts[0].strip())
        feedback = parts[1].strip()
    except:
        # Fallback nếu AI trả về định dạng sai
        score = 5
        feedback = "Cấu trúc bài viết chưa rõ ràng."

    # Cập nhật State
    state.reviewer_score = score
    state.reviewer_feedback += "\n" + feedback
    
    print(f"   => Điểm: {score}/10")
    print(f"   => Feedback: {feedback}")
    
    return state