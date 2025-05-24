person1_name = 'John'
person1_age = 30
person1_city = 'New York'

person2_name = 'Jane'
person2_age = 25
person2_city = 'Los Angeles'

# pavadinimas nesvarbu, galiu rašyti ir "abc"
# objektą identifikuoja laužtiniai skliaustai
# pythone tai yra dictionary (ne object)
# taigi čia yra dictionary to store person information:
my_friend = {
    'name': "jaunius",
    'age': 35,
    'city': "Kaunas"
}

my_friend['age'] = 40
my_friend['name'] = "Martynas"

print("My friend:", my_friend)
print("My friend's name:", my_friend['name'])
print("My friend's age:", my_friend['age'])


# person_information_object = {
#     'name': "jaunius",
#     'age': 35,
#     'city': "Birzai"
# }

# person_information_object['age'] = 36
# person_information_object['name'] = "Martynas"

# print("Person information object:", person_information_object)
# print("Person's name:", person_information_object['name'])
# print("Person's city:", person_information_object['city'])



# people = [
#     {
#         'name': 'John',
#         'age': 30,
#         'city': 'New York'
#     },
#     {
#         'name': 'Jane',
#         'age': 25,
#         'city': 'Los Angeles'
#     },
#     {
#         'name': 'Martynas',
#         'age': 40,
#         'city': 'Kaunas'
#     }
# ]