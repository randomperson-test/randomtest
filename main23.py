import streamlit as st
import pandas as pd

df = pd.read_csv("data1.csv")
df.columns = df.columns.str.strip()

st.dataframe(df, use_container_width=True)

st.divider()

name = st.text_input("Điền tên của bạn")

if name:
    if name in df["Ho ten"].values:

        row_index = df[df["Ho ten"] == name].index[0]
        new_values = {}
        for column in df.columns:
            if column == "Ho ten":
                continue

            if pd.api.types.is_integer_dtype(df[column]):
                new_values[column] = st.number_input(
                    column,
                    min_value=0,
                    max_value=10,
                    value=int(df.loc[row_index, column]),
                    step=0.25,
                )

        if st.button("Lưu"):
            for column, value in new_values.items():
                df.loc[row_index, column] = value

            df.to_csv("data1.csv", index=False)
            st.success("Đã lưu thay đổi")

            # Reload and display updated table
            df = pd.read_csv("data1.csv")
            st.dataframe(df, use_container_width=True)

    else:
        st.error("Không tìm thấy tên")
