import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Butter Dosa 🌶️🌶️🧄🧅')
streamlit.text('Tawa Fry Vada 🌶️🧄🧅')
streamlit.text('Ghee Fried Idli 🌶️🧄🧅')
streamlit.text('Jalebi with Rabdi')
streamlit.text('Butter Milk🥤')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))



