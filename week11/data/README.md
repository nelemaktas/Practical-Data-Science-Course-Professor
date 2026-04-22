# Donation Data Template

This directory contains sample data for the NGO donation analysis tutorial.

## Files

### `donation_template.csv`
A sample CSV file with 4 months of donation records (January - April 2024).

**Columns:**
- `date`: Donation date (YYYY-MM-DD format)
- `donor_id`: Unique identifier for the donor (numeric ID)
- `amount`: Donation amount in dollars (can be decimal)
- `category`: Either "One-time" or "Recurring"
- `recurring`: "Yes" if part of recurring donation, "No" otherwise

**Sample Data Characteristics:**
- 25 donation records across 13 unique donors
- Mix of one-time and recurring donations
- Amounts range from $25 to $500
- Covers 4 months of data (realistic monthly pattern)

## How to Use

1. **For Learning:** Use `donation_template.csv` directly in the Streamlit tutorial
2. **For Testing:** Upload this file to the Streamlit app to see all features in action
3. **For Your Own NGO:** Use this as a template to format your real donation data

## Creating Your Own Donation File

Use this template structure for your actual CSV file:
```
date,donor_id,amount,category,recurring
YYYY-MM-DD,<number>,<decimal>,<One-time|Recurring>,<Yes|No>
```

**Important Notes:**
- Dates must be in YYYY-MM-DD format
- Amounts must be positive numbers
- Donor IDs should be unique identifiers (can be numbers or text)
- The app will automatically clean duplicates and invalid records

## Expected Results with Template Data

When you use `donation_template.csv` with the Streamlit app, you should see:
- **Total Donated:** ~$2,300
- **Unique Donors:** 13
- **Average Gift:** ~$92
- **Meals Served:** ~7,667 (based on $15 = 50 meals conversion)
- **Families Helped:** ~2,556
- **Loyal Donors (2+ gifts):** 4 repeat donors
