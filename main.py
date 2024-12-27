import streamlit as st
import requests

st.set_page_config(layout="wide")

url = ("https://api.nasa.gov/planetary/apod?"
       "api_key=Ff7VzeU663aPkwbJISZZKfMxMUzSnpMDMzxe7i2v")
api_key = "Ff7VzeU663aPkwbJISZZKfMxMUzSnpMDMzxe7i2v"
# get data from API
response = requests.get(url)
data = response.json()
# Extract data in needed variables
title = data["title"]
explanation = data["explanation"]
img_path = data["hdurl"]
# get image
response2 = requests.get(img_path)
image = response2.content
with open("image.jpg","wb") as file:
    file.write(response2.content)
# create website content
st.title("❤️ TAGHDIM BE ZIBATARIN SETAREYE ZENDEGIM ❤️")
st.title(title)
st.image("image.jpg")
st.write(explanation)