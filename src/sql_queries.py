import pandas as pd
import sqlalchemy as alch
from getpass import getpass
import re
import numpy as np
import requests
import seaborn as sns
import matplotlib.pyplot as plt
import stylecloud
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from IPython.display import Image
import wordcloud as wc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as mp
from streamlit import secrets

sns.set_context("poster")
sns.set(rc={"figure.figsize": (12.,6.)})
sns.set_style("whitegrid")
dbName=secrets["dbName"]
password = secrets["password"]
connectionData = f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)
engine.connect()

# 1) Number of products by category
def get_product_counts_by_category ():
    query = f"""SELECT Category, COUNT(product_id) as 'Number of products' 
    FROM final_project_ironhack.main_product_info
    GROUP BY Category
    ORDER BY COUNT(product_id) DESC;"""
    df = pd.read_sql_query(query, engine)
    return df

# 2) Number of products by subcategory 
def get_product_counts_by_subcategory ():
    query = f"""SELECT Subcategory, COUNT(product_id) as 'Number of products' 
    FROM final_project_ironhack.main_product_info
    GROUP BY Subcategory
    ORDER BY COUNT(product_id) DESC;"""
    df = pd.read_sql_query(query, engine)
    return df

# 3) Number of products by subcategory for a given category (parameter) - PANDAS
def get_subcategory_counts_by_given_category (category):
    query = f"""SELECT Subcategory, COUNT(product_id) as 'Number of products' 
    FROM final_project_ironhack.main_product_info
    WHERE Category LIKE '%%{category}%%'
    GROUP BY Subcategory
    ORDER BY COUNT(product_id) DESC;"""
    df = pd.read_sql_query(query, engine)
    return df
# 3A
def get_products_by_given_subcategory (subcategory):
    query = f"""SELECT product_name 
    FROM final_project_ironhack.main_product_info
    WHERE Subcategory LIKE '%%{subcategory}%%'
    ORDER BY product_name ASC;"""
    df = pd.read_sql_query(query, engine)
    return df

# 3B) Getting product counts by given subcategory (parameter) - PANDAS
def get_product_counts_by_given_subcategory (subcategory):
    query = f"""SELECT COUNT(product_name) as "Total number of products within {subcategory}" 
    FROM final_project_ironhack.main_product_info
    WHERE Subcategory LIKE '%%{subcategory}%%';"""
    df = pd.read_sql_query(query, engine)
    return df

# 4) Top 5 products by price - PANDAS
def get_top_5_by_price ():
    query = f"""SELECT product_name, Price 
    FROM final_project_ironhack.main_product_info
    WHERE Price != "No price info for this product"
    ORDER BY Price DESC
    LIMIT 5;"""
    df = pd.read_sql_query(query, engine)
    df.style
    return df

# 5) Getting the number of products without promotion by category - PANDAS
def get_no_promoted_products_by_category ():
    query = f"""SELECT Category, COUNT(product_id) as "Number of products WITHOUT promotion" 
    FROM final_project_ironhack.main_product_info
    WHERE Promotion = "No promotion"
    GROUP BY Category
    ORDER BY COUNT(product_id) DESC;"""
    df = pd.read_sql_query(query, engine)
    return df

# 6) Getting the number of products with promotion by category - PANDAS
def get_promoted_products_by_category ():
    query = f"""SELECT Category, COUNT(product_id) as "Number of products WITH promotion" 
    FROM final_project_ironhack.main_product_info
    WHERE Promotion != "No promotion"
    GROUP BY Category
    ORDER BY COUNT(product_id) DESC;"""
    df = pd.read_sql_query(query, engine)
    return df

# 7) Getting the number of products without promotion by subcategory - PANDAS
def get_no_promoted_products_by_subcategory ():
    query = f"""SELECT Subcategory, COUNT(product_id) as "Number of products WITHOUT promotion" 
    FROM final_project_ironhack.main_product_info
    WHERE Promotion = "No promotion"
    GROUP BY Subcategory
    ORDER BY COUNT(product_id) DESC;"""
    df = pd.read_sql_query(query, engine)
    return df

# 8) Getting the number of products without promotion by subcategory - PANDAS
def get_no_promoted_products_by_subcategory ():
    query = f"""SELECT Subcategory, COUNT(product_id) as "Number of products WITH promotion" 
    FROM final_project_ironhack.main_product_info
    WHERE Promotion != "No promotion"
    GROUP BY Subcategory
    ORDER BY COUNT(product_id) DESC; """
    df = pd.read_sql_query(query, engine)
    return df

# 9) Getting the number of new products by category - PANDAS
def get_innovation_by_category ():
    query = f"""SELECT Category, COUNT(product_id) as "Number of NEW products" 
    FROM final_project_ironhack.main_product_info
    WHERE Innovation = "New"
    GROUP BY Category
    ORDER BY COUNT(product_id) DESC;  """
    df = pd.read_sql_query(query, engine)
    return df

