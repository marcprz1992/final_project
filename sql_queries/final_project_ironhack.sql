use final_project_ironhack;

ALTER TABLE main_product_info MODIFY product_link VARCHAR(60);
ALTER TABLE uk_postcode_by_product_manufacturer MODIFY product_link VARCHAR(60);
ALTER TABLE main_product_info MODIFY product_name VARCHAR(200);
ALTER TABLE main_product_info
  ADD CONSTRAINT contacts_pk 
    PRIMARY KEY (product_id,product_name,product_link);
    
ALTER TABLE brand_general_info MODIFY brand_url VARCHAR(200);
ALTER TABLE brand_general_info
	ADD CONSTRAINT contacts_pk 
		PRIMARY KEY (brand_url);   

ALTER TABLE brand_product_info MODIFY product_name VARCHAR(200);    
ALTER TABLE brand_product_info MODIFY brand_url VARCHAR(200);
ALTER TABLE brand_product_info
	ADD CONSTRAINT contacts_pk 
		PRIMARY KEY (product_id,product_name,brand_url);  

ALTER TABLE gdas_reviews_info_by_product MODIFY product_link VARCHAR(60);
ALTER TABLE gdas_reviews_info_by_product
	ADD CONSTRAINT contacts_pk 
		PRIMARY KEY (product_link); 

ALTER TABLE uk_postcode_by_product_manufacturer
  ADD CONSTRAINT contacts_pk 
    PRIMARY KEY (product_link);
        
        
-- Query 1:

SELECT Category, COUNT(product_id) as 'Number of products' 
    FROM final_project_ironhack.main_product_info
    GROUP BY Category
    ORDER BY COUNT(product_id) DESC;

-- Query 2

SELECT Subcategory, COUNT(product_id) as 'Number of products' 
    FROM final_project_ironhack.main_product_info
    GROUP BY Subcategory
    ORDER BY COUNT(product_id) DESC;
-- Query 3
SELECT Subcategory, COUNT(product_id) as 'Number of products' 
    FROM final_project_ironhack.main_product_info
    WHERE Category = 'drinks'
    GROUP BY Subcategory
    ORDER BY COUNT(product_id) DESC;

-- Query 4
SELECT product_name, Price 
    FROM final_project_ironhack.main_product_info
    WHERE Price != "No price info for this product"
    ORDER BY Price DESC
    LIMIT 20;    

-- Query 5
SELECT Category, COUNT(product_id) as "Number of products WITHOUT promotion" 
    FROM final_project_ironhack.main_product_info
    WHERE Promotion = "No promotion"
    GROUP BY Category
    ORDER BY COUNT(product_id) DESC;   

-- Query 6
SELECT Category, COUNT(product_id) as "Number of products WITH promotion" 
    FROM final_project_ironhack.main_product_info
    WHERE Promotion != "No promotion"
    GROUP BY Category
    ORDER BY COUNT(product_id) DESC; 

-- Query 7
SELECT Subcategory, COUNT(product_id) as "Number of products WITHOUT promotion" 
    FROM final_project_ironhack.main_product_info
    WHERE Promotion = "No promotion"
    GROUP BY Subcategory
    ORDER BY COUNT(product_id) DESC; 

-- Query 8
SELECT Subcategory, COUNT(product_id) as "Number of products WITH promotion" 
    FROM final_project_ironhack.main_product_info
    WHERE Promotion != "No promotion"
    GROUP BY Subcategory
    ORDER BY COUNT(product_id) DESC; 

-- Query 9
SELECT Category, COUNT(product_id) as "Number of NEW products" 
    FROM final_project_ironhack.main_product_info
    WHERE Innovation = "New"
    GROUP BY Category
    ORDER BY COUNT(product_id) DESC; 

-- Query 10
SELECT Subcategory, COUNT(product_id) as "Number of NEW products" 
    FROM final_project_ironhack.main_product_info
    WHERE Innovation = "New"
    GROUP BY Subcategory
    ORDER BY COUNT(product_id) DESC; 

