from pyfiglet import figlet_format

def main():
    # Выводим красивую надпись "romanSecurity"
    print(figlet_format("romanSecurity"))
    
    while True:
        command = input("Введите команду: ")
        if command.lower() == "romanlinux":
            print("Вы запустили RomanLinux!")
        elif command.lower() == "exit":
            print("Выход из программы.")
            break
        else:
            print("Неизвестная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()

