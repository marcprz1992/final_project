import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import src.sql_queries as secuel
from src.sql_queries import engine
import pandas as pd
import sqlalchemy as alch
from getpass import getpass
import re
import numpy as np
import requests
import seaborn as sns
import matplotlib.pyplot as plt
import stylecloud
import wordcloud as wc
from wordcloud import WordCloud, STOPWORDS
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as mp


st.set_page_config(
    page_title="General Overview")

#st.markdown("What's going on at Tesco?")
# st.sidebar.markdown("# Page 6")


st.title("What's going on at Tesco?")
cover = Image.open("../final_project/tesco_store.jpg")
st.image(cover, use_column_width=True)



st.header("1) Understanding Tesco categories")
st.dataframe(secuel.get_product_counts_by_category ())
q1 = secuel.get_product_counts_by_category ()
fig1 = px.bar(q1, x="Category", y="Number of products",title="Number of products by category",color="Category")
st.plotly_chart(fig1, use_container_width=True)

q43 = secuel.get_key_category_info()
fig43 = px.scatter(q43, x="Subcategory", y="Total Number of products",color="Category",
                 title="Number of products by subcategory",size="Total Number of products")
st.plotly_chart(fig43, use_container_width=True) 

st.write("You will also be able to filter the data by the categories or subcategories you are after in order to see the actual product list:")
option1 = st.selectbox(
    'Please choose a category:',
    ['food cupboard',
 'home and ents',
 'health and beauty',
 'fresh food',
 'drinks',
 'household',
 'frozen food',
 'baby',
 'petcare',
 'bakery'])

q3 = secuel.get_subcategory_counts_by_given_category(option1)
fig3 = px.bar(q3, x="Subcategory", y="Number of products",title=f"Number of products within each <b>{option1}</b> subcategory")
st.plotly_chart(fig3, use_container_width=True)

st.write("You can also filter by the subcategory you are most interested in")
option2 = st.selectbox("Please choose a subcategory:", (secuel.get_subcategory_counts_by_given_category (option1)))
st.dataframe(secuel.get_product_counts_by_given_subcategory (option2))
st.dataframe(secuel.get_products_by_given_subcategory (option2))


st.header("2) Price Analysis")

st.dataframe(secuel.get_avg_price_for_all_categories())
q13 = secuel.get_avg_price_for_all_categories ()
fig13 = px.bar(q13, x="Category", y="Average Price",title="Average selling price across all categories",color="Category")
st.plotly_chart(fig13, use_container_width=True)

st.write("For the following section, if you want to get access to the average price details from a specific category please do provide a category in the filter below.")
option1A = st.selectbox(
    'Please choose a category for price details:',
    ['food cupboard',
 'home and ents',
 'health and beauty',
 'fresh food',
 'drinks',
 'household',
 'frozen food',
 'baby',
 'petcare',
 'bakery'])


q14 = secuel.get_avg_price_for_all_subcategories(option1A)
fig14 = px.bar(q14, x="Subcategory", y="Average Price",title=f"Average Price across <b>{option1A}</b> subcategories",color="Subcategory")
st.plotly_chart(fig14, use_container_width=True)

option1B = st.selectbox("Please choose a subcategory to get the price details for the brands underneath:", (secuel.get_subcategory_counts_by_given_category (option1A)))

q14A = secuel.get_avg_price_for_all_brands(option1B)
fig14A = px.bar(q14A, x="Brand", y="Average Price",title=f"Average Price across Brands within <b>{option1B}</b>",color="Average Price")
st.plotly_chart(fig14A, use_container_width=True)



st.header("3) Manufacturers location")

st.write("If you are interested in seeing whereabouts the country the key manufacturers for each category are located in, you can use the filter below.")

st.write("To look at where the manufacturers for a given category are located, please do provide a category below.")
option16 = st.selectbox(
    'Please choose a category for location:',
    ['food cupboard',
 'home and ents',
 'health and beauty',
 'fresh food',
 'drinks',
 'household',
 'frozen food',
 'baby',
 'petcare',
 'bakery'])



q114 = secuel.get_postcodes_by_given_category(option16)
#st.dataframe(q114)
st.map(q114) 

