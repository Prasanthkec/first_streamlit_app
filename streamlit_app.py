import snowflake.connector
import streamlit
import pandas
import requests
from urllib.error import URLError

streamlit.header("The fruitload list contains")
def get_fruit_list():
            with my_cnx.cursor() as my_cur:
                        my_cur.execute("select * from fruit_load_list")
                        return my_cur.fetchall()
if streamlit.button('Get fruit load list'):
            my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
            my_data_rows = get_fruit_list()
            streamlit.dataframe(my_data_rows)

streamlit.title('My parents first Healthy Diner')
streamlit.header('🥣 Breakfast Menu')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🐔 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice fruit advice')
def get_fruityvice_data(this_fruit_choice):
            fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
            fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
            return fruityvice_normalized
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
            streamlit.error("Please select a fruit to get information about?")
  else:
            
            streamlit.dataframe(get_fruityvice_data(fruit_choice))
except URLError as e:
     streamlit.error()

streamlit.write('The user entered ', fruit_choice)
#streamlit.stop()

def insert_row_snowflake(new_fruit):
            with my_cnx.cursor() as my_cur:
                        my_cur.execute("insert into fruit_load_list values('"+????+"')")
                        return "Thanks for adding " + new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like to add')
if streamlit.button('Add a Fruit to The List') :
                                    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
                                    streamlit.text(insert_row_snowflake(add_my_fruit))



