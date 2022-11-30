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
    page_title="Stock tracker")

#st.markdown("# Page 4")
#st.sidebar.markdown("# Page 4")

st.title("Stock challenges")
cover = Image.open("../final_project/tesco_stock.jpg")
st.image(cover, use_column_width=True)


st.header("1) Tracking the stock across the different categories")
q33 = secuel.get_products_stock_issues_by_category()
q33B = secuel.giveme_percentages_stock(q33)
st.dataframe(q33B)

layout = go.Layout(
   {
      "title":"Distribution of stock issues by category"})
fig33B = go.Figure(data=[go.Pie(labels=q33B["Category"], values=q33B["Number of products WITHOUT stock"], hole=.3)],layout=layout)
st.plotly_chart(fig33B, use_container_width=True)

st.header("2) Looking for specific stock challenges")
st.write("For the following section, if you want to see what exact products are out of stock, please do provide a category in the filter below.")
option3A = st.selectbox(
    'Please choose a category for stock tracking:',
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


q38A = secuel.get_stock_vs_not_across_subcategories(option3A)
fig38A = px.bar(
    data_frame = q38A,
    x = "Subcategory",
    y = ["Number of products WITH stock","Number of products WITHOUT stock"],
    opacity = 0.9,
    orientation = "v",
    barmode = 'stack',
    title='Number of products in stock vs. not by subcategory')
st.plotly_chart(fig38A, use_container_width=True)

st.write("You can also filter by the subcategory you are most interested in to see what products are currently out of stock")
option3B = st.selectbox("Please choose a subcategory:", (secuel.get_subcategory_counts_by_given_category (option3A)))
st.dataframe(secuel.get_stock_count_across_subcategories(option3B))
st.dataframe(secuel.get_stock2_across_subcategories(option3B))


q293 = st.dataframe(secuel.get_stock_vs_not_across_for_a_given_brand(option3B))
q303 = secuel.get_stock_vs_not_across_for_a_given_brand(option3B)
fig303 = px.bar(q303, x="Brand", y="Number of products WITHOUT stock",title="Number of products WITHOUT stock by Brand",color="Number of products WITHOUT stock")
st.plotly_chart(fig303, use_container_width=True)