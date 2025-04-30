import streamlit as st
import joblib

model = joblib.load("model.pkl")

st.title("predction salary")

years_exceprance = st.number_input("numbers of years" ,min_value=1.0, step=0.01)

btn = st.button("pred")
if btn == True :
    salary = model.predict([[years_exceprance]])
    st.success(salary)