"""
Control the flow of the project
"""
import models
from users import add_user, show_all_users, search_for_user
import sys
sys.path.insert(0, './')
import settings
from pick import pick


FUNCTIONS_LIST = [add_user, show_all_users, search_for_user]

def choose_function():
    """
    Determine action to be performed by the user
    """
    title = "Choose a function or Press CTRL+C to quit: "
    options = FUNCTIONS_LIST
    return pick(options, title)

def choose_repeat():
    """
    Determine whether the user would like to perform another action
    """
    title = "Would you like to enter another function?"
    options = ['yes', 'no']
    return pick(title, options)

def main():
    """
    Control the flow of the database management
    """
    try: 
        with models.session_scope() as session:
            repeat = True
            while repeat:
                selection, index = choose_function()
                print(f"You chose {selection}, choice #{index}")           
                selection(session)
                input("Press Enter to continue or CTRL+C to quit") 
    except KeyboardInterrupt:
        print("Quit")

if __name__=="__main__":
    main()
