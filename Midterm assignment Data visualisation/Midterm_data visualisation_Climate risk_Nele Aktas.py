# Databricks notebook source
# MAGIC %md
# MAGIC Depart from ND-GAIN Dataset from the Notre Dame Global Adaptation Initiative
# MAGIC

# COMMAND ----------

# Content: climate vulnerability and readiness scores for 180 countries between 1995-2023 according to Notre Dame Global Adaptation Initiative methodology, compound indices with separate indicators available.
# Source: https://gain.nd.edu/our-work/country-index/download-data/

# COMMAND ----------

# DBTITLE 1,Import data
import pandas as pd
ready_raw = pd.read_csv('/Workspace/Users/nelemaktas@gmail.com/Midterm assignment Nele Aktas/readiness.csv')
vuln_raw = pd.read_csv('/Workspace/Users/nelemaktas@gmail.com/Midterm assignment Nele Aktas/vulnerability.csv')
ready_raw.head()

# COMMAND ----------

# DBTITLE 1,Explore Data
vuln_raw.head()

# COMMAND ----------

# DBTITLE 1,Explore Readiness Index
print(f"No. countries in readiness index: {ready_raw['ISO3'].nunique()}")
print(f"No. countries in vulnerability index: {vuln_raw['ISO3'].nunique()}")

# COMMAND ----------

# DBTITLE 1,Create working dataset
# For each dataset, restrict to 2023, rename columns
vuln_2023 = vuln_raw[['ISO3','Name','2023']]
vuln_2023 = vuln_2023.rename(columns={'2023': 'vulnerability_score'})
vuln_2023.head()

ready_2023 = ready_raw[['ISO3','2023']]
ready_2023 = ready_2023.rename(columns={'2023': 'readiness_score'})
ready_2023.head()

# COMMAND ----------

# DBTITLE 1,Drop null values
ready_2023 = ready_2023.dropna(subset=['readiness_score'])
vuln_2023 = vuln_2023.dropna(subset=['vulnerability_score'])

ready_2023[ready_2023['readiness_score'].isna()]
#vuln_2023[vuln_2023['vulnerability_score'].isna()]

# COMMAND ----------

# DBTITLE 1,Basic stats READINESS
ready_2023['readiness_score'].describe()

# COMMAND ----------

# DBTITLE 1,Basic stats VULNERABILITY
vuln_2023['vulnerability_score'].describe()

# COMMAND ----------

# DBTITLE 1,Merge both datasets into one
merged_2023 = ready_2023.merge(vuln_2023, on='ISO3', how='inner')
merged_2023 = merged_2023[['ISO3', 'Name', 'vulnerability_score','readiness_score']]
print(f"{merged_2023.head()}")
print(f"{merged_2023.shape}")

# COMMAND ----------

# DBTITLE 1,Explore scatter plot
import plotly.express as px

fig = px.scatter(
    merged_2023,
    x='vulnerability_score',
    y='readiness_score',
    size='vulnerability_score',
    color='readiness_score',
    hover_name='Name',
    title='Climate risk: Vulnerability vs Readiness (2023)'
)
fig.show()

# COMMAND ----------

# DBTITLE 1,Explore top and flop countries READINESS
ready_2023_sorted = ready_2023.sort_values('readiness_score',ascending=False)
ready_2023_sorted

# COMMAND ----------

# DBTITLE 1,Explore top and flop countries VULNERABILITY
vuln_2023_sorted = vuln_2023.sort_values('vulnerability_score',ascending=False)
vuln_2023_sorted

# COMMAND ----------

# MAGIC %md
# MAGIC Include income group classification dataset

# COMMAND ----------

# DBTITLE 1,Infos on dataset
## Content: World Bank classification of countries into income groups using GNI per capita and Atlas method. Published yearly on 1st July.
## Classification:
#   L (Low income) <= 1,145LM (Lower middle income) 1,146 - 4,515
#   UM (Upper middle income) 4,516 - 14,005
#   H (High income) > 14,005
# Source: https://datahelpdesk.worldbank.org/knowledgebase/articles/906519-world-bank-country-and-lending-groups

# COMMAND ----------

# Using AI for debugging, I found out that I needed openpyxl in order to work with an excel file (xlsx)
%pip install openpyxl

# COMMAND ----------

# DBTITLE 1,Import dataset
# Import dataset
income_raw = pd.read_excel('/Workspace/Users/nelemaktas@gmail.com/Midterm assignment Nele Aktas/Country income groups World Bank edited.xlsx')
income_raw.head()

# COMMAND ----------

