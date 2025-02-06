import streamlit as st
from lib import get_results
# ///////////model input/////////////////
# input=[6,148,72,35,0,33.,0.627,50]
# y=model.predict([input])
# st.title('Uber pickups in NYC')
Pregnancies=st.text_input("Enter how many time you got Pregnant")
Glucose=st.text_input("Enter  Glucose")
BloodPressure=st.text_input("Enter BloodPressure")
SkinThickness=st.text_input("Enter SkinThickness")
Insulin=st.text_input("Enter Insulin")
BMIx=st.text_input("Enter BMI")
DiabetesPedigreeFunction=st.text_input("Enter DiabetesPedigreeFunction")
Age=st.text_input("Enter your age")

show=st.button("click")
if show:
    result=get_results(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMIx,DiabetesPedigreeFunction,Age)
    if result:
        st.title('sorry ,,, you are daiabitic')
    else:
        st.title("good news ,you are not daiabitic")
