import pandas as pd
import streamlit as st

st.title("Dọn dẹp dữ liệu")

# Upload file
uploaded_file = st.file_uploader("tải lên file CSV", type=["csv"])

if uploaded_file is not None:

    # Đọc file
    data = pd.read_csv(uploaded_file)

    st.subheader("Dữ liệu ban đầu")
    st.dataframe(data)

    # Thống kê
    total_rows = len(data)
    duplicate_rows = data.duplicated().sum()
    null_rows = data.isnull().any(axis=1).sum()

    st.write(f"**Tổng số hàng:** {total_rows}")
    st.write(f"**Số hàng trùng:** {duplicate_rows}")
    st.write(f"**Số hàng Null/NaN:** {null_rows}")

    # Nút dọn dẹp
    if st.button("Dọn dẹp file"):

        cleaned_data = data.drop_duplicates()
        cleaned_data = cleaned_data.dropna()

        cleaned_rows = len(cleaned_data)

        st.subheader("Kết quả sau khi dọn dẹp")

        st.write(f"**Số hàng ban đầu:** {total_rows}")
        st.write(f"**Số hàng sau khi dọn:** {cleaned_rows}")

        st.dataframe(cleaned_data)
