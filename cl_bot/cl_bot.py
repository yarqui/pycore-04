def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args: list, contacts: dict):
    name, phone = args
    name = name.lower()
    contacts[name] = phone
    return 'Contact added.'

def change_contact(args: list, contacts: dict):
    name, phone = args

    if name not in contacts:
        return 'No contact with such name'
    
    contacts.update({name: phone})
    return 'Contact updated'
        

def show_phone(args: list, contacts: dict):
    [name] = args
    phone = contacts.get(name)

    if not phone:
        return 'No contact with such name'
    
    return phone 

def show_all(contacts: dict):
    return [{name: phone} for name, phone in contacts.items()]

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match(command):
            case "close" | "exit":
                print('Good bye!')
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "all":
                print(show_all(contacts))
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()