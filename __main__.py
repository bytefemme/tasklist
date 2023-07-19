print("¡Bienvenido a administrador de tareas! Esta aplicación te permitirá organizar y gestionar tus tareas de manera sencilla y eficiente. Podrás agregar nuevas tareas, eliminar las que ya no necesites y marcar como completadas aquellas que hayas finalizado")
print("")

selected_option = ""
while selected_option != "quit":
    selected_option = input("tasklist>>> ")
    if selected_option == "list":
        task1 ={"id":1,"name":"nath","description":"sensual","date":"today","isComplete":False}
        task2 ={"id":2,"name":"mike","description":"sexy","date":"today","isComplete":False}
        task3 ={"id":3,"name":"jose","description":"handsome","date":"today","isComplete":False}
        tasks = [task1, task2, task3]
        for task in tasks:
            print("id: " + str(task["id"]))
            print("name: " + task["name"])
            print("description: " + task["description"])
            print("date: " + task["date"])
            print("isComplete: " + str(task["isComplete"]))
            print()

    elif selected_option == "add":
        print("Add")
    elif selected_option == "delete":
        print("Delete")
    elif selected_option == "complete":
        print("Complete")
    elif selected_option == "quit":
        print("Quit")
    else:
        print("list: lista todas las tareas creadas")
        print("add: add a new task to the list")
        print("delete: delete a task from the list")
        print("complete: complete a task from the list")
        print("quit: quit from tasklist")
        print("help: show help")
