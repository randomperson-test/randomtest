import streamlit as st
import pandas as pd

data = pd.read_csv("data1.csv")
st.dataframe(data)

ten = st.text_input("Điền tên của bạn")

if st.button("Đặt tất cả điểm thành 10"):
    if ten in data["Ho ten"].values:
        data.loc[data["Ho ten"] == ten, data.columns[1:]] = 10

        data.to_csv("data1.csv", index=False)

        st.success("Đã cập nhật")
        st.dataframe(pd.read_csv("data1.csv"))
    else:
        st.error("Không tìm thấy tên.")
