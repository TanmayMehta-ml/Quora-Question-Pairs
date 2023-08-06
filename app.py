import streamlit as st
import helper
# import pickle
# import requests

# model = pickle.load(open('model.pkl','rb'))
import requests
import pickle

model_url = 'https://github.com/TanmayMehta-ml/Quora-Question-Pairs/releases/download/model-weight-1.0/model.pkl'
response = requests.get(model_url)

if response.status_code == 200:
    with open('model.pkl', 'wb') as f:
        f.write(response.content)

    model = pickle.load(open('model.pkl', 'rb'))
else:
    # Handle the case if the model file could not be fetched
    raise Exception("Failed to fetch the model file from the release.")

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')