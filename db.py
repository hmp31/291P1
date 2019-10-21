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
    

    valid = False
    while (not valid):
        username = input("Username: ")
        password = input("Password: ")
        cursor.execute(" SELECT * FROM users WHERE uid = ? and pwd = ?; ", (username, password)) 
        user = cursor.fetchone()

        if user != None:
            valid = True
        else:
            print("Incorrect username or password")
            
    connection.commit()
    return user

def display_menu(utype):
        if utype == 'a':
            print("Which task would you like to perform?")
            print("1 - Register a birth")
            print("2 - Register a marriage")
            print("3 - Renew vehicle registration")
            print("4 - Process a bill of sale")
            print("5 - Process a payment")
            print("6 - Get a driver abstract")
            valid = False
            
            while (not valid):
                task = int(input("Enter a number: "))
                if (task in range(1,7)):
                    valid = True
                else:
                    print("Please enter a valid option")
                    
                
            return task
        
        elif utype == 'o':
            print("1 - Issue a ticket")
            print("2 - Find a car owner") 
            valid = False
            
            while (not valid):
                task = int(input("Enter a number: "))
                if (task in range(1,3)):
                    valid = True
                else:
                    print("Please enter a valid option")
            return task + 6
        

        
def register_birth():
    pass
def register_marriage():
    pass
def renew_reg():
    pass
def bill_of_sale():
    pass
def process_payment():
    pass
def get_driver_abstract():
    pass
def issue_ticket():
    pass
def find_car_owner():
    pass

def main():
    global connection, cursor
    
    connect_to_DB()
    user = get_login()
    print("Welcome " + user[3])
    task = display_menu(user[2])
    if task == 1:
        register_birth()
    elif task == 2:
        register_marriage()
    elif task == 3:
        renew_reg()
    elif task == 4:
        bill_of_sale()
    elif task == 5:
        process_payment()
    elif task == 6:
        get_driver_abstract()
    elif task == 7:
        issue_ticket()
    elif task == 8:
        find_car_owner()
        
    
    
 

if __name__ == "__main__":
    main()
