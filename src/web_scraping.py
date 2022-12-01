import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
import numpy as np
from tqdm.notebook import tqdm, trange

 # 1) Getting main information once providing a list with the urls you are after

def give_me_main_product_info(url_list):
    product_name = []
    product_price = []
    promo_on = []
    price_kg = []
    category = []
    new_or_not = []
    product_id = []
    link_to_product = []
    link_to_image = []
    in_stock = []

    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

   

    for link in tqdm(url_list):
        
        for page in range(1,85): 
            
            html = requests.get(link + str(page), headers=headers)
            soup = BeautifulSoup(html.content, "html.parser")
            prod_details = soup.find_all("div", attrs={"class":"product-details--wrapper"})
            is_it_new = soup.find_all("div", attrs={"class":"styles__StyledVerticalTileWrapper-dvv1wj-0 dtCNPH"})
            prod_id_details = soup.find_all("div", attrs={"class":"styles__StyledTiledContent-dvv1wj-3 bcglTg"})
            prod_details_link = soup.find_all("a", attrs={"class": "product-image-wrapper"})
            for i in range(len(prod_details)):
                if len(prod_details[i].find_all("span")[0].getText()) != 0:
                    product_name.append(prod_details[i].find_all("span")[0].getText())                 
                if len(prod_details[i].find_all("span")[0].getText()) == 0:
                    product_name.append(np.nan)
                if len(prod_details[i].find_all("p", attrs={"class":"styled__StyledHeading-sc-119w3hf-2 jWPEtj styled__Text-sc-8qlq5b-1 lnaeiZ beans-price__text"})) != 0:
                    product_price.append(prod_details[i].find_all("p", attrs={"class":"styled__StyledHeading-sc-119w3hf-2 jWPEtj styled__Text-sc-8qlq5b-1 lnaeiZ beans-price__text"})[0].getText())                 
                if len(prod_details[i].find_all("p", attrs={"class":"styled__StyledHeading-sc-119w3hf-2 jWPEtj styled__Text-sc-8qlq5b-1 lnaeiZ beans-price__text"})) == 0:
                    product_price.append(np.nan)
                if len(prod_details[i].find_all("p", attrs={"styled__StyledFootnote-sc-119w3hf-7 icrlVF styled__Subtext-sc-8qlq5b-2 bNJmdc beans-price__subtext"})) != 0:
                    price_kg.append(prod_details[i].find_all("p", attrs={"styled__StyledFootnote-sc-119w3hf-7 icrlVF styled__Subtext-sc-8qlq5b-2 bNJmdc beans-price__subtext"})[0].getText()) 
                if len(prod_details[i].find_all("p", attrs={"styled__StyledFootnote-sc-119w3hf-7 icrlVF styled__Subtext-sc-8qlq5b-2 bNJmdc beans-price__subtext"})) == 0:
                    price_kg.append(np.nan)
                if len(prod_details[i].find_all("div", attrs={"":"product-info-message with-warning-background unavailable-messages"})) != 0:
                    in_stock.append(prod_details[i].find_all("div", attrs={"":"product-info-message with-warning-background unavailable-messages"}).getText())
                if len(prod_details[i].find_all("div", attrs={"":"product-info-message with-warning-background unavailable-messages"})) == 0:
                    in_stock.append(np.nan)
                if prod_details[i].find_all("p")[0].getText() == "Aldi Price Match":
                    promo_on.append(prod_details[i].find_all("p")[0].getText()) 
                elif len(prod_details[i].find_all("span", attrs={"offer-text"})) != 0:
                    promo_on.append(prod_details[i].find_all("span", attrs={"offer-text"})[0].getText()) 
                else:
                    promo_on.append(np.nan)
                category.append(link)
            for i in range(len(is_it_new)):
                if len(is_it_new[i].find_all("strong", attrs={"class":"styled__FlashSashText-sc-9znnul-1 ggeHk"})) != 0:
                    new_or_not.append(is_it_new[i].find_all("strong", attrs={"class":"styled__FlashSashText-sc-9znnul-1 ggeHk"})[0].getText())                 
                else:
                    new_or_not.append(np.nan)
                    
            for i in range(len(prod_details_link)):
                try:

                    if len(prod_details_link[i].get("href")) != 0:
                        link_to_product.append(prod_details_link[i].get("href"))
                    else: 
                        link_to_product.append(np.nan)
                    image_link_details = soup.find_all("img", attrs={"class":"styled__Image-sjvkdn-0 bJErKA product-image beans-responsive-image__image"})
                    link_to_image.append(image_link_details[i]["srcset"].split(" ")[0])
                except:
                    link_to_image.append(np.nan) 


            for i in range(len(prod_id_details)):
                if len(prod_id_details[i]["id"].split("-")[1]) != 0:
                    product_id.append(prod_id_details[i]["id"].split("-")[1])
                else:
                    product_id.append(np.nan)

    print(len(price_kg))  
    print(len(promo_on))    
    print(len(product_name))
    print(len(product_price))
    print(len(new_or_not))
    print(len(category))
    print(len(product_id)) 
    print(len(link_to_product))
    print(len(link_to_image))
    print(len(in_stock))


