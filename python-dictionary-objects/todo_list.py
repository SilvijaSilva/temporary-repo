from datetime import datetime

todo_items_list = []

while True:
    todo_item_title = input("Enter todo's item: ")
    
    while True:
        todo_item_date = (input("Enter todo's date (YYYY-MM-DD): "))
        try:
            todo_item_date = datetime.strptime(todo_item_date, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

    todo_item = {
        'title': todo_item_title,
        'date': todo_item_date
    }

    todo_items_list.append(todo_item)

    for n in todo_items_list:
        print(f"Work to do: {n['title']}, Date: {n['date']}")
