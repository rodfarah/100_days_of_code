tasks = []


def add_task(task: str):
    tasks.append(task)


def delete_task(task_idx: int):
    tasks.remove(task_dict[task_idx])


def edit_task(task_idx: int, new_task: str):
    tasks.insert(task_idx-2, new_task)
    tasks.remove(task_dict[task_idx])


def ask_id(any_dict):
    check_process = True
    while check_process:
        task_id = int(input("Type task ID: "))
        if task_id not in any_dict.keys():
            print("No such ID on task dictionary.")
        else:
            check_process = False
            return task_id


def ask_new_task():
    return input("What is the new task? ")


module_is_on = True

while module_is_on:
    task_dict = {idx: task for idx, task in enumerate(tasks, 1)}
    task_dict_len = len(task_dict)
    if task_dict_len == 0:
        print("\nYour task list is empty.")
    else:
        print(f"\nHere are your tasks: {task_dict}")
    action = input("(A)dd, (D)elete or (E)dit? ")
    if action == "A":
        add_task(ask_new_task())
    elif action == "D":
        if task_dict_len == 0:
            print("You can not edit or delete items on an empty task list.")
            continue
        delete_task(ask_id(task_dict))
    elif action == "E":
        if task_dict_len == 0:
            print("You can not edit or delete items on an empty task list.")
            continue
        edit_task(ask_id(task_dict), ask_new_task())
    else:
        print(f"{action} is not an option.")

    if input("Would you like to continue?(Y/N) ") == "N":
        module_is_on = False
