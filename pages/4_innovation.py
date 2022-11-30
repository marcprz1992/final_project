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
    page_title="Innovation")

#st.markdown("# Page 2")
#st.sidebar.markdown("# Page 2")

st.title("Innovation at Tesco")
cover = Image.open("../final_project/tesco_innovation.jpg")
st.image(cover, use_column_width=True)


st.header("1) Innovation overview")
q48 = secuel.get_innovation_vs_not_across_categories2()
q49 = secuel.giveme_percentages_innovation(q48)
st.dataframe(q49)


layout = go.Layout(
   {
      "title":"Distribution of innovation by category"})
fig49a = go.Figure(data=[go.Pie(labels=q49["Category"], values=q49["New products"], hole=.3)],layout=layout)
st.plotly_chart(fig49a, use_container_width=True)


st.header("2) Looking for specific innovation")
st.write("For the following section, if you want to get access to the innovation details from a specific category please do provide a category in the filter below.")
option4A = st.selectbox(
    'Please choose a category for promo details:',
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

q48A = secuel.get_innov_vs_not_across_subcategories(option4A)
#fig28A = px.bar(q28A, x="Subcategory", y="Number of products WITH promotion",title="Promotional Activity across subcategories",color="Subcategory")
#st.plotly_chart(fig28A, use_container_width=True)

fig48B = px.bar(
    data_frame = q48A,
    x = "Subcategory",
    y = ["Rest of range","New products"],
    opacity = 0.9,
    orientation = "v",
    barmode = 'stack',
    title='Distribution of innovation vs. rest of range by subcategory')
st.plotly_chart(fig48B, use_container_width=True)

st.write("You can also filter by the subcategory you are most interested in to see what new & exciting innovation is happening there.")
option4B = st.selectbox("Please choose a subcategory:", (secuel.get_subcategory_counts_by_given_category (option4A)))
st.dataframe(secuel.get_innov_count_across_subcategories(option4B))
st.dataframe(secuel.get_innov2_across_subcategories(option4B))



q49C = st.dataframe(secuel.get_innov2_vs_not_across_for_a_given_brand(option4B))
#fig29A = px.bar(
  #  data_frame = q29,
   # x = "Brand",
   # y = ["Number of products WITHOUT promotion","Number of products WITH promotion"],
    #opacity = 0.9,
    #orientation = "v",
    #barmode = 'stack',
    #title='Number of products in promo vs. not by brand')
#st.plotly_chart(fig29A, use_container_width=True)

#st.dataframe(secuel.get_products_by_given_subcategory (option2))

q40C = secuel.get_innov2_vs_not_across_for_a_given_brand(option4B)
fig40C = px.bar(q40C, x="Brand", y="New products",title="Number of NEW products by Brand",color="New products")
st.plotly_chart(fig40C, use_container_width=True)