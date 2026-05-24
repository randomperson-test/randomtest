import streamlit as st

st.set_page_config(layout="wide")

st.title("Nhà hàng ABC")

st.write("Chào mừng bạn đến với nhà hàng ABC")

st.header("Món khai vị")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):

        st.image(
            "https://tse2.mm.bing.net/th/id/OIP._5wkud0zUQwwf0bCi970MwHaHa?r=0&rs=1&pid=ImgDetMain&o=7&rm=3",
            use_container_width=True
        )

        st.subheader("Khoai tây chiên")

        st.write("35,000 VNĐ")

        sl_khoai = st.number_input(
            "Số lượng khoai tây chiên",
            min_value=0,
            step=1,
            key="khoai"
        )

with col2:
    with st.container(border=True):

        st.image(
            "https://images.unsplash.com/photo-1546069901-ba9599a7e63c",
            use_container_width=True
        )

        st.subheader("Salad")

        st.write("30,000 VNĐ")

        sl_salad = st.number_input(
            "Số lượng salad",
            min_value=0,
            step=1,
            key="salad"
        )

st.header("Món chính")

col3, col4 = st.columns(2)

with col3:
    with st.container(border=True):

        st.image(
            "https://images.unsplash.com/photo-1513104890138-7c749659a591",
            use_container_width=True
        )

        st.subheader("Pizza")

        st.write("120,000 VNĐ")

        sl_pizza = st.number_input(
            "Số lượng pizza",
            min_value=0,
            step=1,
            key="pizza"
        )

with col4:
    with st.container(border=True):

        st.image(
            "https://tse4.mm.bing.net/th/id/OIP.X4ZEMvdkJdohXpSxkUrgUQHaE7?r=0&rs=1&pid=ImgDetMain&o=7&rm=3",
            use_container_width=True
        )

        st.subheader("Phở")

        st.write("50,000 VNĐ")

        sl_pho = st.number_input(
            "Số lượng phở",
            min_value=0,
            step=1,
            key="pho"
        )

st.header("Món tráng miệng")

col5, col6 = st.columns(2)

with col5:
    with st.container(border=True):

        st.image(
            "https://tse2.mm.bing.net/th/id/OIP.oYJD0sMEGoPt6HPo7sd2rgHaE8?r=0&rs=1&pid=ImgDetMain&o=7&rm=3",
            use_container_width=True
        )

        st.subheader("Bánh ngọt")

        st.write("20,000 VNĐ")

        sl_banh = st.number_input(
            "Số lượng bánh ngọt",
            min_value=0,
            step=1,
            key="banh"
        )

with col6:
    with st.container(border=True):

        st.image(
            "https://images.unsplash.com/photo-1619566636858-adf3ef46400b",
            use_container_width=True
        )

        st.subheader("Trái cây")

        st.write("15,000 VNĐ")

        sl_traicay = st.number_input(
            "Số lượng trái cây",
            min_value=0,
            step=1,
            key="fruit"
        )

if st.button("Nộp"):

    tong = (
        sl_khoai * 35000
        + sl_salad * 30000
        + sl_pizza * 120000
        + sl_pho * 50000
        + sl_banh * 20000
        + sl_traicay * 15000
    )

    st.header("Hóa đơn")

    if sl_khoai > 0:
        st.write("Khoai tây chiên:", sl_khoai, "=", sl_khoai * 35000)

    if sl_salad > 0:
        st.write("Salad:", sl_salad, "=", sl_salad * 30000)

    if sl_pizza > 0:
        st.write("Pizza:", sl_pizza, "=", sl_pizza * 120000)

    if sl_pho > 0:
        st.write("Phở:", sl_pho, "=", sl_pho * 50000)

    if sl_banh > 0:
        st.write("Bánh ngọt:", sl_banh, "=", sl_banh * 20000)

    if sl_traicay > 0:
        st.write("Trái cây:", sl_traicay, "=", sl_traicay * 15000)

    st.subheader(f"Tổng tiền: {tong} VNĐ")