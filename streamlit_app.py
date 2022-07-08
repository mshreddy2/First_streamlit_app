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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Display the table on the page.
# streamlit.dataframe(my_fruit_list)

# display the table on the page
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