# 10) Getting the number of new products by subcategory - PANDAS
def get_innovation_by_subcategory ():
    query = f"""SELECT Subcategory, COUNT(product_id) as "Number of NEW products" 
    FROM final_project_ironhack.main_product_info
    WHERE Innovation = "New"
    GROUP BY Subcategory
    ORDER BY COUNT(product_id) DESC;   """
    df = pd.read_sql_query(query, engine)
    return df

# 11) Getting price and promo for a given product - PANDAS
def get_price_promo_from_product(product):
    query = f"""SELECT product_name, Price, Promotion
    FROM final_project_ironhack.main_product_info
    WHERE product_name LIKE '%%{product}%%'
    AND Price != "No price info for this product"
    ORDER BY Price DESC;    """
    df = pd.read_sql_query(query, engine)
    return df

# 12) Getting price and promo for a given product - PANDAS
def get_avg_price_from_category(category):
    query = f"""SELECT Category, ROUND(AVG(Price),2) AS "Average Price"
    FROM final_project_ironhack.main_product_info
    WHERE Category LIKE '%%{category}%%'
    AND Price != "No price info for this product"
    ORDER BY ROUND(AVG(Price),2) DESC;     """
    df = pd.read_sql_query(query, engine)
    return df

# 13) Getting avg price for all categories - PANDAS
def get_avg_price_for_all_categories():
    query = f"""SELECT Category, ROUND(AVG(Price),2) AS "Average Price"
    FROM final_project_ironhack.main_product_info
    WHERE Price != "No price info for this product"
    GROUP BY Category
    ORDER BY ROUND(AVG(Price),2) DESC;      """
    df = pd.read_sql_query(query, engine)
    return df

# 14) Getting avg price for all categories - PANDAS
def get_avg_price_for_all_subcategories(category):
    query = f"""SELECT Subcategory, ROUND(AVG(Price),2) AS "Average Price"
    FROM final_project_ironhack.main_product_info
    WHERE Price != "No price info for this product"
    AND Category LIKE '%%{category}%%'
    GROUP BY Subcategory
    ORDER BY ROUND(AVG(Price),2) ASC;       """
    df = pd.read_sql_query(query, engine)
    return df

# 14A) Getting avg price for all brands within a category - PANDAS
def get_avg_price_for_all_brands(subcategory):
    query = f"""SELECT 
    br.Brand,
    ROUND(AVG(Price),2) AS "Average Price"
    FROM final_project_ironhack.main_product_info mpi
    LEFT JOIN brand_product_info bpi USING(product_id)
    LEFT JOIN brand_general_info br USING(brand_url)
    WHERE Price != "No price info for this product"
    AND Subcategory LIKE '%%{subcategory}%%'
    GROUP BY Brand
    ORDER BY ROUND(AVG(Price),2) ASC;       """
    df = pd.read_sql_query(query, engine)
    return df


# 15) First join: main info & brand - PANDAS
def get_main_info_and_brand():
    query = f"""SELECT 
    mpi.product_name,
    br.Brand,
    mpi.Price
    FROM main_product_info mpi
    LEFT JOIN brand_product_info bpi USING(product_id)
    LEFT JOIN brand_general_info br USING(brand_url)
    WHERE Price != "No price info for this product"
    AND Brand IS NOT NULL
    ORDER BY Price DESC;"""
    df = pd.read_sql_query(query, engine)
    return df

# 16) Second join: top 10 brands by average price - PANDAS
def get_brand_and_avg_price():
    query = f"""SELECT 
    br.Brand,
    ROUND(AVG(mpi.Price),2) as "Average Price"
    FROM main_product_info mpi
    LEFT JOIN brand_product_info bpi USING(product_id)
    LEFT JOIN brand_general_info br USING(brand_url)
    WHERE Price != "No price info for this product"
    AND Brand IS NOT NULL
    GROUP BY Brand
    ORDER BY AVG(Price) DESC
    LIMIT 10; """
    df = pd.read_sql_query(query, engine)
    return df

# 17) Third join: average price for a brand requested (parameter) - PANDAS
def get_one_brand_and_avg_price(brand):
    query = f"""SELECT 
    br.Brand,
    ROUND(AVG(mpi.Price),2) as "Average Price"
    FROM main_product_info mpi
    LEFT JOIN brand_product_info bpi USING(product_id)
    LEFT JOIN brand_general_info br USING(brand_url)
    WHERE Price != "No price info for this product"
    AND Brand IS NOT NULL
    AND Brand LIKE '%%{brand}%%'
    GROUP BY Brand
    ORDER BY AVG(Price) DESC
    LIMIT 1;  """
    df = pd.read_sql_query(query, engine)
    return df

# 18) Fourth join: number of products on promo for a brand requested (parameter)
def get_count_promoted_products_by_brand(brand):
    query = f"""SELECT 
    br.Brand,
    COUNT(mpi.product_id) as "Number of products ON PROMOTION"
    FROM main_product_info mpi
    LEFT JOIN brand_product_info bpi USING(product_id)
    LEFT JOIN brand_general_info br USING(brand_url)
    WHERE Promotion != "No promotion"
    AND Brand IS NOT NULL
    AND Brand LIKE '%%{brand}%%'
    GROUP BY Brand
    ORDER BY COUNT(mpi.product_id) DESC
    LIMIT 1;    """
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


