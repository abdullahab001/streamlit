import pickle

import pandas as pd
import streamlit as st

df = pd.read_csv('ola_driver_scaler.csv')

#st.write(df)

st.header('Driver Churn Prediction')

col1,col2,col3,col4 = st.columns(4)
col5,col6,col7 = st.columns(3)
col8,col9 = st.columns(2)
col10,col11 = st.columns(2)
with col1:
    gender = st.selectbox('Select Gender',('Male','Female'))
with col2:
    city = st.selectbox('Select City',('C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15','C16','C17','C18','C19','C20','C21','C22','C23','C24','C25','C26','C27','C28','C29'))
with col3:
    education = st.selectbox('Education Level',(0,1,2))
with col4:
    designation = st.selectbox('Joining Designation',(1,2,3,4,5))
with col5:
    grade = st.selectbox('Grade',(1,2,3,4,5))
with col6:
    rating = st.selectbox('Quarterly Rating',(1,2,3,4,5))
with col7:
    age = st.number_input('Age',value=0)
with col8:
    income = st.slider('Select an Income Range', 5000, 200000, step=500)
with col9:
    businessvalue = st.slider('Select a Range of Business Value',-2000000.0,100000000.0,step=100.0)
with col10:
    inc_inc = st.selectbox('Is Income Increased?',('Yes','No'))
with col11:
    rt_inc = st.selectbox('Is Rating Increased?',('Yes','No'))
city_list = []
for i in ['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15','C16','C17','C18','C19','C20','C21','C22','C23','C24','C25','C26','C27','C28','C29']:
    if city == i:
        city_list.append(1)
    else:
        city_list.append(0)

encode_dict = {
    'gender':{'Male':1,'Female':0},
    'inc_inc':{'Yes':1,'No':0},
    'rt_inc':{'Yes':1,'No':0},
}
def model_pred(age,gender,education,income,designation,grade,businessvalue,rating,rt_inc,inc_inc,city_list):
    input = \
    [[age, gender, education, income, designation,
     grade, businessvalue, rating, rt_inc,
     inc_inc, city_list[0], city_list[9], city_list[10], city_list[11],
     city_list[12], city_list[13], city_list[14], city_list[15], city_list[16], city_list[17],
     city_list[18], city_list[1], city_list[19], city_list[20], city_list[21], city_list[22],
     city_list[23], city_list[24], city_list[25], city_list[26], city_list[27], city_list[28],
     city_list[2], city_list[3], city_list[4], city_list[5], city_list[6], city_list[7],
     city_list[8]]]

    with open('driver_churn.sav','rb') as file:
        classification = pickle.load(file)
        return classification.predict(input)

if st.button('Predict'):
    g = encode_dict['gender'][gender]
    inc = encode_dict['inc_inc'][inc_inc]
    rt = encode_dict['rt_inc'][rt_inc]
    pred = model_pred(age,g,education,income,designation,grade,businessvalue,rating,rt,inc,city_list)

    if pred[0] == 1:
        st.write(f':sob: Beware :sob:!!! He is going to Churn')
    else:
        st.write('He is a valued Driver :sunglasses: , and his performance is good')