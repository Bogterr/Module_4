def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

try:
    inner_function()
except:
    print("\n",
          "Ошибка! Функция: 'inner_function()' не может быть вызвана.\n"
          "Log ошибки:\n"
          "NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?")

##################################
print()
test_function()