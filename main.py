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
    page_title="UK Supermarket Analysis",
    page_icon="🛒")

cover = Image.open("../final_project/tesco_logo.png")
st.image(cover, use_column_width=True)

#st.markdown("# Main page")
#st.sidebar.markdown("# Main page")



st.title('Welcome to my final project')
st.header("Introduction & objectives")
st.write("The main goal for this project has been to test everything I have learned over the last couple of months as part of the Data Analytics bootcamp.")
st.write("Therefore, and given my previous background in Fast Moving Consumer Gooods (FMCG), I thought it would be a great idea to _**have a dashboard that would easily help me (a consumer/user) get all the public information across the British supermarkets**_ in order to decide whether I should buy a given product/category/brand in a supermarket or another.")
st.write("Given the main goal above, the objectives for this project are:")
st.write("1) Start with Tesco (UK market leader) as the first component of this dashboard to test whether it works as expected.")
st.write("2) Web scraping from Tesco's website so I could get:")
st.write("a) Product name, price, category, promotions, etc.")
st.write("b) GDA (Guideline Daily Amounts) information & product reviews given by customers, where applicable.")
st.write("c) Sentiment Analysis of a given product/category/brand")
st.write("3) Deep dive analysis of Tesco's brands, categories & subcategories within different scenarios: stock issues, promotions, innovation, etc.")


st.header("Let's jump into the different sections to see what the data gathered looks like!")


st.header("Conclusions & Next Steps")

st.write("Now that we can see the analysis for Tesco works and that you can get different insights depending on the information you select, the idea would be to do the following:")
st.write("1) Extend the analysis to the key British supermarket chains in order to get a comparison by category/brand.")
st.write("2) Weekly update of this analysis so historical data can be gathered as well as price predictions can be calculated given the historical.")
st.write("3) Add GDA (aka nutritional values of the products) to the analysis to get a better understanding of how much these relate to price & promotions and what impact the new HFSS (High in Fat, Salt & Sugar) legislation on food products is going to have across the market.")
# Choose Tesco (UK market leader) as the first component of this dashboard to test whether it works as expected.")