-- Query 11
SELECT Subcategory, COUNT(product_id) as "Number of NEW products" 
    FROM final_project_ironhack.main_product_info
    WHERE Innovation = "New"
    GROUP BY Subcategory
    ORDER BY COUNT(product_id) DESC; 

-- Query 12
SELECT product_name, Price, Promotion
    FROM final_project_ironhack.main_product_info
    WHERE product_name LIKE "%chocolate%"
    AND Price != "No price info for this product"
    ORDER BY Price DESC; 

-- Query 13
SELECT Category, ROUND(AVG(Price),2) AS "Average Price"
    FROM final_project_ironhack.main_product_info
    WHERE Category LIKE "%home%"
    AND Price != "No price info for this product"
    ORDER BY ROUND(AVG(Price),2) DESC; 

-- Query 14
SELECT Category, ROUND(AVG(Price),2) AS "Average Price"
    FROM final_project_ironhack.main_product_info
    WHERE Price != "No price info for this product"
    GROUP BY Category
    ORDER BY ROUND(AVG(Price),2) DESC; 

-- Query 15
SELECT Subcategory, ROUND(AVG(Price),2) AS "Average Price"
    FROM final_project_ironhack.main_product_info
    WHERE Price != "No price info for this product"
    GROUP BY Subcategory
    ORDER BY ROUND(AVG(Price),2) ASC; 

-- Query 16 - Joining tables 1
SELECT 
mpi.product_name,
br.Brand,
mpi.Price
FROM main_product_info mpi
LEFT JOIN brand_product_info bpi USING(product_id)
LEFT JOIN brand_general_info br USING(brand_url)
WHERE Price != "No price info for this product"
AND Brand IS NOT NULL
ORDER BY Price DESC; 

-- Query 17 - Joining tables 2
SELECT 
br.Brand,
ROUND(AVG(mpi.Price),2) as "Average Price"
FROM main_product_info mpi
LEFT JOIN brand_product_info bpi USING(product_id)
LEFT JOIN brand_general_info br USING(brand_url)
WHERE Price != "No price info for this product"
AND Brand IS NOT NULL
GROUP BY Brand
ORDER BY AVG(Price) DESC
LIMIT 10; 

-- Query 18 - Joining tables 3
SELECT 
br.Brand,
ROUND(AVG(mpi.Price),2) as "Average Price"
FROM main_product_info mpi
LEFT JOIN brand_product_info bpi USING(product_id)
LEFT JOIN brand_general_info br USING(brand_url)
WHERE Price != "No price info for this product"
AND Brand IS NOT NULL
AND Brand LIKE "%tesco%"
GROUP BY Brand
ORDER BY AVG(Price) DESC; 

-- Query 19 - Joining tables 4
SELECT 
br.Brand,
ROUND(AVG(mpi.Price),2) as "Average Price"
FROM main_product_info mpi
LEFT JOIN brand_product_info bpi USING(product_id)
LEFT JOIN brand_general_info br USING(brand_url)
WHERE Price != "No price info for this product"
AND Brand IS NOT NULL
AND Brand LIKE "%finest%"
ORDER BY AVG(Price) DESC; 

-- Query 20 - Joining tables 5 All brands matching the string
SELECT 
br.Brand,
COUNT(mpi.product_id) as "Number of products ON PROMOTION"
FROM main_product_info mpi
LEFT JOIN brand_product_info bpi USING(product_id)
LEFT JOIN brand_general_info br USING(brand_url)
WHERE Promotion != "No promotion"
AND Brand IS NOT NULL
AND Brand LIKE "%tesco%"
GROUP BY Brand
ORDER BY COUNT(mpi.product_id) DESC; 