# DBTITLE 1,Prepare for merge
# Bring to similar format as dataset on climate risk
income = income_raw[['Country Code',2023]]
income = income.rename(columns={'Country Code':'ISO3',2023:'Income group'})
income = income.dropna(subset="Income group")
print(f"{income.head()}")
print(f"{income.shape}")

# COMMAND ----------

# DBTITLE 1,Merge with current dataset
merged_2023_income = merged_2023.merge(income, on='ISO3', how='inner')
merged_2023_income.head()

# COMMAND ----------

# DBTITLE 1,Explore scatter plot
fig = px.scatter(
    merged_2023,
    x='vulnerability_score',
    y='readiness_score',
    size='vulnerability_score',
    color='readiness_score',
    hover_name='Name',
    title='Climate risk: Vulnerability vs Readiness (2023)'
)
fig.show()

# COMMAND ----------

# MAGIC %md
# MAGIC Include GDP data

# COMMAND ----------

## Content: GDP in current prices (dollar)
## Source: https://data.worldbank.org/indicator/NY.GDP.MKTP.CD
# First 4 rows are metadata

# COMMAND ----------

# DBTITLE 1,Import dataset
gdp_raw = pd.read_csv('/Workspace/Users/nelemaktas@gmail.com/Midterm assignment Nele Aktas/GDP data number format edited new.csv')
gdp_raw.head()

# COMMAND ----------

# DBTITLE 1,Prepare for merge
# Reduce to relevant columns, drop rows with missing values, rename columns in accord with dataset on climate risk
gdp = gdp_raw[['Country Code','2023']]
gdp = gdp.rename(columns={'Country Code':'ISO3', '2023':'GDP'})
gdp = gdp.dropna(subset="GDP")
print(gdp.head())
print(gdp.shape)
print(gdp['ISO3'].unique())

# COMMAND ----------

# DBTITLE 1,Merge with Climate risk dataset
merged_2023_income_gdp = merged_2023_income.merge(gdp, on='ISO3', how='inner')
merged_2023_income_gdp.head()

# COMMAND ----------

# DBTITLE 1,Explore structure
merged_2023_income_gdp.columns

# COMMAND ----------

# DBTITLE 1,Change income group labels
# Change names of income groups for better comprehension
merged_2023_income_gdp['Income group'] = merged_2023_income_gdp['Income group'].replace({
    'L': 'Low income',
    'LM': 'Lower-middle income',
    'UM': 'Upper-middle income',
    'H': 'High income'
})

# COMMAND ----------

# DBTITLE 1,Update plot
# Update scatter plot with GDP as scatter size
fig1 = px.scatter(
    merged_2023_income_gdp,
    x='vulnerability_score',
    y='readiness_score',
    size='GDP',
    title='The most vulnerable countries are the least able to cope with climate change',
    labels={
        'vulnerability_score': 'Vulnerability Score',
        'readiness_score': 'Readiness Score'},
    category_orders={
        'Income group': ['Low income', 'Lower-middle income', 'Upper-middle income', 'High income']},
    color='Income group',
    color_discrete_map={
        'Low income': '#e74c3c','Lower-middle income': '#f39c12','Upper-middle income': '#f1c40f','High income': '#27ae60'},
    template='plotly_white', # for better data-ink-ratio
    hover_name='Name',
    size_max=90)
fig1.show()

# COMMAND ----------

# DBTITLE 1,Update labels to plot
# Label intersting countries (identified by looking at the plot and using the table of the climate risk index)

fig2 = px.scatter(
    merged_2023_income_gdp,
    x='vulnerability_score',
    y='readiness_score',
    size='GDP',
    title='The countries most vulnerable to climate change are the least able to cope with it',
    labels={
        'vulnerability_score': 'Vulnerability Score',
        'readiness_score': 'Readiness Score'},
    category_orders={
        'Income group': ['Low income', 'Lower-middle income', 'Upper-middle income', 'High income']},
    color='Income group',
    color_discrete_map={
        'Low income': '#e74c3c','Lower-middle income': '#f39c12','Upper-middle income': '#f1c40f','High income': '#27ae60'},
    template='plotly_white', # for better data-ink-ratio
    opacity=0.5, # for better visibility
    hover_name='Name',
    size_max=90)

interesting_countries = ['Norway', 'Chad', 'Singapore', 'Switzerland','Rwanda','Kyrgyzstan','Turkmenistan','Somalia']

for country in interesting_countries:
    point = merged_2023_income_gdp[merged_2023_income_gdp['Name'] == country].iloc[0]
    fig2.add_annotation(
        x=point['vulnerability_score'],
        y=point['readiness_score'],
        text=country,
        showarrow=True)
    
fig2.show()
