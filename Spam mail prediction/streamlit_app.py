import streamlit as st
import joblib

# load the model 
model = joblib.load(r"D:\ML project\Spam mail prediction\spam_model (1).pkl")

# streamlit APP UI
st.title("📩 Spam Mail Detection System")
st.markdown("enter your email content below and check if it's spam.")

# input box
user_input = st.text_area("Email content", height=200)


# predict 
if st.button("predict"):
    if user_input.strip() == "":
        st.warning("please enter some eamil text.")
        
    else:
        prediction = model.predict([user_input])[0]
        result = "🚫 Spam" if prediction == 1 else "✅ Not Spam"
        st.success(f"prediction: {result}")
        

# when you run 

# cd "D:\ML project\Spam mail prediction"


# then use -- streamlit run streamlit_app.py