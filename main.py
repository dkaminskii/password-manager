import json
import time

try:
    with open(r"D:\PR\P\password_manager\passwords_list.json", "r", encoding="utf-8") as f:
        dictionary_table = json.load(f)
except:
    dictionary_table = []

master_password = 363
def password_check():
    x = int(input("Enter your password: "))
    if x == master_password:
        return True
    else:
        return False

def adding_passwords():
    passwords_set = {
        "website" : input("Enter the name of the website: "),
        "password" : input("Enter the password for website: ")
    }
    dictionary_table.append(passwords_set)
    with open(r"D:\PR\P\password_manager\passwords_list.json", "w", encoding="utf-8") as file_json:
        json.dump(dictionary_table, file_json, ensure_ascii=False, indent=4)

def display_passwords_list():
    if not dictionary_table:
        print("No passwords")
        return

    for i, x in enumerate(dictionary_table, start=1):
        print(f"{i}. [{x['website']}] {x['password']}")

if __name__ == '__main__':
    if password_check():
        while True:
            choice = input("Select options: \n 1 - add password \n 2 - display password list \n 3 - turn off the program \n ---------> ")
            match choice:
                case'1':
                    adding_passwords()
                case'2':
                    display_passwords_list()
                case'3':
                    time.sleep(2)
                    print("Program was turned off")
                    break