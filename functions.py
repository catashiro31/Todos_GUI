def get_todos(filepath='todos.txt'):
    """
    Get filepath and return to-do list
    :param filepath: path to Zip_GUI
    :return: to-do list
    """
    with open(filepath,'r') as file:
        todos_arg = file.readlines()
    return todos_arg

def write_todo(todos_arg,filepath='todos.txt'):
    """
    Get to-do list and filepath --> Write in Zip_GUI
    :param todos_arg: to-do list
    :param filepath: path to Zip_GUI
    """
    with open(filepath,'w') as file:
        file.writelines(todos_arg)