from .models import model
from .graph import State

def edit_node(state: State) -> State:
    print("--Editing--")
    msg = f"Hãy đóng vai biên tập viên khó tính. Kiểm tra bài viết sau và chỉ sửa các lỗi ngữ pháp hoặc làm văn phong mượt mà hơn (giữ nguyên ý chính): \n\n {state.draft_content}"
    response = model.invoke(msg)
    state.fix_content = response
    return state