# 19) What products from a specific brand are in promotion (parameter) - PANDAS
def get_actual_promoted_products_by_brand(brand):
    query = f"""SELECT 
    mpi.product_name,
    br.Brand
    FROM main_product_info mpi
    LEFT JOIN brand_product_info bpi USING(product_id)
    LEFT JOIN brand_general_info br USING(brand_url)
    WHERE Promotion != "No promotion"
    AND Brand IS NOT NULL
    AND Brand LIKE '%%{brand}%%'
    ORDER BY product_name DESC;"""
    df = pd.read_sql_query(query, engine)
    return df

# 20) Top 10 brands with stock issues - PANDAS
def get_top_10_brands_with_stock_issues():
    query = f"""SELECT 
    br.Brand,
    COUNT(mpi.stock_status) as "Number of products WITHOUT stock"
    FROM main_product_info mpi
    LEFT JOIN brand_product_info bpi USING(product_id)
    LEFT JOIN brand_general_info br USING(brand_url)
    WHERE stock_status != "All good"
    AND Brand IS NOT NULL
    GROUP BY Brand
    ORDER BY COUNT(mpi.stock_status) DESC
    LIMIT 10;"""
    df = pd.read_sql_query(query, engine)
    return df

# 21) Number of products without stock for a given brand (parameter) - PANDAS
def get_count_stock_issues_for_a_given_brand(brand):
    query = f"""SELECT 
    br.Brand,
    COUNT(mpi.stock_status) as "Number of products WITHOUT stock"
    FROM main_product_info mpi
    LEFT JOIN brand_product_info bpi USING(product_id)
    LEFT JOIN brand_general_info br USING(brand_url)
    WHERE stock_status != "All good"
    AND Brand IS NOT NULL
    AND Brand LIKE '%%{brand}%%'
    ORDER BY COUNT(mpi.stock_status) DESC
    LIMIT 10; """
    df = pd.read_sql_query(query, engine)
    return df

# 22) Details on the products without stock for a given brand (parameter) - PANDAS
def get_products_stock_issues_for_a_given_brand(brand):
    query = f"""SELECT 
    mpi.product_name,
    br.Brand
    FROM main_product_info mpi
    LEFT JOIN brand_product_info bpi USING(product_id)
    LEFT JOIN brand_general_info br USING(brand_url)
    WHERE stock_status != "All good"
    AND Brand IS NOT NULL
    AND Brand LIKE '%%{brand}%%'
    ORDER BY mpi.product_name ASC;  """
    df = pd.read_sql_query(query, engine)
    return df

# 23) Products WITHOUT stock by category - PANDAS
def get_products_stock_issues_by_category():
    query = f"""SELECT 
    Category,
    COUNT(Innovation) as "Total Number of products",
    COUNT(CASE WHEN stock_status != 'All good' THEN 1 ELSE NULL END) as "Number of products WITHOUT stock",
    COUNT(CASE WHEN stock_status = 'All good' THEN 1 ELSE NULL END) as "Number of products WITH stock"
    FROM main_product_info
    GROUP BY Category
    ORDER BY COUNT(CASE WHEN stock_status != 'All good' THEN 1 ELSE NULL END) DESC;  """
    df = pd.read_sql_query(query, engine)
    return df

def giveme_percentages_stock(dataframe):
    percentages = []
    for item,row in dataframe.iterrows():
        percentages.append(round(row["Number of products WITHOUT stock"] / row["Total Number of products"],2))
    dataframe["%_of_total"] = percentages
    return dataframe

def giveme_percentages_innovation(dataframe):
    percentages = []
    for item,row in dataframe.iterrows():
        percentages.append(round(row["New products"] / row["Total Number of products"],2))
    dataframe["%_of_total"] = percentages
    return dataframe



# 24) Details on the products WITHOUT stock for a given category - PANDAS
def get_products_stock_issues_by_given_category(category):
    query = f"""SELECT 
    product_name,
    Category
    FROM main_product_info
    WHERE stock_status != "All good"
    AND Category LIKE '%%{category}%%'
    ORDER BY product_name ASC;   """
    df = pd.read_sql_query(query, engine)
    return df

# 25) Number of NPD products across all brands - PANDAS
def get_innovation_by_category():
    query = f"""SELECT 
    br.Brand,
    COUNT(mpi.Innovation) as "Number of NEW products"
    FROM main_product_info mpi
    LEFT JOIN brand_product_info bpi USING(product_id)
    LEFT JOIN brand_general_info br USING(brand_url)
    WHERE Innovation = "New"
    AND Brand IS NOT NULL
    GROUP BY Brand
    ORDER BY COUNT(mpi.Innovation) DESC;    """
    df = pd.read_sql_query(query, engine)
    return df

