import os

TASKS_FILE = "tasks.txt"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]


def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")


def main():
    tasks = load_tasks()
    while True:
        print(
            "\nМеню:\n1. Показать все задачи\n2. Добавить задачу\n3. Удалить задачу\n4. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            new_task = input("Введите новую задачу: ")
            tasks.append(new_task)
            save_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            try:
                index = int(input("Введите номер задачи для удаления: ")) - 1
                if 0 <= index < len(tasks):
                    del tasks[index]
                    save_tasks(tasks)
                else:
                    print("Некорректный номер задачи.")
            except ValueError:
                print("Введите число.")
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