-- Query 20 - Joining tables 5 All brands matching the string
SELECT 
br.Brand,
COUNT(mpi.product_id) as "Number of products ON PROMOTION"
FROM main_product_info mpi
LEFT JOIN brand_product_info bpi USING(product_id)
LEFT JOIN brand_general_info br USING(brand_url)
WHERE Promotion != "No promotion"
AND Brand IS NOT NULL
AND Brand LIKE "%heinz%"
ORDER BY COUNT(mpi.product_id) DESC; 

-- Query 21 - What products from a specific brand are in promotion
SELECT 
mpi.product_name,
br.Brand
FROM main_product_info mpi
LEFT JOIN brand_product_info bpi USING(product_id)
LEFT JOIN brand_general_info br USING(brand_url)
WHERE Promotion != "No promotion"
AND Brand IS NOT NULL
AND Brand LIKE "%heinz%"
ORDER BY product_name DESC; 

-- Query 22 - Top 10 brands with stock issues
SELECT 
br.Brand,
COUNT(mpi.stock_status) as "Number of products WITHOUT stock"
FROM main_product_info mpi
LEFT JOIN brand_product_info bpi USING(product_id)
LEFT JOIN brand_general_info br USING(brand_url)
WHERE stock_status != "All good"
AND Brand IS NOT NULL
GROUP BY Brand
ORDER BY COUNT(mpi.stock_status) DESC
LIMIT 10; 

-- Query 23 - Number of products without stock for a given brand
SELECT 
br.Brand,
COUNT(mpi.stock_status) as "Number of products WITHOUT stock"
FROM main_product_info mpi
LEFT JOIN brand_product_info bpi USING(product_id)
LEFT JOIN brand_general_info br USING(brand_url)
WHERE stock_status != "All good"
AND Brand IS NOT NULL
AND Brand LIKE "%cadbury%"
ORDER BY COUNT(mpi.stock_status) DESC
LIMIT 10; 

-- Query 24 - Details on the products without stock for a given brand
SELECT 
mpi.product_name,
br.Brand
-- COUNT(mpi.stock_status) as "Number of products WITHOUT stock"
FROM main_product_info mpi
LEFT JOIN brand_product_info bpi USING(product_id)
LEFT JOIN brand_general_info br USING(brand_url)
WHERE stock_status != "All good"
AND Brand IS NOT NULL
AND Brand LIKE "%cadbury%"
ORDER BY mpi.product_name ASC; 

-- Query 25 - Products WITHOUT stock by category
SELECT 
Category,
COUNT(stock_status) as "Number of products WITHOUT stock"
FROM main_product_info
WHERE stock_status != "All good"
-- AND Brand LIKE "%cadbury%"
GROUP BY Category
ORDER BY COUNT(stock_status) DESC; 

-- Query 26 - Details on the products WITHOUT stock for a given category
SELECT 
product_name,
Category
FROM main_product_info
WHERE stock_status != "All good"
AND Category LIKE "%frozen%"
ORDER BY product_name ASC; 

-- Query 27 - Number of NPD products across all brands
SELECT 
br.Brand,
COUNT(mpi.Innovation) as "Number of NEW products"
FROM main_product_info mpi
LEFT JOIN brand_product_info bpi USING(product_id)
LEFT JOIN brand_general_info br USING(brand_url)
WHERE Innovation = "New"
AND Brand IS NOT NULL
GROUP BY Brand
ORDER BY COUNT(mpi.Innovation) DESC; 

-- Query 28 - Number of NPD products vs. NOT NPD for a given brand
SELECT 
br.Brand,
COUNT(mpi.Innovation) as "Total Number of products",
COUNT(CASE WHEN mpi.Innovation = 'New' THEN 1 ELSE NULL END) as "Number of NEW products",
COUNT(CASE WHEN mpi.Innovation != 'New' THEN 1 ELSE NULL END) as "Rest of range"
FROM main_product_info mpi
LEFT JOIN brand_product_info bpi USING(product_id)
LEFT JOIN brand_general_info br USING(brand_url)
WHERE Brand LIKE "%finest%"; 

