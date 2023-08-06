import streamlit as st
import helper
import requests
import pickle

# Fetch the pre-trained model
model_url = 'https://github.com/TanmayMehta-ml/Quora-Question-Pairs/releases/download/model-weight-1.0/model.pkl'
response = requests.get(model_url)

if response.status_code == 200:
    with open('model.pkl', 'wb') as f:
        f.write(response.content)

    model = pickle.load(open('model.pkl', 'rb'))
else:
    # Handle the case if the model file could not be fetched
    raise Exception("Failed to fetch the model file from the release.")

# Page title and header
st.title('Quora Question Pairs')
st.header('Find out if two questions are duplicates or not!')

# User input for question pairs
q1 = st.text_input('Enter your first question here:')
q2 = st.text_input('Enter your second question here:')

# Predict button
if st.button('Find'):
    # Create query point for model prediction
    query = helper.query_point_creator(q1, q2)
    result = model.predict(query)[0]

    # Display prediction result
    if result:
        st.success('✅ These questions look similar! They might be duplicates.')
    else:
        st.info('🚫 These questions seem to be different.')

# Add a fun emoji and footer
st.write('Made with ⌨️ & 🖱️ by Tanmay Mehta')
st.write('Connect with me on [LinkedIn](https://www.linkedin.com/in/tanmay-here/)')
