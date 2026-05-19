import csv
import os

input_files = [
    'data/daily_sales_data_0.csv',
    'data/daily_sales_data_1.csv',
    'data/daily_sales_data_2.csv'
]
output_file = 'data/formatted_sales_data.csv'

with open(output_file, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['sales', 'date', 'region'])
    
    for filename in input_files:
        with open(filename, mode='r') as infile:
            reader = csv.reader(infile)
            header = next(reader)
            # Find indices
            product_idx = header.index('product')
            quantity_idx = header.index('quantity')
            price_idx = header.index('price')
            date_idx = header.index('date')
            region_idx = header.index('region')
            
            for row in reader:
                product = row[product_idx]
                if product.lower() == 'pink morsel':
                    price_str = row[price_idx].replace('$', '').strip()
                    price = float(price_str)
                    quantity = int(row[quantity_idx])
                    sales = price * quantity
                    date = row[date_idx]
                    region = row[region_idx]
                    
                    writer.writerow([sales, date, region])

print(f"Data successfully processed and written to {output_file}")
