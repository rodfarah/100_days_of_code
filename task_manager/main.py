tasks = []


def task_num_checker(any_func):
    """Decorator, check if task number exists inside task dictionary"""
    def wrapper_func():
        global task_dict
        check_process = True
        while check_process:
            chosen_idx = any_func()
            if chosen_idx not in task_dict.keys():
                print("No such ID on task dictionary.")
            else:
                check_process = False
                return chosen_idx
    return wrapper_func


def add_task(task: str):
    """ Add a task to task list"""
    tasks.append(task)
    return "Task added successfully."

def delete_task(task_idx: int):
    """Given an index number (key), delete task (value) from task dictionary"""
    tasks.remove(task_dict[task_idx])


def edit_task(task_number: int, new_task: str):
    """Given a task number (key), edit the corresponding task (value) inside task dictionary"""
    tasks.insert(task_number-1, new_task)
    tasks.remove(task_dict[task_number])


@task_num_checker
def ask_task_num() -> int:
    """Ask user for a task number (key inside tasks dictionary)"""
    while True:
        try:
            return int(input("Type task ID: "))
        except:
            print("Please, enter valid digit(s).")



def ask_new_task() -> str:
    """ Ask user for a new task"""
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
        delete_task(ask_task_num())
    elif action == "E":
        if task_dict_len == 0:
            print("You can not edit or delete items on an empty task list.")
            continue
        edit_task(ask_task_num(), ask_new_task())
    else:
        print(f'"{action}" is not an option.')

    while True:
        keep_going = input("Would you like to continue?(Y/N) ")
        if keep_going == "N":
            module_is_on = False
            break
        elif keep_going == "Y":
            break
        else:
            print("Please, enter Y or N: ")
