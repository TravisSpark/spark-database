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
    title = "Choose a function: "
    options = FUNCTIONS_LIST
    return pick(options, title)

def choose_repeat():
    """
    Determine whether the user would like to perform another action
    """
    title = "Would you like to enter another function?"
    options = ['yes', 'no']
    return pick(options, title)

def main():
    """
    Control the flow of the database management
    """
    repeat = 'yes'
    while repeat=='yes':
        with models.session_scope() as session:
            selection, index = choose_function()           
            selection(session)
        input("Press Enter to continue...")
        repeat, index = choose_repeat()
    

if __name__=="__main__":
    main()
