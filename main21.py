import streamlit as st
import pandas as pd
import numpy as np
file= "data2.csv"
df = pd.read_csv(file)

st.dataframe(df)

if st.button("Random"):

    randomized_df = df.copy()

    numeric_cols = randomized_df.select_dtypes(
        include=["number"]
    ).columns

    for col in numeric_cols:
        randomized_df[col] = np.random.randint(
            1, 11,
            size=len(randomized_df)
        )

    randomized_df.to_csv(file, index=False)
