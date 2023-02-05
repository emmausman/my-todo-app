def get_todos():
    """ Read a text file and return the list of to-do items"""
    with open('todos.txt', 'r') as localfile:
        localtodos = localfile.readlines()
    return localtodos

def save_todos(todos):
    with open('todos.txt', 'w') as localfile:
        localfile.writelines(todos)