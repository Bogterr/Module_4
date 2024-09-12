# Имя
def Name_():
      global name
      print("\n"
            "Как тебя зовут?")
      name = input("\nОбычно, все зовут меня: ")
      print(f"Приятно познакомиться, {name}!")
      return name

name = ""
Name_()

# print(name)