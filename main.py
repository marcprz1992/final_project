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
    page_title="Welcome to my final project!",
    page_icon="👋")

cover = Image.open("../final_project/tesco_logo.png")
st.image(cover, use_column_width=True)

#st.markdown("# Main page")
st.sidebar.markdown("# Main page")



st.title('Deeep dive from Tesco')
st.header("General information")

#query = f"""SELECT Category, COUNT(product_id) as 'Number of products' 
    #FROM final_project_ironhack.main_product_info
    #GROUP BY Category
    #ORDER BY COUNT(product_id) DESC;"""
#df = pd.read_sql_query(query, engine)

st.dataframe(secuel.get_product_counts_by_category ())

option1 = st.selectbox(
    'Please choose a category:',
    ('Fresh', 'Household', 'Petcare'))

st.dataframe(secuel.get_subcategory_counts_by_given_category (option1))



st.header("First chart:")

q1 = secuel.get_product_counts_by_category ()
fig1 = px.bar(q1, x="Category", y="Number of products",title="Number of products by category",color="Category")
st.plotly_chart(fig1, use_container_width=True)

q43 = secuel.get_key_category_info()
fig43 = px.scatter(q43, x="Subcategory", y="Total Number of products",color="Category",
                 title="Number of products by subcategory",size="Total Number of products")
st.plotly_chart(fig43, use_container_width=True) 