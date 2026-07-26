import streamlit as st
import pandas as pd

FILE = "data1.csv"

# Load CSV
df = pd.read_csv(FILE)
df.columns = df.columns.str.strip()

# Show current CSV
st.subheader("Dữ liệu hiện tại")
st.dataframe(df, use_container_width=True)

st.divider()

# Enter name
name = st.text_input("Điền tên của bạn")

if name:
    # Check if the name exists
    if name in df["Ho ten"].values:

        row_index = df[df["Ho ten"] == name].index[0]
        if st.button("Đặt tất cả điểm thành 10"):

            # Set every integer column to 10
            for column in df.columns:
                if column != "Ho ten" and pd.api.types.is_integer_dtype(df[column]):
                    df.loc[row_index, column] = 10

            # Save changes
            df.to_csv(FILE, index=False)

            st.success("Đã cập nhật điểm")

            # Reload and display updated table
            df = pd.read_csv(FILE)
            st.subheader("Dữ liệu sau khi cập nhật")
            st.dataframe(df, use_container_width=True)

    else:
        st.error("Không tìm thấy tên.")
