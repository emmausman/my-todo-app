import streamlit as st
# to run - go to terminal and type 'streamlit run web_app.py'
# once the local host is open, you can modify the program and just hit refresh in the browser
import functions

# then pip freeze > requirements.txt
# the requirements.txt file has all the packages the app needs to install
# pip freeze shows you the list.  > filename puts it in a file
# make sure Git is the VCS
# commit files to github; go to github and create a repository
# get the url, return to pycharm, goto manage remotes (under VCS)
# enter url


def add_todo():
    todo = st.session_state["new_todo"].capitalize() +'\n'
    todos.append(todo)
    functions.save_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")
# Note: order is important

#st.checkbox("Buy groceries")
#st.checkbox("Throw out the trash")

todos = functions.get_todos()

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.save_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

# st.text_input(label="Enter a 'to do' item: ")  #--> label above box
st.text_input(label="", placeholder='Add new todo ...', on_change=add_todo, key='new_todo')

st.session_state        # This shows the session_states at the bottom of the web page
# helpful for debugging
