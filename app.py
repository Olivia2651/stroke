import streamlit as st 
import numpy
import string
import pickle
st.set_option('deprecation.showfileUploaderEncoding',False)
model = pickle.load(open('model_pk.pkl','rb'))


def main():
  st.sidebar.header("Stroke Risk Prediction")
  st.sidebar.header("This is a web app that tells you the predicted wether you will have a stroke or not")
  st.sidebar.header("Just fill in the information below")
  st.sidebar.header("Stroke Risk Prediction")



  age = st.slider("Input your age:",0,100)
  hypertension = st.slider("Input if you have hypertension, 0 if no and 1 if yes",0,1)
  heartdisease = st.slider("Input if you have heart disease, 0 if no and 1 if yes",0,1)
  sugar=st.slider("Input your average glucose level",150.0,300.000)
  bmi=st.slider("Input your BMI",0.0,70.0)

  inputs=[{age,hypertension,heartdisease,sugar,bmi}]

  if st.button('Predict'):
    result = model.predict(inputs)
    updated_res = result.flatten().astype(int)
    if  updated_res ==0:
      st.write("Not very probable you will have a stroke soon")
    else:
      st.write("It is probable you might have a stroke soon therefore you should see your doctor")


if __name__=='__main__':
  main() 






  
  
