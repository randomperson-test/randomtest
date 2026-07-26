import streamlit as st
import pandas as pd

# Load CSV
FILE = "data1.csv"
df = pd.read_csv(FILE)

# Enter name
name = st.text_input("điền tên của bạn")

if name:
    # Find the row
    if name in df["Ho ten"].values:

        # Get row index
        row_index = df[df["Ho ten"] == name].index[0]

        st.write("chỉnh sửa điểm của bạn")

        # Dictionary to store edited values
        new_values = {}

        # Loop through columns except name
        for column in df.columns:
            if column == "Ho ten":
                continue

            # Only allow integer columns
            if pd.api.types.is_integer_dtype(df[column]):
                current = int(df.loc[row_index, column])

                new_values[column] = st.number_input(
                    column,
                    min_value=1,
                    max_value=10,
                    value=current,
                    step=1,
                )

        # Save button
        if st.button("lưu"):
            for column, value in new_values.items():
                df.loc[row_index, column] = value

            df.to_csv(FILE, index=False)
            st.success("điểm đã được thay đổi")

    else:
        st.error("không tìm thấy tên")