# 2) Getting the brand information when providing the html for a given category

def give_me_brand_info(html_path):

    brand_list = []
    brand_url = []

    with open(html_path, 'r') as brands:
        html_string = brands.read()
        soup = BeautifulSoup(html_string)
        prod_details = soup.find_all("div", attrs={"id": "filter-brands"})
        getting_brands = prod_details[0].find_all("li", {"class": "filter-option__container"})#[0].getText().strip("Filter by").split("\xa0")[0]
        x = prod_details[0].find_all("a", {"class": "filter-option--link"})

        for i in range(len(getting_brands)):
            if len(getting_brands[i]) != 0:
                brand_list.append(getting_brands[i].getText().strip("Filter by").split("\xa0")[0])
            if len(getting_brands[i]) == 0:
                brand_list.append(np.nan)
            if len(x[i]) != 0:
                brand_url.append(x[i].get("href"))
            else:
                brand_url.append(np.nan)
                
    print(len(brand_list))
    print(len(brand_url))


# 3) Getting brand & product links:

def give_me_only_brand_by_product(brand_url):
    product_id = []
    brand_link = []
    product_name = []

    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    for link in tqdm(brand_url):
        for page in range(1,15):
            
            # 1. Request a brand
            html = requests.get(link + str(page), headers=headers)
            soup = BeautifulSoup(html.content, "html.parser")
            
            # 2. Get a list of all products
            prod_details = soup.find_all("div", attrs={"class":"product-details--wrapper"})
            prod_id_details = soup.find_all("div", attrs={"class":"styles__StyledTiledContent-dvv1wj-3 bcglTg"})  
            
            try:
                #3. Get details for each product
                for i in range(len(prod_details)):
                    if len(prod_details[i].find_all("span")[0].getText()) != 0:
                        product_name.append(prod_details[i].find_all("span")[0].getText())                 
                    else:
                        product_name.append(np.nan)
                    brand_link.append(link)
                #4. Get ID for each product
                for i in range(len(prod_id_details)):
                    if len(prod_id_details[i]["id"].split("-")[1]) != 0:
                        product_id.append(prod_id_details[i]["id"].split("-")[1])
                    else:
                        product_id.append(np.nan)
            
            except:
                print(f"There was an error on iteration {page} in link {link}")

    print(len(product_id))
    print(len(product_name))
    print(len(brand_link))


# 4) Getting manufacturers' addresses

def manuf_addresses(df):
    for link in tqdm(df["Product Link"]):
    
        pattern = "([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})"
        headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }
        html = requests.get(link, headers=headers)
        soup = BeautifulSoup(html.content, "html.parser")
        address_details = soup.find_all("div", attrs={"class":"product-info-block product-info-block--manufacturer-address"})
    
    whole_link.append(link)
    try:
        x = address_details[0].getText()
        postcode = re.findall(pattern, x)[0]
        postcode_details.append(postcode[1])
    except:
        postcode_details.append(np.nan) 
    print(len(postcode_details))
    print(len(whole_link))