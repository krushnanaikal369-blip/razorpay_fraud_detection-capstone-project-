import pandas as pd
#load the dataset
df = pd.read_csv("transactions_raw.csv")
#no of rows and columns
df.shape

# find no of duplicate rows
duplicate_rows = df[df.duplicated()]
duplicate_rows.shape[0]
# removing duplicate rows
df = df.drop_duplicates()
df.shape

# calculate the percentage of missing values in each column
missing_values = df.isnull().sum()
missing_percentage = (missing_values / len(df)) * 100

# find no of rows with amount less than < 1 or > 1000000
negative_amount_rows = df[df['amount'] < 1 | df['amount'] > 1000000]
print(negative_amount_rows.shape[0])
 
 #finding distinct value from merchant_category and city
distinct_merchant_categories = df['merchant_category'].nunique()
distinct_cities = df['city'].nunique()
print(distinct_merchant_categories)
print(distinct_cities)


def clean_transactions(df):
    # Remove duplicate rows
    df = df.drop_duplicates()

    # Strip surrounding spaces and convert to title case for string columns
    df['merchant_category'] = df['merchant_category'].str.strip().str.title()
    df['city'] = df['city'].str.strip().str.title()

    #drop rows where amount is missing 
    df = df.dropna(subset=['amount_inr'])

    #drop rows where amount_inr is less than one and greater than 1000000
    df = df[(df['amount_inr'] > 0) & (df['amount_inr'] <= 1000000)]

    # Remove rows with missing values in 'amount' and 'distance_from_home_km'
    df = df.dropna(subset=['amount', 'distance_from_home_km'])

#reset the index of the DataFrame after cleaning
    df = df.reset_index(drop=True)