# 26) Number of NPD products vs. NOT NPD for a given brand (parameter) - PANDAS
def get_innovation_by_given_brand(brand):
    query = f"""SELECT 
    br.Brand,
    COUNT(mpi.Innovation) as "Total Number of products",
    COUNT(CASE WHEN mpi.Innovation = 'New' THEN 1 ELSE NULL END) as "Number of NEW products",
    COUNT(CASE WHEN mpi.Innovation != 'New' THEN 1 ELSE NULL END) as "Rest of range"
    FROM main_product_info mpi
    LEFT JOIN brand_product_info bpi USING(product_id)
    LEFT JOIN brand_general_info br USING(brand_url)
    WHERE Brand LIKE '%%{brand}%%';     """
    df = pd.read_sql_query(query, engine)
    return df

# 27) Number of NPD products across all categories vs. NOT NPD - PANDAS
def get_innovation_vs_not_across_categories():
    query = f"""SELECT 
    Category,
    COUNT(mpi.Innovation) as "Total Number of products",
    COUNT(CASE WHEN Innovation = 'New' THEN 1 ELSE NULL END) as "Number of NEW products",
    COUNT(CASE WHEN Innovation != 'New' THEN 1 ELSE NULL END) as "Rest of range"
    FROM main_product_info mpi
    GROUP BY Category
    ORDER BY COUNT(CASE WHEN Innovation = 'New' THEN 1 ELSE NULL END) DESC;      """
    df = pd.read_sql_query(query, engine)
    return df

# 28) Number of products in promo vs. not by category - PANDAS
def get_promotion_vs_not_across_categories():
    query = f"""SELECT 
    Category,
    COUNT(Promotion) as "Total Number of products",
    COUNT(CASE WHEN Promotion = 'No promotion' THEN 1 ELSE NULL END) as "Number of products WITHOUT promotion",
    COUNT(CASE WHEN Promotion != 'No promotion' THEN 1 ELSE NULL END) as "Number of products WITH promotion"
    FROM main_product_info 
    GROUP BY Category
    ORDER BY COUNT(CASE WHEN Innovation != 'No promotion' THEN 1 ELSE NULL END) DESC;"""
    df = pd.read_sql_query(query, engine)
    return df

# 28C) Number of new products not by category - PANDAS
def get_innovation_vs_not_across_categories2():
    query = f"""SELECT 
    Category,
    COUNT(Innovation) as "Total Number of products",
    COUNT(CASE WHEN Innovation = 'New' THEN 1 ELSE NULL END) as "New products",
    COUNT(CASE WHEN Innovation != 'New' THEN 1 ELSE NULL END) as "Rest of range"
    FROM main_product_info 
    GROUP BY Category
    ORDER BY COUNT(CASE WHEN Innovation = 'New' THEN 1 ELSE NULL END) DESC;"""
    df = pd.read_sql_query(query, engine)
    return df

# Caveat to get the percentages from query 28:

def giveme_percentages(dataframe):
    percentages = []
    for item,row in dataframe.iterrows():
        percentages.append(round(row["Number of products WITH promotion"] / row["Total Number of products"],2))
    dataframe["% promo vs. total"] = percentages
    return dataframe

# 280A) Number of products in stock vs. not by given category - PANDAS
def get_stock_vs_not_across_subcategories(category):
    query = f"""SELECT 
    Subcategory,
    COUNT(Innovation) as "Total Number of products",
    COUNT(CASE WHEN stock_status != 'All good' THEN 1 ELSE NULL END) as "Number of products WITHOUT stock",
    COUNT(CASE WHEN stock_status = 'All good' THEN 1 ELSE NULL END) as "Number of products WITH stock"
    FROM main_product_info 
    WHERE Category LIKE '%%{category}%%'
    GROUP BY Subcategory
    ORDER BY COUNT(Innovation) DESC;"""
    df = pd.read_sql_query(query, engine)
    return df

# 280B) Same for innovation
def get_innov_vs_not_across_subcategories(category):
    query = f"""SELECT 
    Subcategory,
    COUNT(Innovation) as "Total Number of products",
    COUNT(CASE WHEN Innovation = 'New' THEN 1 ELSE NULL END) as "New products",
    COUNT(CASE WHEN Innovation != 'New' THEN 1 ELSE NULL END) as "Rest of range"
    FROM main_product_info 
    WHERE Category LIKE '%%{category}%%'
    GROUP BY Subcategory
    ORDER BY COUNT(Innovation) DESC;"""
    df = pd.read_sql_query(query, engine)
    return df
# 28A) Number of products in promo vs. not by given category - PANDAS
def get_promotion_vs_not_across_subcategories(category):
    query = f"""SELECT 
    Subcategory,
    COUNT(Promotion) as "Total Number of products",
    COUNT(CASE WHEN Promotion = 'No promotion' THEN 1 ELSE NULL END) as "Number of products WITHOUT promotion",
    COUNT(CASE WHEN Promotion != 'No promotion' THEN 1 ELSE NULL END) as "Number of products WITH promotion"
    FROM main_product_info 
    WHERE Category LIKE '%%{category}%%'
    GROUP BY Subcategory
    ORDER BY COUNT(Promotion) DESC;"""
    df = pd.read_sql_query(query, engine)
    return df

