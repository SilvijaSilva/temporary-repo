# person_list = []

# while True:
#     person_name = input("Enter person's name: ")
#     person_age = input("Enter person's age: ")
#     person_city = input("Enter person's city: ")

#     person = {
#         'name': person_name,
#         'age': person_age,
#         'city': person_city
#     }

#     person_list.append(person)

#     for p in person_list:
#         print(f"Name: {p['name']}, Age: {p['age']}, City: {p['city']}")

from datetime import datetime

todo_items_list = []

while True:
    todo_item_title = input("Enter todo's item: ")
    todo_item_date = str(input("Enter todo's date (YYYY-MM-DD): "))

    try:
        todo_item_date = datetime.strptime(todo_item_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        continue

    todo_item = {
        'title': todo_item_title,
        'date': todo_item_date
    }

    todo_items_list.append(todo_item)

    for n in todo_items_list:
        print(f"Title: {n['title']}, Date: {n['date']}")
