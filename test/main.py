# temp_list = []

# again = True
# while again:
#     to_do = input("Enter input: ")
#     temp_list.append(to_do)
#     continuee = input("Continue: Y/y")
#     if continuee == "Y" or continuee == "y":
#         continue
#     else:
#         break

# print(temp_list)

to_do = []

while True:
    user_action = input("Type add, show or exit: ").strip()

    match user_action:
        case "add":
            todo = input("Enter a task: ")
            to_do.append(todo)
        case "show":
            for item in to_do:
                print(item)
        case "exit":
            break
        case whatever:
            print("You have entered wrong command!")
            continue

print("Bye!")