# 28B) Actual product list of products in promo vs. not by given subcategory - PANDAS
def get_promotion_across_subcategories(subcategory):
    query = f"""SELECT 
    product_name as 'Product Name', Promotion
    FROM main_product_info 
    WHERE Subcategory LIKE '%%{subcategory}%%' AND
    Promotion != 'No promotion'
    ORDER BY product_name DESC;"""
    df = pd.read_sql_query(query, engine)
    return df
 # 28BB)  product list count of products in promo vs. not by given subcategory - PANDAS
def get_promotion_count_across_subcategories(subcategory):
    query = f"""SELECT 
    COUNT(product_name) as "Total number of products on promotion within {subcategory}"
    FROM main_product_info 
    WHERE Subcategory LIKE '%%{subcategory}%%' AND
    Promotion != 'No promotion'
    ORDER BY product_name DESC;"""
    df = pd.read_sql_query(query, engine)
    return df  

 # 38BB)  Same for stock
def get_stock_count_across_subcategories(subcategory):
    query = f"""SELECT 
    COUNT(product_name) as "Total number of products out of stock within {subcategory}"
    FROM main_product_info 
    WHERE Subcategory LIKE '%%{subcategory}%%' AND
    stock_status != 'All good'
    ORDER BY product_name DESC;"""
    df = pd.read_sql_query(query, engine)
    return df  

# 38B) Same for Stock
def get_stock2_across_subcategories(subcategory):
    query = f"""SELECT 
    product_name as 'Product Name', stock_status as "Out of stock"
    FROM main_product_info 
    WHERE Subcategory LIKE '%%{subcategory}%%' AND
    stock_status != 'All good'
    ORDER BY product_name DESC;"""
    df = pd.read_sql_query(query, engine)
    return df

 # 38BC)  Same for innovation
def get_innov_count_across_subcategories(subcategory):
    query = f"""SELECT 
    COUNT(product_name) as "Total number of new products within {subcategory}"
    FROM main_product_info 
    WHERE Subcategory LIKE '%%{subcategory}%%' AND
    Innovation = 'New'
    ORDER BY product_name DESC;"""
    df = pd.read_sql_query(query, engine)
    return df  

# 38C) Same for innovation
def get_innov2_across_subcategories(subcategory):
    query = f"""SELECT 
    product_name as 'Product Name', Innovation
    FROM main_product_info 
    WHERE Subcategory LIKE '%%{subcategory}%%' AND
    Innovation = 'New'
    ORDER BY product_name DESC;"""
    df = pd.read_sql_query(query, engine)
    return df


# 29) Total Number of products & in promo vs. not by brand (parameter) - PANDAS
def get_promotion_vs_not_across_for_a_given_brand(subcategory):
    query = f"""SELECT 
    br.Brand,
    #COUNT(mpi.product_name) as "Total Number of products",
    #COUNT(CASE WHEN mpi.Promotion = 'No promotion' THEN 1 ELSE NULL END) as "Number of products WITHOUT promotion",
    COUNT(CASE WHEN mpi.Promotion != 'No promotion' THEN 1 ELSE NULL END) as "Number of products WITH promotion"
    FROM main_product_info mpi
    LEFT JOIN brand_product_info bpi USING(product_id)
    LEFT JOIN brand_general_info br USING(brand_url)
    WHERE Subcategory LIKE '%%{subcategory}%%'
    GROUP BY br.Brand
    ORDER BY COUNT(CASE WHEN mpi.Promotion != 'No promotion' THEN 1 ELSE NULL END) DESC
    LIMIT 20; """
    df = pd.read_sql_query(query, engine)
    return df


# 29) Same for stock
def get_stock_vs_not_across_for_a_given_brand(subcategory):
    query = f"""SELECT 
    br.Brand,
    #COUNT(mpi.product_name) as "Total Number of products",
    COUNT(CASE WHEN mpi.stock_status != 'All good' THEN 1 ELSE NULL END) as "Number of products WITHOUT stock"
    #COUNT(CASE WHEN mpi.stock_status = 'All good' THEN 1 ELSE NULL END) as "Number of products WITH stock"
    FROM main_product_info mpi
    LEFT JOIN brand_product_info bpi USING(product_id)
    LEFT JOIN brand_general_info br USING(brand_url)
    WHERE Subcategory LIKE '%%{subcategory}%%'
    GROUP BY br.Brand
    ORDER BY COUNT(CASE WHEN mpi.stock_status != 'All good' THEN 1 ELSE NULL END) DESC
    LIMIT 20; """
    df = pd.read_sql_query(query, engine)
    return df

# 29C) Same for innovation
def get_innov2_vs_not_across_for_a_given_brand(subcategory):
    query = f"""SELECT 
    br.Brand,
    #COUNT(mpi.product_name) as "Total Number of products",
    #COUNT(CASE WHEN mpi.Innovation != 'New' THEN 1 ELSE NULL END) as "Rest of range"
    COUNT(CASE WHEN mpi.Innovation = 'New' THEN 1 ELSE NULL END) as "New products"
    FROM main_product_info mpi
    LEFT JOIN brand_product_info bpi USING(product_id)
    LEFT JOIN brand_general_info br USING(brand_url)
    WHERE Subcategory LIKE '%%{subcategory}%%'
    GROUP BY br.Brand
    ORDER BY COUNT(CASE WHEN mpi.Innovation = 'New' THEN 1 ELSE NULL END) DESC
    LIMIT 20; """
    df = pd.read_sql_query(query, engine)
    return df

