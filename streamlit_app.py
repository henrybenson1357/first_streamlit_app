import streamlit
import pandas as pd
import requests
import snowflake.connector


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()
def insert_row_snowflake(new_fruit):
  with mycnx.cursor() as my_cur:
      my_cur.execute("insert into fruit_load_list values ('"+str(new_fruit)+"')")
      return "Thanks for adding "+new_fruit
if streamlit.button('Get Fruit Load List'):
  my_data_rows=get_fruit_load_list()
  streamlit.dataframe(my_data_rows)

fruit_to_add=streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add Fruit to the List'):
  add_fruit_to_list=insert_row_snowflake(fruit_to_add)
  streamlist.text(add_fruit_to_list)


fruit_df= pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruit_df = fruit_df.set_index('Fruit')
fruit_select = streamlit.multiselect("Pick some fruits:", list(fruit_df.index),['Avocado','Strawberries'])
display_fruit_df = fruit_df.loc[fruit_select]
streamlit.dataframe(display_fruit_df)
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.header('Fruity Fruit Advice')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
