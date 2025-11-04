import streamlit as st

st.title("Student Info Form")

name = st.text_input("Enter your First Name:")
surname = st.text_input("Enter your Surname:")
marks_10 = st.number_input("Enter your 10th Marks (%):", 0, 100)
marks_12 = st.number_input("Enter your 12th Marks (%):", 0, 100)

if st.button("Submit"):
    st.success(f"Hello {name} {surname}! 🎓")
    st.write(f"10th Marks: {marks_10}%")
    st.write(f"12th Marks: {marks_12}%")
