import streamlit as st
import joblib
string = "Machine Learning"
st.set_page_config(page_title=string, page_icon="😆")
st.title("Machine Learning")
st.write("""
# Salary Prediction Model
Salary vs. *Experience*
""")
mymodel = joblib.load("salary.pkl")
exp = st.sidebar.slider('Experience',1.0,50.0,2.0)
salary = round(mymodel.predict([[exp]])[0],2)
st.write(f"Experience: ", exp)
st.write(f"Salary: ", float(salary))