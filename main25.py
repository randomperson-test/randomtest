import pandas as pd
import streamlit as st

data = pd.read_csv("data5.8.csv")

st.write("Dữ liệu:")
st.dataframe(data)

so_gio_hoc = data["Số Giờ Học"]
diem = data["Điểm Số"]

st.write("Số giờ học")
st.write("Min:", so_gio_hoc.min())
st.write("Max:", so_gio_hoc.max())
st.write("Mean:", so_gio_hoc.mean())
st.write("Median:", so_gio_hoc.median())
st.write("Mode:", so_gio_hoc.mode())

st.write("Điểm số")
st.write("Min:", diem.min())
st.write("Max:", diem.max())
st.write("Mean:", diem.mean())
st.write("Median:", diem.median())
st.write("Mode:", diem.mode())