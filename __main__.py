print("¡Bienvenido a administrador de tareas! Esta aplicación te permitirá organizar y gestionar tus tareas de manera sencilla y eficiente. Podrás agregar nuevas tareas, eliminar las que ya no necesites y marcar como completadas aquellas que hayas finalizado")
print("")


task_list = []

counter = 0

selected_option = ""

while selected_option != "quit":
    selected_option = input("tasklist>>> ")
    
    if selected_option == "list":
        for task in task_list:
            print("id: " + str(task["id"]))
            print("name: " + task["name"])
            print("description: " + task["description"])
            print("date: " + task["date"])
            print("is_complete: " + str(task["is_complete"]))
            print() 
    elif selected_option == "add":
        counter += 1
        task_id = counter 
        task_name = input("enter task name: ")
        task_description = input("enter a description: ")
        task_date = input("enter a date (day/month/year): ")
        is_task_complete = False
        task ={"id":task_id,"name":task_name,"description":task_description,"date":task_date,"is_complete":is_task_complete}
        task_list.append(task)
        print("new task added")
    elif selected_option == "delete":
        task_delete = int(input("enter task id: "))
        for task in task_list:
            if task["id"] == task_delete:
                task_list.remove(task)
                print("task deleted")
    elif selected_option == "complete":
        task_complete = int(input("enter task id: "))
        for task in task_list:
            if task ["id"] == task_complete:
                task ["is_complete"] = True               
                print("task completed")
            

            

    elif selected_option == "quit":
        print("Quit")
    else:
        print("list: lista todas las tareas creadas")
        print("add: add a new task to the list")
        print("delete: delete a task from the list")
        print("complete: complete a task from the list")
        print("quit: quit from tasklist")
        print("help: show help")
