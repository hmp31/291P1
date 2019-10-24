import sqlite3
import getpass
import random

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
        password = getpass.getpass()
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
        

        
def register_birth(user_info):

    print("\nBirth registry")
    reg_no = unique_registration()
    fname = input("First name: ") 
    lname = input("Last name: ")
    regplace = user_info[5]
    gender = input("Gender: ")

    m_fname = input("Mothers first name: ")
    m_lname = input("Mothers last name: ")
    cursor.execute(" SELECT * FROM persons WHERE fname = ? and lname = ?; ", (m_fname, m_lname)) 
    mother = cursor.fetchone()
    if mother == None:
        print("Mother's name not found in database. Redirecting to register mother...")
        insert_person()



    f_fname = input("Fathers first name: ")
    f_lname = input ("Fathers last name: ")
    cursor.execute(" SELECT * FROM persons WHERE fname = ? and lname = ?; ", (f_fname, f_lname)) 
    father = cursor.fetchone()
    if father == None:
        print("Father's name not found in database. Redirecting to register father...")
        insert_person()
    
    cursor.execute("SELECT address, phone FROM persons WHERE fname = ? AND lname = ?", (m_fname, m_lname))
    mothers_info = cursor.fetchone()
    address = mothers_info[0]
    phone = mothers_info[1]
    bdate = input("Birth date (YYYY-MM-DD): ")
    bplace = input("Birth place: ")
	
    data_person = (fname, lname, bdate, bplace, address, phone)

    cursor.execute("INSERT INTO persons VALUES (?, ?, ?, ? ,?, ?); ", data_person)

    data_birth = (reg_no, fname, lname, regplace, gender, f_fname, f_lname, m_fname, m_lname)
    cursor.execute("INSERT INTO births VALUES (?, ?, ?, date('now'), ?, ?, ?, ?, ?, ? ); ", data_birth)

    connection.commit()

	
	
		   
    
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

def unique_registration():
	return random.randint(0,9999)

def insert_person():
    print("Registering a person")
    fname = input("First name: ") 
    lname = input("Last name: ")
    bdate = input("Birth date: ")
    bplace = input("Birth place: ")
    address = input("Address: ")
    phone = input("Phone: ")

    data = [fname, lname, bdate, bplace, address, phone]

    for i in range(2, len(data)):
        if data[i] == '':
            data[i] = None

    cursor.execute("INSERT INTO persons VALUES (?, ?, ?, ?, ?, ?);", data)

    cursor.execute("SELECT * FROM persons WHERE fname = ? AND lname = ?", (fname, lname))
    check = cursor.fetchone()
    if check != None:
        print(fname + ' ' + lname + ' successfuly registered.')

    connection.commit()

def main():
    global connection, cursor
    
    connect_to_DB()
    user = get_login()
    print("Welcome " + user[3])
    task = display_menu(user[2])
    if task == 1:
        register_birth(user)
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
