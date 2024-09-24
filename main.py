# Zadanie moduł 3.2

shoppingList = {
    "grocery store":['eggs','tomato','butter'],
    "convenience store":['newspaper','Coca Cola','chewing gum'],
    "pet store":['catfood','dogfood','birdfood']
    }
total_products = 0

for shop, items in shoppingList.items():
    capitalized_items = [item.capitalize() for item in items]
    total_products += len(items)
    formatted_items = ', '.join(capitalized_items) 
    print(f"Idę do {shop.capitalize()} i kupuję tam {formatted_items}")
print(f"W sumie kupuję {total_products} produktów")