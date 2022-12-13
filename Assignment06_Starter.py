# ------------------------------------------------------------------------ #
# Title: Assignment 06
# Description: Program currently loads data from file into list of Dictionary objects.
                # Write more functions to help organize the code.
# ChangeLog (Sebastian Moreno, November 23, 2022, Integrated functions into program):
# MMoreno,2022-11-23,Created file and inputted script provided from RRoot
# MMoreno,2022-11-23,Added code to complete assignment 6
# ------------------------------------------------------------------------ #


# -- Data -- #
# Declare variables and constants
objFileName = "ToDoFile.txt"
strData = ""  # A row of text data from the file
strChoice = ""  # Capture the user option selection


#Function 1

#Loading file into table
#Input variable filename
#Output: loaded the dictionary acting as a table into ToDoFile.txt

def load_file_into_table(filename): #Created a function called load file into table, the function is currently loading
                                        #filename into the table
    lstTable = []  # An empty list that acts as a table of rows
    objFile = open(filename, "r") #we created a variable (objFile) that will open the filename variable to read
    for line in objFile: #Created for loop for the objFile variable that will split the line with a comma
        strData = line.split(",")
        dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()} #And will add the following data to
                                                                            #lsttable as selected by task 0 and priority 1
        lstTable.append(dicRow)
    objFile.close() #Close the objfile or txt file
    return lstTable #Returns the list that acts as a table of rows


# Option 1 - Show the current items in the table | Function 2 Part 2

#Function two continues here
#Print message plus task and row added displayed
#Function ends and returns nothing after finishing

def show_the_current_items(lstTable):
    print("******* The current items ToDo are: *******")
    for row in lstTable:
        print(row["Task"] + "(" + row["Priority"] + ")")
    print("*******************************************")
    return None


#Function 3, Adding new data or menu of options #2
#Defining a new function called add_new_data that accepts three paramteres
def add_new_data(lstTable, strTask, strPriority):
    dicRow = {"Task": strTask, "Priority": strPriority} #Task and Priority are saved within dicRow variable
    lstTable.append(dicRow)  #Task and Prioritiy are added to lstTable
    print("Current Data in table:") #print function to show current data in table is and let the user know what we're lookign for

    # Show the current items in the table
    show_the_current_items(lstTable)  #Function we created that shows the current items in the list table
    return lstTable #return lstTable or in other words items within the list table as a result



# Function4 part 2
def remove_table_item(lstTable):
    # Step 5a - Allow user to indicate which row to delete
    strKeyToRemove = input("Which TASK would you like removed? - ")
    blnItemRemoved = False  # Use this to verify that the data was found and removed
    for row in lstTable: #for loop including list table
        task, priority = dict(row).values()  #get task and priority from each row
        if task == strKeyToRemove: #if statement
            lstTable.remove(row)  #removing row
            blnItemRemoved = True #make this equivalent to true

    # Update user on the status
    if blnItemRemoved == True:  #since if statement shows this is true we print the message for user to remove
        print("The task was removed.")
    else:   #else
        print("I'm sorry, but I could not find that task.")  #can not find task so let user know can not find to remove


    # Show the current items in the table
    show_the_current_items(lstTable) # Function 2 #call function to show current items in list table
    return lstTable  #return list table


# Function 5 part 2
def save_items_to_file(objFileName, lstTable):  # function takes as input obj file and list table
    # Show the current items in the table
    show_the_current_items(lstTable)  #function to show items in list table

    # Ask if they want save that data
    if "y" == str(input("Save this data to file? (y/n) - ")).strip().lower():  #user requested whether save data
                                                                    #through if statement
        objFile = open(objFileName, "w")     #since user said yes to save file, open text file to write
        for dicRow in lstTable:
            objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")   #writing task and priority down in
                                                                                    #text file
        objFile.close()                     #close text file after this process is done
        input("Data saved to file! Press the [Enter] key to return to menu.")  #let user know data saved
    else:   #else
        input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
            #let user know data was not saved
    return None #return nothing and end execution of this function




lstTable = load_file_into_table(objFileName) #This calls the function of list that acts as a table of rows
#  telling python to run all of the code that is within this function


# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()  # Add an extra line for looks


    #Function 2, Part 1
    # If statement to have user choice on menu of options for showing current data selected
    # Call the function show_the_current_items and lstTable within it
    # Show the current items in the table
    if strChoice.strip() == '1':
        show_the_current_items(lstTable)



    # Function 3, Part 1
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2': #user selection
        strTask = str(input("What is the task? - ")).strip()  #request user input for task
        strPriority = str(input("What is the priority? [high|low] - ")).strip() #request user input for priority
        lstTable = add_new_data(lstTable, strTask, strPriority) #list table variable, calls new function which takes in
        #task and priority. Output of this goes into the list table.


    # Function 4, Part 1
    # Step 5 - Remove a new item to the list/Table
    elif strChoice.strip() == '3': #user elects this option
        lstTable = remove_table_item(lstTable)  #call function to remove item from lsttable


    # Function 5, Part 1
    # Step 6 - Save tasks to the ToDoFile.txt file
    elif strChoice == '4':  #user inputted selection to save file to txt
        save_items_to_file(objFileName, lstTable)  # Call function to save everything in list table and save in text file




    elif strChoice == '5':
        break   # and Exit the program
