from db_config import User


def main():
    print("===== Welcome to CRM Application =====")
    print("[S]how: Show all users info")
    print("[A]dd: Add new user")
    print("[Q]uit: Quit The Application")
    print("======================================")

    selected_command = ""

    while selected_command != "Q":
        print()
        selected_command = input("Your command > ")

        if selected_command == "S":
            for usr in User.select():
                print(f"Name: {usr.user} Age: {usr.age}")

        elif selected_command == "A":
            user_name = input("New user name > ")
            user_age = input("New user age > ")
            user_data = User(user=user_name, age=user_age)
            user_data.save()
            print(f"Add new user: {user_name}")

        elif selected_command == "Q":
            break

        else:
            print(f"{selected_command}: command not found")

    print("Bye!")


if __name__ == "__main__":
    main()
