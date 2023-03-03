import streamlit as st 
import numpy
import string
import pickle
st.set_option('deprecation.showfileUploaderEncoding',False)
model = pickle.load(open('LR2_pk.pkl','rb'))


def main():
  st.title("Stroke Risk Prediction")
  
  st.sidebar.header("This is a web app that tells you the predicted wether you will have a stroke or not")
  
  st.subheader("Just fill in the information")
  age = st.slider("Input your age:",0,100)
  hypertension = st.slider("Input if you have hypertension.\n 0 if no and 1 if yes",0,1)
  heartdisease = st.slider("Input if you have heart disease.\n 0 if no and 1 if yes",0,1)
  ever_married=st.slider('Input your marriage status.\n0 if no and 1 if yes',0,1)
  work_type= st.selectbox('Input the type of work you do.\n2 if Private,3 if Self-employed,0 if Govt_job,4 if children,1 if Never_worked',(2,3,0,4,1))
  sugar=st.number_input("Input your average glucose level", min_value=None, max_value=None)
  bmi=st.number_input("Input your BMI", min_value=None, max_value=None)
  smoking_status=st.selectbox('Input your smoking status.\n 1 is formerly smoked,2 is never smoked,3 is smokes,0 is Unknown' ,(1,2,3,0))
  

  inputs=[[age,hypertension,heartdisease,ever_married,work_type,sugar,bmi,smoking_status]]
  if st.button('Predict'):
    result = model.predict(inputs)
    updated_res = result.flatten().astype(int)
    if  updated_res ==0:
      st.write("Not very probable you will have a stroke soon")
    else:
      st.write("It is probable you might have a stroke soon therefore you should see your doctor")


if __name__=='__main__':
  main() 






  
  