-- Query 29 - Number of NPD products across all categories vs. NOT NPD
SELECT 
Category,
COUNT(mpi.Innovation) as "Total Number of products",
COUNT(CASE WHEN Innovation = 'New' THEN 1 ELSE NULL END) as "Number of NEW products",
COUNT(CASE WHEN Innovation != 'New' THEN 1 ELSE NULL END) as "Rest of range"
FROM main_product_info mpi
GROUP BY Category
ORDER BY COUNT(CASE WHEN Innovation = 'New' THEN 1 ELSE NULL END) DESC; 

-- Query 30 - Number of products in promo vs. not by category
SELECT 
Category,
COUNT(Promotion) as "Total Number of products",
COUNT(CASE WHEN Promotion = 'No promotion' THEN 1 ELSE NULL END) as "Number of products WITHOUT promotion",
COUNT(CASE WHEN Promotion != 'No promotion' THEN 1 ELSE NULL END) as "Number of products WITH promotion"
FROM main_product_info 
GROUP BY Category
ORDER BY COUNT(CASE WHEN Innovation != 'No promotion' THEN 1 ELSE NULL END) DESC;


-- Query 31 - Total Number of products & in promo vs. not by brand
SELECT 
br.Brand,
COUNT(mpi.Innovation) as "Total Number of products",
COUNT(CASE WHEN mpi.Promotion = 'No promotion' THEN 1 ELSE NULL END) as "Number of products WITHOUT promotion",
COUNT(CASE WHEN mpi.Promotion != 'No promotion' THEN 1 ELSE NULL END) as "Number of products WITH promotion"
FROM main_product_info mpi
LEFT JOIN brand_product_info bpi USING(product_id)
LEFT JOIN brand_general_info br USING(brand_url)
WHERE Brand LIKE "%finest%"; 

-- Query 32 - Getting the GDAs for a specific product
SELECT
mpi.product_name, 
gda.Energy_kJ,
gda.Kilocalories,
gda.Fat,
gda.Saturates,
gda.Sugars
FROM main_product_info mpi
LEFT JOIN gdas_reviews_info_by_product gda USING(product_link)
WHERE mpi.product_name LIKE "%Tesco Finest Belgian Chocolate Yule Log%"; 


-- Query 33 - Getting the Average GDAs for a given brand
SELECT 
br.Brand,
ROUND(AVG(gda.Energy_kJ),2) as "Average Energy (kJ)",
ROUND(AVG(gda.Kilocalories),2) as "Average Kilocalories",
ROUND(AVG(gda.Fat),2) as "Average Fat",
ROUND(AVG(gda.Saturates),2) as "Average Saturates",
ROUND(AVG(gda.Sugars),2) as "Average Sugars"
FROM brand_general_info br
LEFT JOIN brand_product_info bpi USING(brand_url)
LEFT JOIN main_product_info mpi USING(product_id)
LEFT JOIN gdas_reviews_info_by_product gda USING(product_link)
WHERE Brand LIKE "%finest%"
AND Brand IS NOT NULL;

-- Query 33 - Getting the top 5 products with the most negative "neg" score from their reviews
SELECT 
mpi.product_name,
br.Brand,
gda.neg
FROM main_product_info mpi
LEFT JOIN brand_product_info bpi USING(product_id)
LEFT JOIN brand_general_info br USING(brand_url)
LEFT JOIN gdas_reviews_info_by_product gda USING(product_link)
WHERE Brand IS NOT NULL
ORDER BY gda.neg DESC
LIMIT 5;

-- Query 34 - Getting the sentiment for a given product (when review has been given)
SELECT 
mpi.product_name,
gda.pos,
gda.neg,
gda.neu,
gda.compound
FROM main_product_info mpi
LEFT JOIN brand_product_info bpi USING(product_id)
LEFT JOIN brand_general_info br USING(brand_url)
LEFT JOIN gdas_reviews_info_by_product gda USING(product_link)
-- WHERE Brand IS NOT NULL
-- WHERE gda.customer_reviews != "No reviews given yet"
WHERE mpi.product_name LIKE "%Tesco Finest Belgian Chocolate Yule Log%";

