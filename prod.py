import subprocess

def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Ошибка: {str(e)}"

def main():
    print("Добро пожаловать в командный калькулятор!")
    print("Введите математическое выражение или 'выход' для завершения.")

    while True:
        user_input = input("Введите выражение: ")
        
        if user_input.lower() == 'выход':
            print("До свидания!")
            break

        result = calculate(user_input)
        print(f"Результат: {result}\n")
        subprocess.run("start cmd /k", shell=True)

if __name__ == "__main__":
    main()
