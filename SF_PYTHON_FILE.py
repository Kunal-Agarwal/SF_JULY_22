import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Butter Dosa ð¶ï¸ð¶ï¸ð§ð§')
streamlit.text('Tawa Fry Vada ð¶ï¸ð§ð§')
streamlit.text('Ghee Fried Idli ð¶ï¸ð§ð§')
streamlit.text('Jalebi with Rabdi')
streamlit.text('Butter Milkð¥¤')

streamlit.header('ðð¥­ Build Your Own Fruit Smoothie ð¥ð')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries', 'Banana'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)



