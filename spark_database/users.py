"""
Manage user information
"""
import models
from pick import pick

def user_input():
    """
    Create new accounts from dashboard inputs
    """
    correct = 'no'
    while correct == 'no':
        first_name = input ("First Name: ")
        last_name = input ("Last Name: ")
        email = input ("Email: ")
        phone = input ("Phone: ")
        unit = input ("Unit: ")
        section = input ("Section: ")
        rfid = input ("RFID: ")

        check =  (f"first_name: {first_name}, last_name: {last_name}, email: {email}, phone: {phone}, unit: {unit}, section: {section}, rfid: {rfid}")
        title = f"{check}\n Are these values correct?"
        options = ['yes', 'no']
        correct, index = pick(options, title)

    user_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'unit': unit,
        'section': section,
        'rfid': rfid
    }
    return user_data

def add_user(session):
    user_data = user_input()
    session.add(models.User(**user_data))

def show_all_users(session):
    all_users = session.query(models.User).all()
    for user in all_users:
        print(f"first_name: {user.first_name}, last_name: {user.last_name}, email: {user.email}, phone: {user.phone}, unit: {user.unit}, section: {user.section}, rfid: {user.rfid}, date joined: {user.date_joined}")

def search_for_user(session):
    search_first_name = input("What is the user's first name? ")
    search_last_name = input("What is the user's last name? ")
    user_search = session.query(models.User).filter(models.User.first_name.like(f"%{search_first_name}%"), models.User.last_name.like(f"%{search_last_name}%"))
    
    for user in user_search:
        print(f"first_name: {user.first_name}, last_name: {user.last_name}, email: {user.email}, phone: {user.phone}, unit: {user.unit}, section: {user.section}, rfid: {user.rfid}")
