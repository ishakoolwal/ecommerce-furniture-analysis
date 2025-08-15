# 🪑 E-commerce Furniture Data Analysis

## 📌 Project Overview
This project analyzes an **E-commerce furniture dataset** containing product details, prices, shipping information, and sales figures.  
The goal is to:
- Explore sales patterns
- Visualize trends
- Identify factors influencing sales
- Prepare features for predictive modeling

---

## 📊 Dataset Overview
**Rows:** 2,000 furniture products  
**Columns:**
- `productTitle` – Name or description of the product  
- `price` – Current selling price of the item  
- `sold` – Number of units sold  
- `tagText` – Shipping or promotional tags (e.g., "Free shipping")  
- `originalPrice` *(optional)* – Original price before discounts  

---

## 🛠 Tools & Technologies
- **Python** – Data analysis & preprocessing
- **Pandas** – Data cleaning
- **Matplotlib / Seaborn** – Data visualization
- **Scikit-learn** – Predictive modeling
- **SQL** – Querying data
- **Excel** – Preliminary exploration

---

## 📈 Analysis Performed
1. **Data Cleaning & Preprocessing**
   - Removed missing critical values
   - Converted `price` and `sold` to numeric
   - Encoded `tagText` values, grouping rare ones into "Others"
   - Added text-based features (title length, word count)

2. **Exploratory Data Analysis (EDA)**
   - Distribution of items sold
   - Distribution of price
   - Price vs Sold scatter plot
   - Count of `tagText` categories
   - Title length vs Sold units

3. **Feature Engineering**
   - Discount percentage calculation
   - Text encoding with TF-IDF for product titles
   - Tag encoding with Label Encoding

4. **Predictive Modeling**
   - Linear Regression
   - Random Forest Regression
   - Model evaluation using MSE & R²

---

## 📷 Key Insights
- "Free shipping" dominates product listings
- Price is not the only driver of sales; product demand and quality also matter
- Text features such as title length and word count provide additional predictive signals

---


