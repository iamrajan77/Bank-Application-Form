""""
- In this code  functionality for all modules have been added except Forgot Password .
- Success messages like 'Ammount credited successfully' , 'Ammount debited successfully" have been added.
@author: RAJAN POUDEL
"""

#BANK APPLICATION FORM

# forgot password option isnot added , aand it will be added soon in upcoming version\code

# will display the message like , amount is credited to (account number\name)

data = {
    "1001" : ["Rajan",12000,"admin@123","savings"],
    "1002" : ["Bickey",20000,"pass@123","current"],
    "1003" : ["Abinash",25000,"pass@123","savings"],
    "1004" : ["",20000,"pass@123","current"]
}
Acc_No_List = list(data.keys())
while True:
    print(" MENU ".center(20,"#"))
    print("1 - Login".ljust(40))
    print("2 - Signup".ljust(40))
    print("3 - Forgot password".ljust(40))
    print("4 - Exit".ljust(40))
    print("#"*20)
    print("Enter your choice".ljust(40))
    Choise = int(input("".rjust(40)))

    #Login cradencials for all the users including bank manager

    if Choise == 1: 
        Acc_No_List = list(data.keys())
        print("Enter your Account number".ljust(40))
        Accno = input("".rjust(40))
        if Accno in Acc_No_List:
            print("Enter your password".ljust(40))
            Pssw = input("".rjust(40))
            if Pssw == data[Accno][2]:
                print("Login successful".ljust(40))
                while True:
                    print(" MENU ".center(20,"#"))
                    print("1 - Credit".ljust(40))
                    print("2 - Debit".ljust(40))
                    print("3 - Check balance".ljust(40))
                    print("4 - Details".ljust(40))
                    print("5 - Change password".ljust(40))
                    print("6 - Log out".ljust(40))
                    print("#"*20)
                    print("Enter your choice".ljust(40))
                    Choise = int(input("".rjust(40)))
                    if Choise == 1:
                        Balance = data[Accno][1]
                        print("Enter the ammount to be credited".ljust(40))
                        Amount = int(input("".rjust(40)))
                        Balance = Balance + Amount
                        data[Accno][1] = Balance
                        print("Annount credited successfully".ljust(40))
                    elif Choise == 2:
                        Balance = data[Accno][1]
                        print("Enter the ammount to be debited from your account".ljust(40))
                        Amount = int(input("".rjust(40)))
                        if Amount <= Balance:
                            Balance = Balance - Amount
                            data[Accno][1] = Balance
                            print("Annount debited successfully".ljust(40))
                        else:
                            print("Amount is not sufficient.".ljust(40))
                    elif Choise == 3:
                        print(f"You have {data[Accno][1]} balance in your account .".ljust(40))
                    elif Choise == 4:
                        Info_Header = ["Name","Balance","Password","Account type"]
                        print("Details".center(44,"*"))
                        for i in range(len(Info_Header)):
                            print(f"{Info_Header[i]:<20} - {data[Accno][i]:>20}".ljust(40))
                        print("*"*44)
                    elif Choise == 5:
                        Old_Pssw = data[Accno][2]
                        print("Enter your old password".ljust(40))
                        Pssw = input("".rjust(40))
                        if Pssw == data[Accno][2]:
                            print("Enter your new password".ljust(40))
                            Pssw = input("".rjust(40))
                            Pssw_Len = len(Pssw)
                            if Pssw_Len >= 8:
                                Count = {
                                    "Alphabet" : 0,
                                    "Number" : 0,
                                    "Spetial character" : 0
                                }
                                Spetial = ["!","@","#","$","%","^","&","*","(",")","_","+","-","=","{","}","[","]",",","\\",";",":","<",">","/","?","~","`"]
                                for char in Pssw:
                                    if (65 <= ord(char) <= 90) or 97 <= ord(char) <= 112 :#and Count["Alphabet"] == 0:
                                        Count["Alphabet"] = 1
                                    if 48 <= ord(char) <= 57 :#and Count["Number"] == 0:
                                        Count["Number"] = 1
                                    if char in Spetial:
                                        Count["Spetial character"] = 1
                                if Count["Alphabet"] == 1 and Count["Number"] == 1 and Count["Spetial character"] == 1:
                                    data[Accno][2] = Pssw
                                print("Confirm password".ljust(40))
                                Pssw = input("".rjust(40))
                                if Pssw == data[Accno][2]:
                                    data[Accno][2] = Pssw
                                    print("Password changed".ljust(40))
                                else:
                                    print("Incorrect password".ljust(40))
                                for i in Count:
                                    Count[i] = 0
                    elif Choise ==  6:
                        break
        else:
            print(f"{Accno} account number is not correct .".ljust(40))
            
    #Code for the Signup
    
    elif Choise == 2:
        print("Enter your name".ljust(40))
        Name =input("".rjust(40))
        print("Choose account type".ljust(40))
        print("1 - Savings".ljust(40))
        print("2 - Current".ljust(40))
        print("Enter your choice".ljust(40))
        Acc_Type = int(input("".rjust(40)))
        Acc = ""
        if Acc_Type == 1:
            Acc = "savings"
            print("Enter the initial balance ammount".ljust(40))
            Balance = int(input("".rjust(40)))
            if Balance < 0:
                print("For savings account the minimum balance is 0".ljust(40))
        elif Acc_Type == 2:
            Acc = "current"
            print("Enter the initial balance ammount".ljust(40))
            Balance = int(input("".rjust(40)))
            if Balance < 10000:
                print("For savings account the minimum balance is 10000".ljust(40))
        else:
            print("Invalid option".ljust(40))
        print("Enter your  password".ljust(40))
        Pssw = input("".rjust(40))
        Pssw_Len = len(Pssw)
        if Pssw_Len >= 8:
            Count = {
                "Alphabet" : 0,
                "Number" : 0,
                "Spetial character" : 0
            }
            Spetial = ["!","@","#","$","%","^","&","*","(",")","_","+","-","=","{","}","[","]",",","\\",";",":","<",">","/","?","~","`"]
            for char in Pssw:
                if (65 <= ord(char) <= 90) or 97 <= ord(char) <= 112 :#and Count["Alphabet"] == 0:
                    Count["Alphabet"] = 1
                if 48 <= ord(char) <= 57 :#and Count["Number"] == 0:
                    Count["Number"] = 1
                if char in Spetial:
                    Count["Spetial character"] = 1
            if Count["Alphabet"] == 1 and Count["Number"] == 1 and Count["Spetial character"] == 1:
                data[Accno][2] = Pssw
            print("Confirm password".ljust(40))
            Pssw = input("".rjust(40))
            if Pssw == data[Accno][2]:
                data[Accno][2] = Pssw
            else:
                print("Incorrect password".ljust(40))
            for i in Count:
                Count[i] = 0
            New_Data = [Name,Balance,Pssw,Acc]
            New_Acc_Num = str(int(Acc_No_List[len(Acc_No_List)-1])+1)
            data.update({New_Acc_Num : New_Data})
            print(f"Account created . Your account number is {New_Acc_Num}".ljust(40))
        
    #forgot password (Choice == 3)#
    
    """Code to be written here"""
    
    #finally the code is done , exit#
    
    if Choise == 4:
        break