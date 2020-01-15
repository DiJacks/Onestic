import pandas as pd

customers = pd.read_csv('customers.csv')
orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')


#TASK1
ids = []
prices = []

for index, row in orders.iterrows():
  ids.append(row['id'])
  price = 0
  for p in row['products'].split():
    price += products.loc[int(p)]['cost']
  prices.append(price)

order_prices = pd.DataFrame({
  'id':ids,
  'euros':prices
})
order_prices.to_csv('order_prices.csv', index=False)


#TASK 2
ids=[]
customers_products = [[] for i in range(len(products))]

for index, row in orders.iterrows():
  for p in row['products'].split():
    customers_products[int(p)].append(row['id'])

for i in range(len(customers_products)):
  ids.append(products.loc[i]['id'])
  #Eliminate duplicates
  customers_products[i] = list(dict.fromkeys(customers_products[i]))
  #Get a space-separated string
  customers_products[i] = " ".join(str(item) for item in customers_products[i]) 

product_customers = pd.DataFrame({
  'id':ids,
  'customer_ids':customers_products
})
product_customers.to_csv('product_customers.csv', index=False)


#TASK 3
euros = [0 for i in range(len(customers))]
for index, row in orders.iterrows():
  euros[row['customer']] += order_prices.loc[row['id']]['euros']

customer_ranking = customers
customer_ranking['total_euros'] = euros
customer_ranking = customer_ranking.sort_values(by=['total_euros','id'],ascending=[False,True])

customer_ranking.to_csv('customer_ranking.csv', index=False)

