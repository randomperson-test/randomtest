import streamlit as st

st.set_page_config(page_title="Ôn tập Python", layout="wide")

st.sidebar.title("MENU BÀI HỌC")

bai1 = st.sidebar.button("Bài 1")
bai2 = st.sidebar.button("Bài 2")
bai3 = st.sidebar.button("Bài 3")
bai5 = st.sidebar.button("Bài 5")
bai6 = st.sidebar.button("Bài 6")
bai7 = st.sidebar.button("Bài 7")

if bai1:
    st.header("BÀI 1")
    st.write(
        "- Class là bản thiết kế (khuôn mẫu)\n"
        "- Object là đối tượng được tạo từ class\n"
        "- Class chứa thuộc tính và phương thức\n"
        "- Object là thực thể cụ thể\n"
    )

elif bai2:
    st.header("BÀI 2")
    st.write(
        "- Instance method: có self, làm việc với object\n"
        "- Class method: có cls, làm việc với class\n"
        "- Static method: không cần self hoặc cls\n"
    )

elif bai3:
    st.header("BÀI 3")
    st.write(
        "- Getter (@property): lấy giá trị\n"
        "- Setter (@name.setter): gán giá trị có kiểm soát\n"
        "- Deleter (@name.deleter): xóa thuộc tính\n"
    )

elif bai5:
    st.header("BÀI 5")
    st.write(
        "- Streamlit dùng để tạo web bằng Python\n"
        "- st.title(): tiêu đề\n"
        "- st.write(): viết nội dung\n"
        "- st.sidebar(): tạo menu bên trái\n"
    )

elif bai6:
    st.header("BÀI 6")
    st.write(
        "- st.button(): tạo nút bấm\n"
        "- st.progress(): thanh tiến độ\n"
        "- st.balloons(): hiệu ứng bóng bay\n"
    )

    if st.button("Ví dụ"):
        st.progress(100)
        st.balloons()

elif bai7:
    st.header("BÀI 7")
    st.write(
        "- st.image(): hiển thị hình ảnh\n"
        "- st.audio(): phát âm thanh\n"
        "- st.video(): phát video\n"
    )

    st.write("Video ví dụ")
    st.video("https://www.youtube.com/watch?v=nc4tcJL6-W0")

    st.write("Ảnh ví dụ")
    st.image("https://static.wixstatic.com/media/a137e0_70efca2877e4406bb4d711ba46104892~mv2.png")
