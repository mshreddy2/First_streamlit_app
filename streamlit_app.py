import streamlit

streamlit.title('My Parents New HealthyDiner')

streamlit.header('Breakfast Favorites')
streamlit.text('\N{bowl with spoon}Omega 3 & Blueberry Oatmeal ')
streamlit.text('\N{leafy green}Kale, Spinach & Rocket Smoothie')
streamlit.text('\N{egg}Hard-Boiled Free-Range Egg')
streamlit.text('\N{avocado} \N{bread} Avocado Toast')

streamlit.header('\N{banana} \N{strawberry} Build Your Own Fruit Smoothie \N{kiwifruit} \N{grapes} ')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
