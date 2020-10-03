def open_file(file_name):
    with open(file_name) as file:
        lines = file.read().split("\n")
    return lines

def get_cook_book(f_lines):
    #Задача 1
    cook_book = {}
    for i in range(0, len(f_lines)):
        if (i - 1 < 0) or (f_lines[i-1] == ''):
            cook_book[f_lines[i]] = []
            ingr_count = int(f_lines[i+1])
            for j in range(i + 2, i + 2 + ingr_count):
                temp_dict = {}
                temp_list = f_lines[j].split(" | ")
                temp_dict['ingredient_name'] = temp_list[0]
                temp_dict['quantity'] = temp_list[1]
                temp_dict['measure'] = temp_list[2]
                cook_book[f_lines[i]].append(temp_dict)
    return cook_book     

def get_shop_list_by_dishes(dishes, person_count):
    #Задача 2
    file_lines = open_file('recipes.txt')    
    cook_book = get_cook_book(file_lines)
    shop_list = {}
    for i in range(0, len(dishes)):
        #for key in cook_book:
        if dishes[i] in cook_book.keys():
            for ingr in cook_book[dishes[i]]:
                temp_dict = {}
                temp_dict['measure'] = ingr['measure']
                if ingr['ingredient_name'] not in shop_list.keys():
                    shop_list[ingr['ingredient_name']] = {}                    
                    temp_dict['quantity'] = int(ingr['quantity']) * person_count
                else:
                    temp_dict['quantity'] = shop_list[ingr['ingredient_name']]['quantity'] + int(ingr['quantity']) * person_count
                shop_list[ingr['ingredient_name']] = temp_dict
    return shop_list

def main():
    file_lines = open_file('recipes.txt')
    print(f'Cook book:\n{get_cook_book(file_lines)}\n')
    print(f"Shop list:\n{get_shop_list_by_dishes(['Фахитос', 'Омлет', 'Запеченный картофель'], 3)}")               

main()
