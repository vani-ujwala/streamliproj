import streamlit as st

def cal(a, b):
    return a + b
number_first = st.number_input("Enter the first number")
number_second = st.number_input("Enter the second number")
if st.button("add"):
    result = cal(number_first, number_second)
    st.write(f"The result is: {result}")
def diff(a, b):
    return a - b
if st.button("sub"):
    result = diff(number_first, number_second)
    st.write(f"The result is: {result}")
