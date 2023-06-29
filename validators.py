def check_num(num, from_n, to_n) -> bool:
    if num == "":
        return False
    else:
        if str(num).isdigit():
            if (int(num) >= from_n and int(num) <= to_n):
                return True
            else:
                return False
        else: 
            return  False    


def check_password_len(password_len) -> bool:
    return check_num(password_len, 10, 150)

def check_num_of_users(num_of_users) -> bool:
    return check_num(num_of_users, 10, 200)

def email_is_valid(email) -> bool:
    email = str(email)

    if(email == ""): return False
    else:
        if(email.find("@") != -1):
            if((len(email.split("@")[1]) > 3) and email.split("@")[1].find(".") != -1):
                return True
            else:
                return False
        else:
            return False

def name_is_valid(name) -> bool:
    name = str(name)

    if(name.isalpha()):
        if(len(name) > 2):
            return True
        else: 
            return False
    else:
        return False