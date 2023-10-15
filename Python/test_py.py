fruits = ['apple', 'orange', 'lemon', 'ananas']
print(fruits.count('apple'))   #  1
print(fruits.index('orange'))  # 1
# print(fruits.index('potato'))  # завершение с ошибкой
fruits.insert(1, 'strawberry')  # вставка нового значения перед указанным индексом
print(fruits)
last_fruit = fruits.pop() # удаление с одновременным извлечением последнего элемента списка 
print(last_fruit)
print(fruits)
fruit_pozition_pop = fruits.pop(1)  # удаление с одновременным извлечением элемента списка c указанным индексом
print(fruit_pozition_pop)