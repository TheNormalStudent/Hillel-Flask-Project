from flask import Flask, request
from datetime import datetime
from utils import generate_password as gp, read_file, generate_fake_user, read_csv, space, database_connect_execute_set
from validators import check_password_len, check_num_of_users, name_is_valid, email_is_valid, phone_is_valid


app = Flask(__name__)

@app.route('/hello/')
def hello_world():
    return "Hello world!"

@app.route('/generate-password/')
def generate_password():
    password_len = str(request.args.get('password-len'))
    print('password_len', password_len)


    if not check_password_len(password_len):
        return  "Invalid parametr \"password-len\". Should be int from 10 to 100\n"
    else: pass

    password = gp(int(password_len))

    return f"Your new password: {password}\n"

@app.route('/requirements/')
def get_requirements():
    return read_file()

@app.route('/generate-users/')
def get_users():
    num_of_users = str(request.args.get('num-of-users'))
    print ('num-of-users', num_of_users)

    if not check_num_of_users(num_of_users):
        return  "Invalid parametr \"num-of-users\". Should be int from 10 to 200\n"
    else: pass


    return generate_fake_user(num_of_users)

@app.route('/mean/')
def mean():
    cm, kg = read_csv()
    res_str = "Average height: " + cm + "\n" + "Average weight: "+ kg + "\n"
    return res_str

@app.route('/space/')
def space_get():
    return "Amount of austronauts in the SPACE: " + str(space()) + " \n"

@app.route('/emails/create/')
def create_email():
    contact_name = request.args['contactName']
    email_value = request.args['Email']

    if not (email_is_valid(email_value)): 
        return "Not valid email. It should contain @ and chars more than 3 chars after @.\n"

    if not(name_is_valid(contact_name)):
        return "Not valid name. Should be str without digits more than 2 chars.\n"

    sql_query = f'''
    INSERT INTO emails (contactName, emailValue)
    VALUES ('{contact_name}', '{email_value}');
    '''

    database_connect_execute_set(sql_query)

    return 'create_emails'

@app.route('/emails/read/')
def read_email():
    sql_query = f'''
    SELECT * FROM emails
    '''

    result = database_connect_execute_set(sql_query)
    return str(result)

@app.route('/emails/update/')
def update_email():
    contact_name = request.args['contactName']
    email_value = request.args['Email']

    if not (email_is_valid(email_value)): 
        return "Not valid email. It should contain @ and chars more than 3 chars after @.\n"

    if not(name_is_valid(contact_name)):
        return "Not valid name. Should be str without digits more than 2 chars.\n"

    sql_query = f'''
    UPDATE emails
    SET contactName = '{contact_name}'
    WHERE emailValue = '{email_value}';
    '''

    database_connect_execute_set(sql_query)

    return 'update_email'

@app.route('/emails/delete/')
def delete_email():

    sql_query = f'''
    DELETE FROM emails
    '''
    database_connect_execute_set(sql_query)
    return 'delete_email'



@app.route('/phones/create/')
def create_phones():
    contact_name = request.args['contactName']
    phone_value = request.args['Phone']

    if not(name_is_valid(contact_name)):
        return "Not valid name. Should be str without digits more than 2 chars.\n"

    if not(phone_is_valid(phone_value)):
        return "Not valid phone. Should be only digits in number of 10 or 12"

    sql_query = f'''
    INSERT INTO phones (contactName, phoneValue)
    VALUES ('{contact_name}', '{phone_value}');
    '''

    database_connect_execute_set(sql_query)

    return 'create_phones'

@app.route('/phones/read/')
def read_phones():
    sql_query = f'''
    SELECT * FROM phones
    '''

    result = database_connect_execute_set(sql_query)
    return str(result)

@app.route('/phones/update/')
def update_phones():
    contact_name = request.args['contactName']
    phone_value = request.args['Phone']

    if not(name_is_valid(contact_name)):
        return "Not valid name. Should be str without digits more than 2 chars.\n"

    if not(phone_is_valid(phone_value)):
        return "Not valid phone. Should be only digits in number of 10 or 12"

    sql_query = f'''
    UPDATE phones
    SET contactName = '{contact_name}'
    WHERE phoneValue = '{phone_value}';
    '''

    database_connect_execute_set(sql_query)

    return 'update_phones'

@app.route('/phones/delete/')
def delete_phones():

    sql_query = f'''
    DELETE FROM phones
    '''
    database_connect_execute_set(sql_query)
    return 'delete_phones'


if __name__ == '__main__':
    print("git check")
    app.run(host = '0.0.0.0')

#Trying out git pull-requests