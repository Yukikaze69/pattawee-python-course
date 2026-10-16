# Complete this program to classify people by age
<<<<<<< HEAD
#age = int(input("Enter age: "))
=======
age = int(input("Enter age: "))
>>>>>>> upstream/main

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
<<<<<<< HEAD
#if age >= 60:
    #print("Senior")
#elif age >= 20:
 #   print("adult")
#elif age >= 13:
  #  print("teenager")
#elif age >= 0:
   # print("child")
=======

>>>>>>> upstream/main


# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
<<<<<<< HEAD
        if choice == "1":
            print("Your Balance:{blance}")
        elif choice == "2":
            withdraw = input("Enter amount: ")
            balance = balance - withdraw
        elif choice == "3":
            deposit = input("Enter amount: ")
             balance = balance + deposit   
        elif choice == "4":
            break        
=======
        
>>>>>>> upstream/main
else:
    print("Invalid PIN")
