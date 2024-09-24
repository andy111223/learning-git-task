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
    print(f"I'm going to a {shop.capitalize()} to buy: {formatted_items}")
print(f"In total, I bought {total_products} products")