-- Query 35 - Getting the average sentiment for a given brand
SELECT 
br.Brand,
ROUND(AVG(gda.pos),2) as "Average Positive Sentiment",
ROUND(AVG(gda.neg),2) as "Average Negative Sentiment",
ROUND(AVG(gda.neu),2) as "Average Neutral Sentiment",
ROUND(AVG(gda.compound),2) as "Average Compound"
FROM main_product_info mpi
LEFT JOIN brand_product_info bpi USING(product_id)
LEFT JOIN brand_general_info br USING(brand_url)
LEFT JOIN gdas_reviews_info_by_product gda USING(product_link)
WHERE br.Brand LIKE "%cadbury%";

-- Query 36 - Getting the review for a given product
SELECT 
mpi.product_name,
gda.customer_reviews
FROM main_product_info mpi
LEFT JOIN gdas_reviews_info_by_product gda USING(product_link)
WHERE mpi.product_name LIKE "%Tesco Finest Belgian Chocolate Yule Log%";

-- Query 36 - Getting the top 10 products by customer rating
SELECT 
mpi.product_name,
gda.customer_rating
FROM main_product_info mpi
LEFT JOIN gdas_reviews_info_by_product gda USING(product_link)
WHERE gda.customer_rating IS NOT NULL AND gda.customer_rating != "No ratings given yet" AND gda.customer_rating <= "5.0"
ORDER BY gda.customer_rating DESC
LIMIT 10;

-- Query 37 - Getting the top 10 products by worst compound
SELECT 
mpi.product_name,
gda.compound
FROM main_product_info mpi
LEFT JOIN gdas_reviews_info_by_product gda USING(product_link)
WHERE gda.customer_reviews != "No reviews given yet"
ORDER BY gda.compound ASC
LIMIT 10;

-- Query 38 - Getting the links for both the actual product and the image
SELECT 
product_name,
product_link,
Image
FROM main_product_info
WHERE product_name LIKE "%Tesco Disney Mickey & Minnie Drink Dispenser%"; 

-- Query 39 - Price & Saturates comparison for a given category (would need to order that by Price in Pandas)
SELECT 
mpi.product_name,
mpi.Category,
gda.Saturates,
mpi.Price
FROM main_product_info mpi
LEFT JOIN gdas_reviews_info_by_product gda USING(product_link)
WHERE gda.Saturates != "No info available" AND gda.Saturates != "kcal" AND mpi.Price != "No price info for this product"
AND mpi.Category LIKE "%fresh%"
ORDER BY gda.Saturates DESC;

-- Query 40 - Relationship between number of products in promotion vs. not and their average gdas 
SELECT 
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
WHERE Brand LIKE "%finest%"; 

-- Query 41 - Same as 40 but showing categories and one brand per row
SELECT 
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
WHERE Category LIKE "%fresh%"
GROUP BY Brand
ORDER BY ROUND(AVG(CASE WHEN mpi.Promotion != 'No promotion' THEN gda.Saturates ELSE NULL END),2) DESC; 

-- Query 42 - Same as 41 but showing a row per category
use final_project_ironhack;
SELECT 
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
ORDER BY ROUND(AVG(CASE WHEN mpi.Promotion != 'No promotion' THEN gda.Saturates ELSE NULL END),2) DESC;

-- Query 43: Using postcodes

SELECT 
mpi.product_name,
mpi.Category,
uk.Postcode
FROM main_product_info mpi
LEFT JOIN uk_postcode_by_product_manufacturer uk USING(product_link)
WHERE uk.Postcode != "No manufacturer address for this product"
ORDER BY mpi.Category DESC;



