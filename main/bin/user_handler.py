#This script handles the useer's secret santa and password


def load_users():
    users = {}
    with open('db/users.txt','r') as file:
        for line in file:
            line = line.replace('\n','')
            duple = line.split(':')
            users[duple[0]] = duple[1]
                
                
    return users  

def load_user_pwd():
    users = {}
    with open('db/users_pwd.txt','r') as file:
        for line in file:
            line = line.replace('\n','')
            duple = line.split(':')
            users[duple[0]] = duple[1]
                
                
    return users  
    
def load_user_secret():
    secret = {}
    with open('db/secret_santa.txt','r') as file:
        for line in file:
            line = line.replace('\n','')
            duple = line.split(':')
            secret[duple[0]] = duple[1]
                
                
    return secret    
    

def load_restrictions():
    res = {}
    with open('db/restrictions.txt','r') as file:
        for line in file:
            line = line.replace('\n','')
            duple = line.split(':')
            res[duple[0]] = duple[1]
                
                
    return res       


def check_user(user_id, pwd):
    users = load_user_pwd()
    return users[user_id] == pwd
    
def give_secret_santa(user_id):
    secret = load_user_secret()
    return secret[user_id]
    