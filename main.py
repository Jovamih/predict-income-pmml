from pypmml import Model
import streamlit as st

st.title("Predict Income")
st.write("Predecir el ingreso de una persona segun sus caracteristicas")
st.write("By @johanValerioMitma")
st.image("income-logo.png", use_column_width=True)
model=Model.load("xgboost-model.pmml")
data={}
data['age']=st.selectbox("Edad",("<=17","18-27","28-59","60+"))
data['worclass']=st.selectbox("Clase de trabajo",("Federal-gov","Local-gov","State-gov","Self-emp-inc","Self-emp-not-inc","Without-pay","Never-worked"))
data['fnlwgt']=float(st.text_input("Peso final",50))
data['education']=st.selectbox("Educación",("Bachelors","Some-college","11th","HS-grad","Prof-school","Assoc-acdm","Assoc-voc","9th","7th-8th","12th","Masters","1st-4th","10th","Doctorate","5th-6th","Preschool"))
data['education-num']=float(st.text_input("Número de estudios",9))
data['marital-status']=st.selectbox("Estado civil",("Divorced","Married-civ-spouse","Married-AF-spouse","Never-married","Separated","Widowed","Married-spouse-absent","Married-AF-nohusb"))
data['occupation']=st.selectbox("Ocupación",("Tech-support","Craft-repair","Other-service","Sales","Exec-managerial","Prof-specialty","Handlers-cleaners","Machine-op-inspct","Adm-clerical","Farming-fishing","Transport-moving","Priv-house-serv","Protective-serv","Armed-Forces"))
data['relationship']=st.selectbox("Relación",("Wife","Own-child","Husband","Not-in-family","Other-relative","Unmarried"))
data['race']=st.selectbox("Raza",("American-Indian-Eskimo","Asian-Pac-Islander","Black","Other","White"))
data['sex']=st.selectbox("Sexo",("Male","Female"))
data['capital-gain']=float(st.text_input("Capital ganado",3400))
data['capital-loss']=float(st.text_input("Capital perdido",0))
data['hours-per-week']=float(st.text_input("Horas por semana",45))

#print(model)
#model.inputNames=["age","worclass","fnlwgt","education-num","marital-status","occupation","relationship","race","sex","capital-gain","capital-loss","hours-per-week"]
if st.button("Predecir Ingreso"):
    response=model.predict(data)
    if response['P (<=50K)']>response['P (>50K)']:
        st.success("Ingreso inferior a 50K")
        st.write(f"Probabilidad: {round(response['P (<=50K)']*100,2)}%")
    else:
        st.success("Ingreso superior a 50K")
        st.write(f"Probabilidad: {round(response['P (>50K)']*100,2)}%")
    
else:
    st.warning("Ningun dato predecido")

