from src.models.address_book import AddressBook
from src.services.console_text_designer import ConsoleTextDesigner
from src.services.validator import validate_user_name, validate_phone_number
import pickle


class App:
    def __init__(self):
        # TODO init properties ???
        pass

    def run(self):
        book = load_data("addressbook.pkl") or AddressBook()
        notebook = load_data("notebook.pkl") or Notebook() # Class will be added with note task
         
        console_text_designer = ConsoleTextDesigner()

        console_text_designer.print_info("Welcome to the assistant bot!")

        while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)
            output = ''

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")

            elif command == "add":
                person = fill_new()

                print("Need to do.")
            # elif command == "change":
            #     print("Need to do.")
            # elif command == "phone":
            #     print("Need to do.")
            # elif command == "all":
            #     print("Need to do.")
            # elif command == "add-birthday":
            #     print("Need to do.")
            # elif command == "show-birthday":
            #     print("Need to do.")
            # elif command == "birthdays":
            #     print("Need to do.")
            else:
                print("Invalid command.")

            print(output)

        # TODO: save_data(book)
        save_data(book, "addressbook.pkl")
        save_data(notebook, "notebook.pkl") # variable will be added with note task


def fill_new():  # TODO: move to separate method
    properties = ["name", "phone_number"]

    name = None
    phone_number = None

    while True:
        if len(properties) == 0:
            break

        prop = properties[0]

        if prop == "name":
            input_name = input("print name: ")
            if not validate_user_name(input_name):  # is not valid
                print("name is not valid")
                continue
            name = input_name

        if prop == "phone_number":
            input_phone = input("print phone: ")
            if not validate_phone_number(input_phone):
                print("phone is not valid")
                continue
            phone_number = input_phone

        properties.pop(0)

    print('__________')
    print(name, phone_number)
    print('__________')


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def save_data(data, filename):
    with open(filename, "wb", encoding="utf-8") as f:
        return pickle.dump(data, f)
    

def load_data(filename):
    try:
        with open(filename, "rb", encoding="utf-8") as f:
            pickle.load(f)
    except FileNotFoundError:
        return None

