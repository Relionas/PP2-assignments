import re
import json

# Read File
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Extract Prices
price_pattern = r'\d+(?: \d+)*,\d{2}'
prices = re.findall(price_pattern, text)

# Remove duplicates
unique_prices = list(dict.fromkeys(prices))

# Extract Product Names
product_pattern = r'\d+\.\n(.+)'
products = re.findall(product_pattern, text)

# Extract Date and Time
date_pattern = r'\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}'
date_match = re.search(date_pattern, text)
date_time = date_match.group() if date_match else None

# Extract Payment Method
payment_pattern = r'Банковская карта'
payment_match = re.search(payment_pattern, text)
payment_method = payment_match.group() if payment_match else None

# Extract Total
total_pattern = r'ИТОГО:\n([\d\s,]+)'
total_match = re.search(total_pattern, text)
total = total_match.group(1).strip() if total_match else None

# Convert Prices to Float
def clean_price(price):
    return float(price.replace(" ", "").replace(",", "."))

numeric_prices = [clean_price(p) for p in unique_prices]

# Calculate Sum
calculated_total = sum(numeric_prices)

# Create Structured Output
data = {
    "date_time": date_time,
    "payment_method": payment_method,
    "total_from_receipt": total,
    "calculated_total": calculated_total,
    "products": products
}

# Write JSON file
with open("receipt.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