# 30) Getting the GDAs for a specific product (parameter) - PANDAS
def get_gdas(product_name):
    query = f"""SELECT
    mpi.product_name, 
    gda.Energy_kJ,
    gda.Kilocalories,
    gda.Fat,
    gda.Saturates,
    gda.Sugars,
    gda.Salt
    FROM main_product_info mpi
    LEFT JOIN gdas_reviews_info_by_product gda USING(product_link)
    WHERE mpi.product_name LIKE '%%{product_name}%%'; ; """
    df = pd.read_sql_query(query, engine)
    return df

# 31) Getting the Average GDAs for a given brand (parameter) - PANDAS
def get_avg_gdas_brand(brand):
    query = f"""SELECT 
    br.Brand,
    ROUND(AVG(gda.Energy_kJ),2) as "Average Energy (kJ)",
    ROUND(AVG(gda.Kilocalories),2) as "Average Kilocalories",
    ROUND(AVG(gda.Fat),2) as "Average Fat",
    ROUND(AVG(gda.Saturates),2) as "Average Saturates",
    ROUND(AVG(gda.Sugars),2) as "Average Sugars",
    ROUND(AVG(gda.Salt),2) as "Average Salt"
    FROM brand_general_info br
    LEFT JOIN brand_product_info bpi USING(brand_url)
    LEFT JOIN main_product_info mpi USING(product_id)
    LEFT JOIN gdas_reviews_info_by_product gda USING(product_link)
    WHERE Brand LIKE '%%{brand}%%'
    AND Brand IS NOT NULL; """
    df = pd.read_sql_query(query, engine)
    return df

# 32) Getting the top 5 products with the most negative "neg" score from their reviews
def get_top5_products_most_neg_score():
    query = f"""SELECT 
    mpi.product_name,
    br.Brand,
    gda.neg
    FROM main_product_info mpi
    LEFT JOIN brand_product_info bpi USING(product_id)
    LEFT JOIN brand_general_info br USING(brand_url)
    LEFT JOIN gdas_reviews_info_by_product gda USING(product_link)
    WHERE Brand IS NOT NULL
    ORDER BY gda.neg DESC
    LIMIT 5; """
    df = pd.read_sql_query(query, engine)
    return df

# 33) Getting the sentiment for a given product (when review has been given), (parameter) - PANDAS
def get_sentiment_for_my_product(product_name):
    query = f"""SELECT 
    mpi.product_name,
    gda.pos,
    gda.neg,
    gda.neu,
    gda.compound
    FROM main_product_info mpi
    LEFT JOIN brand_product_info bpi USING(product_id)
    LEFT JOIN brand_general_info br USING(brand_url)
    LEFT JOIN gdas_reviews_info_by_product gda USING(product_link)
    WHERE mpi.product_name LIKE '%%{product_name}%%'; """
    df = pd.read_sql_query(query, engine)
    return df

# 34) Getting the average sentiment for a given brand (parameter) - PANDAS
def get_avg_sentiment_for_my_brand(brand):
    query = f"""SELECT 
    br.Brand,
    ROUND(AVG(gda.pos),2) as "Average Positive Sentiment",
    ROUND(AVG(gda.neg),2) as "Average Negative Sentiment",
    ROUND(AVG(gda.neu),2) as "Average Neutral Sentiment",
    ROUND(AVG(gda.compound),2) as "Average Compound"
    FROM main_product_info mpi
    LEFT JOIN brand_product_info bpi USING(product_id)
    LEFT JOIN brand_general_info br USING(brand_url)
    LEFT JOIN gdas_reviews_info_by_product gda USING(product_link)
    WHERE br.Brand LIKE '%%{brand}%%'; """
    df = pd.read_sql_query(query, engine)
    return df

# 34C) Getting the average sentiment for a given product (parameter) - PANDAS

def get_avg_sentiment_for_my_product(product_name):
    query = f"""SELECT 
    mpi.product_name as "Product Name",
    ROUND(AVG(gda.pos),2) as "Average Positive Sentiment",
    ROUND(AVG(gda.neg),2) as "Average Negative Sentiment",
    ROUND(AVG(gda.neu),2) as "Average Neutral Sentiment",
    ROUND(AVG(gda.compound),2) as "Average Compound"
    FROM main_product_info mpi
    LEFT JOIN gdas_reviews_info_by_product gda USING(product_link)
    WHERE mpi.product_name LIKE '%%{product_name}%%'; """
    df = pd.read_sql_query(query, engine)
    return df
# Getting a list with all the brands 
def get_all_brands_available():
    query = f"""SELECT 
    br.Brand
    #ROUND(AVG(gda.pos),2) as "Average Positive Sentiment",
    #ROUND(AVG(gda.neg),2) as "Average Negative Sentiment",
    #ROUND(AVG(gda.neu),2) as "Average Neutral Sentiment",
    #ROUND(AVG(gda.compound),2) as "Average Compound"
    FROM brand_general_info br
    GROUP BY Brand; """
    df = pd.read_sql_query(query, engine)
    return df

