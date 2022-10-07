def main():
    current_user = (login(users1))
    while current_user == 1:
        current_user = (login(users1))

    state = nya_menu_functions(select_menu(), current_user)
    while state != 3:
        state = nya_menu_functions(select_menu(), current_user)
    main()


def login(list):
    print_available_users(list)
    user = input("Användare: ")
    if user == "3":
        exit("User quit")

    if user in list:
        if input("Lösenord: ") == list[user]:
            print("Lösenord korrekt")
            return user
        print("Lösenord inkorrekt")
        return 1
    print("Användare finns inte")
    return 1


def print_available_users(list):
    print("Skriv in användare eller 3 för att avsluta.")
    print_function_users(list)


def select_menu():
    nya_menyn_ordlista()
    user_input = input("Val: ")
    while not validate_input_is_integer(user_input, 3):
        user_input = input("Val: ")
    return int(user_input)


def nya_menyn_ordlista():
    print()
    print("    Meny")
    print_function(options)
    print()


def nya_menu_functions(choice, user):
    current_list = set_current_list(user)

    if choice == 2:
        print_user_och_data(user)
        return current_list
    if choice == 1:
        mata_in_strings(hantera_input_till_string(), current_list)
        return current_list
    if choice == 3:
        return 3


def hantera_input_till_string():
    user_input = input("Skriv in antal strängar: ")
    while not validate_input_is_integer(user_input, 5):
        user_input = input("Skriv in antal strängar: ")
    return int(user_input)


def set_current_list(user):
    if user == "nisse":
        return nisses
    if user == "bosse":
        return bosses
    if user == "stina":
        return stinas
    return None


def add(prompt, lista):
    string = (input(prompt))
    lista.append(string)
    return string


def view(description, lista):
    print(description)
    print()
    for i in range(len(lista)):
        print(f"    {i+1}) {lista[i]}")


def validate_input_is_integer(string, n):
    if len(string) > 0:
        if string.isnumeric():
            if int(string) in range(1, n + 1, 1):
                return True
            print(f"Endast siffrorna 1 till {n} tillåtna.")
            return
        print("Endast siffror tillåtna.")
        return
    print("Skriv något!")
    return


def mata_in_strings(n, lista):
    new_list= []
    for i in range(n):
        new_list.append(add(f"Lägg till sträng {i+1} av {n}: ", lista))
    view(f"Du har matat in följande {n} strängar", new_list)
    print()


def print_function(lista):
    for key, value in lista.items():
        print(f"    {key}) {value}")


def print_function_users(lista):
    print()
    print("    Användare:")
    for key, value in lista.items():
        print(f"    {key}")
    print()

def print_user_och_data(user):
    if user in data:
        print(f"Data lagrat för {user} {data[user]}")
        return
    print("Användare finns inte")


options = {1: "Add item", 2: "List items", 3: "Log out"}
users1 = {"nisse": "apa", "bosse": "ko", "stina": "t-rex"}
nisses, bosses, stinas = [], [], []
data = {"nisse": nisses, "bosse": bosses, "stina": stinas}
main()
