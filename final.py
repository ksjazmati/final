#Strings for later, will help with restricting user input from having certain characters.
badEmail = "!\"'#$%^&*()=+,<>/?;:[]{}\\ )"
badAddress = "!\"'@$%^&*_=+<>?;:[]{})"
#first function, realted for ID, must implement no alpha chracters, only numbers
def ID():
    while True:
        empID = input("Enter employee ID: ")      
        if empID == "":
            print("Employee ID cannot be empty. Enter again.")
        elif len(empID) > 7:
            print("Employee ID should be less than or equal to 7. Enter again.")
        elif empID.isdigit():
            break
        else:
            print("The employee ID has non numeric characters. Enter again")
    return empID
#second function, name function specifices that spaces, appostrophes and dashes are okay, as they can be found in names
def name():
    while True:
        empName = input("Enter employee name: ")
        if empName.strip() == "":
            print("Employee name can not be empty.")
        elif empName.lower().replace("-", "").replace("'", "").replace(" ", ""):
            break
        else:
            print("Enter correct employee name.")
    return empName
#email function, important to specifcy that @ and . symbol are allowed as they are apart of an email, utilzing the string from earlier for other chracter restrictions
def email():
    while True:
        empEmail = input("Enter employee email: ")
        if empEmail == len(badEmail):
            print(" ")
        elif empEmail.strip().replace("@", "").replace(".", ""):
            break
        else:
            print("Do not use any of these characters: ! \" ' # $ % ^ & * ( ) = + , < > / ? ; : [ ] { } \\ ). Try again.")
            
    return empEmail
#address function, similar to email function,important to specifcy certian charcters are allowed and others are not.
def address():
    question = input("Do you want to give the Address (Y/N): ").upper()
    if question != 'N':
        while True:
            empAdd = input("Enter employee address: ")
            if empAdd == len(badAddress):
                print(" ")
            elif empAdd.strip().replace(",", "").replace(" ", ""):
                break
            else:
                print("Do not use any of these characters: !\"'@$%^&*_=+<>?;:[]{}). Try again.")
        return empAdd
    else:
        print("You did not provide an address")
#salary function, mkaing sure input is a float value as well as in a specific range.
def salary():
    while True:
        empSal = float(input("Enter salary: "))
        if empSal > 18.00 and empSal < 27.00:
            break
        else:
            print("Salary should be between 18 and 27")            
    return empSal
employees = list()

#combining everything together, making dictionaries on how the format should look like and appending.
while True:
    empID = ID()
    empName = name()
    empEmail = email()
    empAdd = address()
    empSal = salary()
    
    Employee_Dict = {
        "Empl_ID": empID, "Empl_Name": empName, "Empl_Email": empEmail, "Empl_Addrs": empAdd, "Empl_Sal": empSal
    }
    employees.append(Employee_Dict)
    #quit if enough inputs
    quit = input("Do you want to quit? Y/N ").upper()
    if quit == "Y":
        break
    #add modiftictions to data 
for employee in employees:
    employee["Empl_Name"] = "IT Department " + employee["Empl_Name"]
    employee["Empl_Sal"] = employee["Empl_Sal"] * 1.3
print(employees)