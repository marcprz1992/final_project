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
    page_title="Promotional Activity")

#st.markdown("# Page 2")
#st.sidebar.markdown("# Page 2")

st.title("Promotional activation at Tesco")
cover = Image.open("../final_project/tesco_clubcard.jpg")
st.image(cover, use_column_width=True)


st.header("1) Promotions overview")
q28 = secuel.get_promotion_vs_not_across_categories()
q29 = secuel.giveme_percentages(q28)
st.dataframe(q29)

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
#labels = q29["Category"]
#sizes = q29["% promo vs. total"]
#explode = (0, 0, 0, 0, 0.1, 0, 0, 0, 0, 0) 

#fig29, ax29 = plt.subplots()
#ax29.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
 #      shadow=True, startangle=90)
#ax29.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#fig29.set_facecolor("none")
#st.pyplot(fig29,title="Distribution of promotions by category")

#st.dataframe(secuel.get_promotion_vs_not_across_categories())

#fig29 = px.pie(q29, values="% promo vs. total", names='Category', title='Distribution of promotions by category')
#st.plotly_chart(fig29, use_container_width=True) 

layout = go.Layout(
   {
      "title":"Distribution of promotions by category"})
fig29a = go.Figure(data=[go.Pie(labels=q29["Category"], values=q29["% promo vs. total"], hole=.3)],layout=layout)
st.plotly_chart(fig29a, use_container_width=True)


st.header("2) Looking for a specific Promo activation")
st.write("For the following section, if you want to get access to the promo details from a specific category please do provide a category in the filter below.")
option2A = st.selectbox(
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

q28A = secuel.get_promotion_vs_not_across_subcategories(option2A)
#fig28A = px.bar(q28A, x="Subcategory", y="Number of products WITH promotion",title="Promotional Activity across subcategories",color="Subcategory")
#st.plotly_chart(fig28A, use_container_width=True)

fig28B = px.bar(
    data_frame = q28A,
    x = "Subcategory",
    y = ["Number of products WITHOUT promotion","Number of products WITH promotion"],
    opacity = 0.9,
    orientation = "v",
    barmode = 'stack',
    title=f'Number of products in promo vs. not by subcategory within <b>{option2A}</b>')
st.plotly_chart(fig28B, use_container_width=True)

st.write("You can also filter by the subcategory you are most interested in to see what products are currently on promotion")
option2B = st.selectbox("Please choose a subcategory:", (secuel.get_subcategory_counts_by_given_category (option2A)))
st.dataframe(secuel.get_promotion_count_across_subcategories(option2B))
st.dataframe(secuel.get_promotion_across_subcategories(option2B))



q29 = st.dataframe(secuel.get_promotion_vs_not_across_for_a_given_brand(option2B))
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

q30 = secuel.get_promotion_vs_not_across_for_a_given_brand(option2B)
fig30 = px.bar(q30, x="Brand", y="Number of products WITH promotion",title="Number of products WITH promotion by Brand",color="Number of products WITH promotion")
st.plotly_chart(fig30, use_container_width=True)