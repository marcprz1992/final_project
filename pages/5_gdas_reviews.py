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
    page_title="Sentiment Analysis & GDAs")

#st.markdown("# Page 2")
#st.sidebar.markdown("# Page 2")

st.title("Sentiment Analysis & GDAs")
cover = Image.open("../final_project/fruits.jpg")
st.image(cover, use_column_width=True)


st.header("1) Analysing the customer sentiment")


option5A = st.selectbox(
    'Please provide a category to see the average sentiment for that category:',
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

q5A = secuel.get_avg_sentiment_for_my_category(option5A)
#q34.plot(x="Brand", y=["Average Positive Sentiment", "Average Negative Sentiment", "Average Neutral Sentiment","Average Compound"], kind="bar", figsize=(9, 8),title='Average Sentiment Analysis for the Brand')

fig4A = px.bar(
    data_frame = q5A,
    x = ["Average Positive Sentiment", "Average Negative Sentiment", "Average Neutral Sentiment","Average Compound"],
    y = "Category",
    opacity = 0.9,
    orientation = "h",
    barmode = 'group',
    title='Average sentiment for the category')
st.plotly_chart(fig4A, use_container_width=True)

st.write("You can also filter by the subcategory to see what the average sentiment for a specific subcategory is.")
option5B = st.selectbox("Please choose a subcategory:", (secuel.get_subcategory_counts_by_given_category (option5A)))

q5B = secuel.get_avg_sentiment_for_my_subcategory(option5B)

fig5A = px.bar(
    data_frame = q5B,
    y = ["Average Positive Sentiment", "Average Negative Sentiment", "Average Neutral Sentiment","Average Compound"],
    x = "Subcategory",
    opacity = 0.9,
    orientation = "v",
    barmode = 'group',
    title='Average sentiment for the subcategory')
st.plotly_chart(fig5A, use_container_width=True)


st.write("If you also want to have a look at the average sentiment for a given brand, you can do it by searching in the below.")
option5C = st.selectbox("Please choose a brand:", (secuel.get_all_brands_available()))
q5C = secuel.get_avg_sentiment_for_my_brand(option5C)

fig6A = px.bar(
    data_frame = q5C,
    y = ["Average Positive Sentiment", "Average Negative Sentiment", "Average Neutral Sentiment","Average Compound"],
    x = "Brand",
    opacity = 0.9,
    orientation = "v",
    barmode = 'group',
    title='Average sentiment for the brand')
st.plotly_chart(fig6A, use_container_width=True)



st.write("You can also search for a specific product to get the average review as well as the product visual and actual review.")
option5D = st.selectbox("Please choose a product:", (secuel.get_all_products_available()))
q5D = secuel.get_avg_sentiment_for_my_product(option5D)

fig7A = px.bar(
    data_frame = q5D,
    y = ["Average Positive Sentiment", "Average Negative Sentiment", "Average Neutral Sentiment","Average Compound"],
    x = "Product Name",
    opacity = 0.9,
    orientation = "v",
    barmode = 'group',
    title='Average sentiment for the product')
st.plotly_chart(fig7A, use_container_width=True)


q5E1 = secuel.get_reviews(option5D)
my_figure = secuel.give_me_a_wordcloud(q5E1)
fig7B, ax = plt.subplots(figsize = (12, 8))
ax.imshow(my_figure)
plt.axis("off")
st.pyplot(fig7B)
#q5E = secuel.get_a_cool__visual_from_df(q5E1,option5D,"../final_project/review_trial1.jpg")