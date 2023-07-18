print("¡Bienvenido a administrador de tareas! Esta aplicación te permitirá organizar y gestionar tus tareas de manera sencilla y eficiente. Podrás agregar nuevas tareas, eliminar las que ya no necesites y marcar como completadas aquellas que hayas finalizado")
print("")
selected_option = ""
while selected_option != "quit":
    selected_option = input("tasklist>>> ")
    if selected_option == "list":
        print("List")
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
