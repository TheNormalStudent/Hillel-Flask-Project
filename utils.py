import random
import os
import string
from faker import Faker
from fake_mail import fake_mails
import pandas as pd
import requests
import sqlite3

def generate_password(query_password_length = 10) -> str:
    choices = string.ascii_letters + string.digits + r"""#$%&'()*+,-./:;=?@[\]^_`{|}~"""
    result = ""

    if not str(query_password_length).isdigit():
        raise TypeError("Invalid password length type...")

    query_password_length = int(query_password_length)

    for _ in range(query_password_length):
        result += random.choice(choices)
    return result 

def read_file() -> str:
    result_str = ""

    if not os.path.exists('requirements.txt'):
        return 'File does not exist'    

    with open('requirements.txt') as f:
        lines = f.readlines()

        for element in lines:
            result_str += element

    return result_str
    

def generate_fake_user(query_num_of_users = 100) -> str:
    fake = Faker()
    res_str = ""
    choices = string.ascii_letters + string.digits

    for _ in range(query_num_of_users):
        mail_user = ""
        for _ in range(10):
            mail_user += random.choice(choices)

        mail_user += '@' + random.choice(fake_mails)

        res_str += fake.name() + "\t" + mail_user + '\n'

    return res_str

def read_csv():
    data = pd.read_csv('data.csv')
    average_height_in_cm = (data.mean()[' "Height(Inches)"']) * 2.54
    average_weight_in_kg = (data.mean()[' "Weight(Pounds)"']) * 0.45359237 
    return str(average_height_in_cm), str(average_weight_in_kg)

def space():
    r = requests.get('http://api.open-notify.org/astros.json')


def database_connect_execute_set(sql_query):
    con = sqlite3.connect('example.db')

    cur = con.cursor()
    cur.execute(sql_query)
    res = cur.fetchall()
    con.commit()
    con.close()    
    return res
