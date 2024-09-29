import streamlit as st 
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyDdcJ3yu1knD-5UivWfQeOUzp3jgW40y38")

model=genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input_text,image_data,prompt):
    response=model.generate_content([input_text,image_data[0],prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("NO FILE WAS UPLOADED")
    
st.set_page_config(page_title="INVOICE GENERATOR-ADHITYA")
st.sidebar.header("ROBOBILL")
st.sidebar.write("MADE")
st.sidebar.write("POWERED BY GEMINI AI")
st.header("ROBOBILL")
st.subheader("MADE BY ADHITYA V")
st.subheader("MANAGE YOUR EXPENSES USING THIS ROBOBILL")
input=st.text_input("What do you want me to do?",key="input")
uploaded_file=st.file_uploader("Choose image from gallery",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)

submit=st.button("LETSSSSSS GOOOOOOOO!!!!!!")

input_prompt = """
You are an expert in calculus. I will upload an image of a calculus question which you are to analyse. You will tell me the steps to solve the question and give me the answer
"""
if submit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("Here's what you need to know!")
    st.write(response)
