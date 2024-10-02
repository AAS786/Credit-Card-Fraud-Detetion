import streamlit as st
import pickle as pk
import warnings
import numpy as np

warnings.filterwarnings("ignore")

# Loading the saved model
model = pk.load(open('Credit_card.sav', 'rb'))

# Custom CSS with Background Image and Enhanced Input Box Design
st.markdown(f"""
    <style>
    body {{
        font-family: Arial, sans-serif;
        background-color: #f0f0f0; /* Light background for body */
    }}
    .main {{
        background: url("https://i.postimg.cc/rsnz7w31/Nature-Background.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        padding: 20px; /* Add padding for better layout */
        border-radius: 10px; /* Rounded corners */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Shadow effect */
    }}
    h1 {{
        color: yellow;
        text-align: center;
        text-decoration: underline;
        margin-bottom: 30px;
    }}
    h3 {{
        text-align: center;
    }}
    .stTextInput > div {{
        display: flex;
        justify-content: center;
        margin-bottom: 10px;
    }}
    .stTextInput input {{
        padding: 10px;
        font-size: 16px;
        border: 2px solid #ccc;
        border-radius: 5px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        transition: border-color 0.3s, box-shadow 0.3s;
    }}
    .stTextInput input:focus {{
        border-color: #4CAF50;
        box-shadow: 0px 4px 6px rgba(76, 175, 80, 0.5);
    }}
    .stButton {{
        display: flex;
        justify-content: center; 
        margin-top: 20px;
    }}
    .stButton button {{
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        font-size: 16px;
        border-radius: 5px;
        transition-duration: 0.4s;
    }}
    .stButton button:hover {{
        background-color: white; 
        color: #4CAF50;
        border: 2px solid #4CAF50;
    }}
    </style>
    """, unsafe_allow_html=True)

# Credit Card Fraud Detection Page
st.markdown("<h1>Credit Card Fraud Detection using <br>Machine Learning</h1>", unsafe_allow_html=True)

# Layout for input boxes
col1, col2, col3, col4 = st.columns(4)
with col1:
    V1 = st.text_input('**V1 Score**', placeholder='Enter V1 Score')
    V5 = st.text_input('**V5 Score**', placeholder='Enter V5 Score')
    V9 = st.text_input('**V9 Score**', placeholder='Enter V9 Score')
    V13 = st.text_input('**V13 Score**', placeholder='Enter V13 Score')
    V17 = st.text_input('**V17 Score**', placeholder='Enter V17 Score')
    V21 = st.text_input('**V21 Score**', placeholder='Enter V21 Score')
    V25 = st.text_input('**V25 Score**', placeholder='Enter V25 Score')
with col2:
    V2 = st.text_input('**V2 Score**', placeholder='Enter V2 Score')
    V6 = st.text_input('**V6 Score**', placeholder='Enter V6 Score')
    V10 = st.text_input('**V10 Score**', placeholder='Enter V10 Score')
    V14 = st.text_input('**V14 Score**', placeholder='Enter V14 Score')
    V18 = st.text_input('**V18 Score**', placeholder='Enter V18 Score')
    V22 = st.text_input('**V22 Score**', placeholder='Enter V22 Score')
    V26 = st.text_input('**V26 Score**', placeholder='Enter V26 Score')
    Amount = st.text_input('**Amount**', placeholder='Enter Amount')

with col3:
    V3 = st.text_input('**V3 Score**', placeholder='Enter V3 Score')
    V7 = st.text_input('**V7 Score**', placeholder='Enter V7 Score')
    V11 = st.text_input('**V11 Score**', placeholder='Enter V11 Score')
    V15 = st.text_input('**V15 Score**', placeholder='Enter V15 Score')
    V19 = st.text_input('**V19 Score**', placeholder='Enter V19 Score')
    V23 = st.text_input('**V23 Score**', placeholder='Enter V23 Score')
    V27 = st.text_input('**V27 Score**', placeholder='Enter V27 Score')
with col4:
    V4 = st.text_input('**V4 Score**', placeholder='Enter V4 Score')
    V8 = st.text_input('**V8 Score**', placeholder='Enter V8 Score')
    V12 = st.text_input('**V12 Score**', placeholder='Enter V12 Score')
    V16 = st.text_input('**V16 Score**', placeholder='Enter V16 Score')
    V20 = st.text_input('**V20 Score**', placeholder='Enter V20 Score')
    V24 = st.text_input('**V24 Score**', placeholder='Enter V24 Score')
    V28 = st.text_input('**V28 Score**', placeholder='Enter V28 Score')

# Prediction Button
if st.button('**Credit Card Fraud Detection Result**'):
    try:
        # Collecting input data into a list
        input_data = [
            float(V1),
            float(V2),
            float(V3),
            float(V4),
            float(V5),
            float(V6),
            float(V7),
            float(V8),
            float(V9),
            float(V10),
            float(V11),
            float(V12),
            float(V13),
            float(V14),
            float(V15),
            float(V16),
            float(V17),
            float(V18),
            float(V19),
            float(V20),
            float(V21),
            float(V22),
            float(V23),
            float(V24),
            float(V25),
            float(V26),
            float(V27),
            float(V28),
            float(Amount)
        ]

        # Reshaping input data for model prediction
        reshaped_input = np.array(input_data).reshape(1, -1)
        gen_prediction = model.predict(reshaped_input)

        # Prediction result
        if gen_prediction[0] == 0:
            Predict_diagnosis = 'The Credit Card Customer is not Fraud'
            result_color = "green"
        else:
            Predict_diagnosis = 'The Credit Card Customer is Fraud'
            result_color = "red"

        # Display prediction result
        st.markdown(f"<h3 style='color: {result_color};'>{Predict_diagnosis}</h3>", unsafe_allow_html=True)
        
        # Trigger balloon animation
        st.balloons()
        
    except ValueError as e:
        st.markdown(f"<h3 style='color: red;'>Invalid input: {e}</h3>", unsafe_allow_html=True)
