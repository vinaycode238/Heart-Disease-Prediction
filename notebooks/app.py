import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Heart Disease Prediction", page_icon=":bar_chart:", layout="wide")

st.title("Heart Disease Prediction App")
st.write("This app predicts the likelihood of heart disease based on user input.")

MODEL_FILE =  "model.pkl"

try :
    final_model = joblib.load(MODEL_FILE)
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file for prediction", type=["csv"])

if uploaded_file is not None:
   input_data = pd.read_csv(uploaded_file)
   st.subheader("Uploaded Data")
   st.dataframe(input_data, use_container_width=True)
   if st.button("Predict"):
       try:
           predictions = final_model.predict(input_data)
           probabilities = final_model.predict_proba(input_data)[:, 1]  # Probability of class 1
           output = input_data.copy()
           output['Predicted Disease'] = predictions
           output['Probability of Disease'] = probabilities.round(2)
           output['Predicted Disease'] = output['Predicted Disease'].map({0: 'No Disease', 1: 'Disease'})
           st.subheader("Prediction Results")
           st.dataframe(output, use_container_width=True)
           
           #CSV Download
           csv = output.to_csv(index=False).encode('utf-8')
           st.download_button(
           label="Download Predictions as CSV",
                          data=csv,
                          file_name="predictions.csv",
                          mime="text/csv")
       except Exception as e:  
           st.error(f"Error during prediction: {e}")
       
      
    
            
     