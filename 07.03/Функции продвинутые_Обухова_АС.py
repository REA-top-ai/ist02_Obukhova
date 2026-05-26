# #Задание
# tables = {
#  1: ['Jiho', False],
#  2: [],
#  3: [],
#  4: [],
#  5: [],
#  6: [],
#  7: [],
# }
# def assign_table(table_number, name, vip_status = False):
#     tables[table_number]['name'] = name
#     tables[table_number]['vip_status'] = vip_status
#     return tables
#
# assign_table(6,'Yoni', False)
# assign_table(4, 'Карла')
# print(tables)
#
#
# #Задание
# def print_order(*order_items):
#     print(order_items)
#
# print_order('Orange Juice', 'Apple Juice', 'Scrambled Eggs', 'Pancakes')


#Задание
# tables = {
#  1: {
#  'name': 'Jiho',
#  'vip_status': False,
#  'order': 'Orange Juice, Apple Juice'
#  },
#  2: {},
#  3: {},
#  4: {},
#  5: {},
#  6: {},
#  7: {},
# }
#
# def assign_and_print_order(table_number, *order_items):
#     tables[table_number]['order'] = order_items
#     for item in order_items:
#         print(item)
#
# assign_table(2, 'Arwa', True)
# assign_and_print_order(2, "Стейк", "Морской окунь", "Бутылка вина")
#
# print(tables)

#Задание
tables = {
 1: {
 'name': 'Chioma',
 'vip_status': False,
 'order': {
 'drinks': 'Orange Juice, Apple Juice',
 'food': 'Pancakes'
 }
 },
 2: {},
 3: {},
 4: {},
 5: {},
 6: {},
 7: {},
}
def assign_food_items(table_num,**order_items):
    order = tables.get(table_num)
    order['order'] = order_items

assign_food_items(2,food='Pancakes, Poached Egg', drinks='Water')
print(tables)