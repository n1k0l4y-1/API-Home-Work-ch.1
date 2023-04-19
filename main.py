with open('grocery_list.txt', 'rt', encoding = 'utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        dish_count = int(file.readline())
        basket = []
        for _ in range(dish_count):
             ingredient_name, quantity, measure = file.readline().strip().split(' | ')
             basket.append({
                 'ingredient_name': ingredient_name,
                 'quantity': quantity,
                 'measure': measure
             })
        file.readline()
        cook_book[dish_name] = basket


    print(cook_book) # результат первого задания

    def get_shop_list_by_dishes(dishes, person_count):
        dishes_for_person = {}
        for recipe, ingredients in cook_book.items():
            if recipe in dishes:
                for ingredient in ingredients:
                    name = ingredient['ingredient_name']
                    quantity = int(ingredient['quantity']) * person_count
                    measure = ingredient['measure']
                    if name not in dishes_for_person.keys():
                        dishes_for_person[name] ={
                            'measure': measure,
                            'quantity': quantity
                        }
                    else:
                        dishes_for_person[name]['quantity'] += quantity
        return print(dishes_for_person)


    get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2) # результат второго задания