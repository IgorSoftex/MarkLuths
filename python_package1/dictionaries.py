#Словари

# pizza = {"class": "Бюджетная", "price": 120}
# print(pizza)
# print(type(pizza))
# # print(pizza["class"])
# pizza["price"] += 1
# pizza["quontity"] = 2
# print(pizza)

pizza = dict()
print(type(pizza))
# print(pizza)
pizza["class"] = "Бюджетная"
pizza["price"] = 100
pizza["toppings"] = ["Сир", "Салямі"]
print(pizza)
# print(pizza["toppings"][0])
for i in pizza["toppings"]:
    print(i)