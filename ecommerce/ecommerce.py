
import os
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


CSV_PATH = "C:/Users/MSI/Downloads/ecommerce.csv"  
OUT_DIR = Path("outputs/ecommerce_figures")
OUT_DIR.mkdir(parents=True, exist_ok=True)

plt.style.use("ggplot")  


def save_and_show(fig_name, dpi=200):
    out_path = OUT_DIR / fig_name
    plt.tight_layout()
    plt.savefig(out_path, dpi=dpi)
    print("Saved:", out_path)
    plt.show()


if not os.path.exists(CSV_PATH):
    raise FileNotFoundError(f"CSV not found at {CSV_PATH}")

df = pd.read_csv(CSV_PATH)
print("Initial shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 rows:\n", df.head())


if 'originalPrice' in df.columns:
    df = df.drop(columns=['originalPrice'])

df = df.dropna(subset=['price', 'sold', 'tagText', 'productTitle'])


df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)


df['sold'] = pd.to_numeric(df['sold'], errors='coerce').fillna(0).astype(int)


df['tagText_code'], _ = pd.factorize(df['tagText'])


df['title_length'] = df['productTitle'].str.len()
df['word_count'] = df['productTitle'].str.split().apply(len)




plt.figure(figsize=(8,6))
sns.histplot(df['sold'], kde=True, color='skyblue', bins=50)
plt.title('Distribution of Furniture Items Sold')
plt.xlabel('Sold Units')
plt.ylabel('Frequency')
save_and_show("distribution_sold.png")


plt.figure(figsize=(8,6))
sns.histplot(df['price'], kde=True, color='green', bins=50)
plt.title('Distribution of Price')
plt.xlabel('Price')
plt.ylabel('Frequency')
save_and_show("distribution_price.png")


plt.figure(figsize=(8,6))
sns.scatterplot(x='price', y='sold', data=df, color='purple', edgecolor='black')
plt.title('Price vs Sold')
plt.xlabel('Price')
plt.ylabel('Sold Units')
save_and_show("price_vs_sold.png")


top_tags = ['Free shipping', '+Shipping: $5.09']  # you can adjust this list
df['tagText'] = df['tagText'].apply(lambda x: x if x in top_tags else 'Others')

plt.figure(figsize=(8,6))
sns.countplot(x='tagText', data=df, palette='viridis', order=df['tagText'].value_counts().index)
plt.title('Count of TagText Categories')
plt.xlabel('Tag Category')
plt.ylabel('Count')
save_and_show("tagText_counts.png")


plt.figure(figsize=(8,6))
sns.scatterplot(x='title_length', y='sold', data=df, color='red', edgecolor='black')
plt.title('Product Title Length vs Sold Units')
plt.xlabel('Title Length (characters)')
plt.ylabel('Sold Units')
save_and_show("title_length_vs_sold.png")


plt.figure(figsize=(8,6))
sns.scatterplot(x='word_count', y='sold', data=df, color='orange', edgecolor='black')
plt.title('Product Title Word Count vs Sold Units')
plt.xlabel('Word Count')
plt.ylabel('Sold Units')
save_and_show("wordcount_vs_sold.png")


