import sqlite3

connection = None
cursor = None

def connect_to_DB():
    global connection, cursor
  
    path = input("Enter path of database: ")
    
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA forteign_keys=ON; ')
    connection.commit()
    return

def get_login():
    global connection, cursor
    
    username = input("Username: ")
    password = input("Password: ")
    valid = False
    while (! valid):
        cursor.execute(" SELECT * FROM users WHERE uid = ? and pwd = ?; ", (username, password)) 
        user = cursor.fetchone()
        if user != None:
            valid = True
        else:
            printf("Incorrect username or password")
            
    connection.commit()
    return user

def dis[laly_menu(utype):
        if utype == 'a':
            print("Which task would you like to perform?")
            print("1 - Register a birth")
            print("2 - Register a marriage")
            print("3 - Renew vehicle registration")
            print("4 - Process a bill of sale")
            print("5 - Process a payment")
            print("6 - Get a driver abstract")
            task = 9
            while (task not in range(1,7)):
                task = input("Enter a number: ")
            return task
        
        elif utype == 'o':
            print("1 - Issue a ticket")
            print("2 - Find a car owner") 
            while (task not in range(1,3)):
                task = input("Enter a number: ")
            return task
        

        

def main():
    global connection, cursor
    
    connect_to_DB()
    user = get_login()
    print("Welcome " + user[3])
    task = display_menu(user[2])
    
    
 

if __name__ == "__main__":
    main()