def get_all_products_available():
    query = f"""SELECT 
    mpi.product_name
    #ROUND(AVG(gda.pos),2) as "Average Positive Sentiment",
    #ROUND(AVG(gda.neg),2) as "Average Negative Sentiment",
    #ROUND(AVG(gda.neu),2) as "Average Neutral Sentiment",
    #ROUND(AVG(gda.compound),2) as "Average Compound"
    FROM main_product_info mpi
    GROUP BY product_name; """
    df = pd.read_sql_query(query, engine)
    return df


# 34B) Getting the average sentiment for a given category (parameter) - PANDAS
def get_avg_sentiment_for_my_category(category):
    query = f"""SELECT 
    mpi.Category,
    ROUND(AVG(gda.pos),2) as "Average Positive Sentiment",
    ROUND(AVG(gda.neg),2) as "Average Negative Sentiment",
    ROUND(AVG(gda.neu),2) as "Average Neutral Sentiment",
    ROUND(AVG(gda.compound),2) as "Average Compound"
    FROM main_product_info mpi
    LEFT JOIN gdas_reviews_info_by_product gda USING(product_link)
    WHERE mpi.Category LIKE '%%{category}%%'; """
    df = pd.read_sql_query(query, engine)
    return df

# 34BB) Getting the average sentiment for a given csubategory (parameter) - PANDAS
def get_avg_sentiment_for_my_subcategory(subcategory):
    query = f"""SELECT 
    mpi.Subcategory,
    ROUND(AVG(gda.pos),2) as "Average Positive Sentiment",
    ROUND(AVG(gda.neg),2) as "Average Negative Sentiment",
    ROUND(AVG(gda.neu),2) as "Average Neutral Sentiment",
    ROUND(AVG(gda.compound),2) as "Average Compound"
    FROM main_product_info mpi
    LEFT JOIN gdas_reviews_info_by_product gda USING(product_link)
    WHERE mpi.Subcategory LIKE '%%{subcategory}%%'; """
    df = pd.read_sql_query(query, engine)
    return df


# 35) Getting the reviews for a given product - PANDAS
def get_reviews(product_name):
    query = f"""SELECT 
    mpi.product_name,
    gda.customer_reviews
    FROM main_product_info mpi
    LEFT JOIN gdas_reviews_info_by_product gda USING(product_link)
    WHERE mpi.product_name LIKE '%%{product_name}%%'; """
    df = pd.read_sql_query(query, engine)
    return df

def give_me_a_wordcloud(df):
    review_ = df["customer_reviews"][0]   
    wordcloud_ = WordCloud().generate(review_)
    return wordcloud_




def get_a_cool__visual_from_df(df,product_name,path_visual):  
    stylecloud.gen_stylecloud(text=df.loc[df["product_name"] == f"{product_name}"]["customer_reviews"].values[0],
                              icon_name='fas fa-apple-alt',
                              background_color='white',
                              collocations=False,
                              output_name = f"{path_visual}")
    return Image(filename=f"{path_visual}")

# 36) Getting the top 10 products by customer rating - PANDAS
def get_top10_products_by_rating():
    query = f"""SELECT 
    mpi.product_name,
    gda.customer_rating
    FROM main_product_info mpi
    LEFT JOIN gdas_reviews_info_by_product gda USING(product_link)
    WHERE gda.customer_rating IS NOT NULL AND gda.customer_rating != "No ratings given yet" AND gda.customer_rating <= "5.0"
    ORDER BY gda.customer_rating DESC
    LIMIT 10;; """
    df = pd.read_sql_query(query, engine)
    return df

# 37) Getting the top 10 products by worst compound - PANDAS
def get_top10_products_by_worst_compound():
    query = f"""SELECT 
    mpi.product_name,
    gda.compound
    FROM main_product_info mpi
    LEFT JOIN gdas_reviews_info_by_product gda USING(product_link)
    WHERE gda.customer_reviews != "No reviews given yet"
    ORDER BY gda.compound ASC
    LIMIT 10; """
    df = pd.read_sql_query(query, engine)
    return df

# 38) Getting the links for both the actual product and the image (parameter) - PANDAS
def get_product_links(product_name):
    query = f"""SELECT 
    product_name,
    product_link,
    Image
    FROM main_product_info
    WHERE product_name LIKE '%%{product_name}%%'; """
    df = pd.read_sql_query(query, engine)
    return df

# 39) Relationship between number of products in promotion vs. not and their average gdas for a brand (parameter) - PANDAS
def get_relationship_gdas_promotions(brand):
    query = f"""SELECT 
    br.Brand,
    COUNT(mpi.Innovation) as "Total Number of products",
    COUNT(CASE WHEN mpi.Promotion = 'No promotion' THEN 1 ELSE NULL END) as "Number of products WITHOUT promotion",
    ROUND(AVG(CASE WHEN mpi.Promotion = 'No promotion' THEN gda.Saturates ELSE NULL END),2) as "Average Saturates when products in PROMOTION",
    COUNT(CASE WHEN mpi.Promotion != 'No promotion' THEN 1 ELSE NULL END) as "Number of products WITH promotion",
    ROUND(AVG(CASE WHEN mpi.Promotion != 'No promotion' THEN gda.Saturates ELSE NULL END),2) as "Average Saturates when products ARE NOT IN PROMOTION"
    FROM main_product_info mpi
    LEFT JOIN brand_product_info bpi USING(product_id)
    LEFT JOIN brand_general_info br USING(brand_url)
    LEFT JOIN gdas_reviews_info_by_product gda USING(product_link)
    WHERE Brand LIKE '%%{brand}%%';  """
    df = pd.read_sql_query(query, engine)
    return df

