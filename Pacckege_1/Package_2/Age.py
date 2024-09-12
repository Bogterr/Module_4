
def Date_of_Birth():
        global BirthDay, day, month, year

        print("\nКогда тебя явили на свет?")
        day = input("День: ")
        month = input("Месяц: ")
        year = input("Год: ")

        BirthDay = f"{day}.{month}.{year}"
        print(f"Дата таоего рождения: {BirthDay}")
        return BirthDay

BirthDay = ""
day = 0
month = 0
year = 0

Date_of_Birth()

# print(BirthDay)