# 40) Relationship between number of products in promotion vs. not and their average gdas for a category (parameter) - PANDAS
def get_relationship_gdas_promotions_cat(category,brand):
    query = f"""SELECT 
    br.Brand,
    COUNT(mpi.Innovation) as "Total Number of products",
    COUNT(CASE WHEN mpi.Promotion = 'No promotion' THEN 1 ELSE NULL END) as "Number of products WITHOUT promotion",
    ROUND(AVG(CASE WHEN mpi.Promotion = 'No promotion' THEN gda.Saturates ELSE NULL END),2) as "Average Saturates when products in PROMOTION",
    COUNT(CASE WHEN mpi.Promotion != 'No promotion' THEN 1 ELSE NULL END) as "Number of products WITH promotion",
    ROUND(AVG(CASE WHEN mpi.Promotion != 'No promotion' THEN gda.Saturates ELSE NULL END),2) as "Average Saturates when products ARE NOT IN PROMOTION"
    FROM main_product_info mpi
    LEFT JOIN brand_product_info bpi USING(product_id)
    LEFT JOIN brand_general_info br USING(brand_url)
    LEFT JOIN gdas_reviews_info_by_product gda USING(product_link)
    WHERE Category LIKE '%%{category}%%'
    AND Brand LIKE '%%{brand}%%'
    -- GROUP BY Brand
    ORDER BY ROUND(AVG(CASE WHEN mpi.Promotion != 'No promotion' THEN gda.Saturates ELSE NULL END),2) DESC;   """
    df = pd.read_sql_query(query, engine)
    return df

# 41) Same as the brand one but by category - PANDAS
def get_relationship_gdas_category():
    query = f"""SELECT 
    mpi.Category,
    COUNT(mpi.Innovation) as "Total Number of products",
    COUNT(CASE WHEN mpi.Promotion = 'No promotion' THEN 1 ELSE NULL END) as "Number of products WITHOUT promotion",
    ROUND(AVG(CASE WHEN mpi.Promotion = 'No promotion' THEN gda.Saturates ELSE NULL END),2) as "Average Saturates when products in PROMOTION",
    COUNT(CASE WHEN mpi.Promotion != 'No promotion' THEN 1 ELSE NULL END) as "Number of products WITH promotion",
    ROUND(AVG(CASE WHEN mpi.Promotion != 'No promotion' THEN gda.Saturates ELSE NULL END),2) as "Average Saturates when products ARE NOT IN PROMOTION"
    FROM main_product_info mpi
    LEFT JOIN brand_product_info bpi USING(product_id)
    LEFT JOIN brand_general_info br USING(brand_url)
    LEFT JOIN gdas_reviews_info_by_product gda USING(product_link)
    GROUP BY Category
    ORDER BY ROUND(AVG(CASE WHEN mpi.Promotion != 'No promotion' THEN gda.Saturates ELSE NULL END),2) DESC;   """
    df = pd.read_sql_query(query, engine)
    return df

# 42) Manufacturer postcode by product (when info available) - PANDAS
def get_postcodes_by_category():
    query = f"""SELECT 
    mpi.product_name,
    mpi.Category,
    uk.Postcode
    FROM main_product_info mpi
    LEFT JOIN uk_postcode_by_product_manufacturer uk USING(product_link)
    WHERE uk.Postcode != "No manufacturer address for this product"
    ORDER BY mpi.Category DESC;   """
    df = pd.read_sql_query(query, engine)
    return df

# 43) Manufacturer postcode by product (when info available)- (parameter) - PANDAS
def get_postcodes_by_given_category(category):
    query = f"""SELECT 
    mpi.Category,
    uk.postcode,
    uk.latitude,
    uk.longitude
    FROM main_product_info mpi
    LEFT JOIN uk_postcode_by_product_manufacturer uk USING(product_link)
    WHERE mpi.Category LIKE '%%{category}%%'
    AND uk.postcode IS NOT NULL;   """
    df = pd.read_sql_query(query, engine)
    return df

# 44) Getting key info by category - PANDAS

def get_key_category_info():
    query = f"""SELECT 
    mpi.Category,
    mpi.Subcategory,
    mpi.Price,
    COUNT(mpi.Innovation) as "Total Number of products"
    FROM main_product_info mpi
    WHERE mpi.Price != 'No price info for this product'
    GROUP BY mpi.Subcategory
    -- ORDER BY COUNT(mpi.Innovation) DESC
    ORDER BY mpi.Subcategory DESC;   """
    df = pd.read_sql_query(query, engine)
    return df

