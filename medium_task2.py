print("===welcome to your Personal Expense Tracker===\n")

dict1={"unknown":int(0),"food":int(250),"travel":int(5000)}                     #here we store category with their amount spent

while True:
        print("a) add expenses\nb) view total spent\nc) view per-category breakdown\nd) exit")
        v3=input("|choose your option|").lower()          
        if v3=="a":
                  print("Note:- if you don`t mention the category then \n       amount will be added to unknown category\n")
                  while True:
                        v2=input("Enter the category ")
                        v1=input("Enter the amount")
                        if (v1=="" or v1=="0") and v2=="":                      #here if amount and catgory both are not input it will raise an valueerror so we handle it by try and except statements
                               try:
                                   print(int(v1))
                               except ValueError as ve:
                                   print("At one field is required\n")
                                   continue
                        if (v1=="" or v1=="0") and v2!="":                      #here if amount is not input so it can not be added  
                               print("amount can`t be zero or null")
                        elif v2=="" and (v1!="" or v1!="0"):                    #here if category is not input but amount is given so it will added to unknown category 
                               v1=int(v1)
                               dict1["unknown"]+=int(v1)
                               print("Amount added in unknown category\n")
                        elif (v2!="" or v2.isalnum()) and v1!="":               #here if both are given so they will be added 
                               v1=int(v1)
                               if v2 in dict1.keys():                           #here if category exist it will added in it
                                   dict1[v2]=dict1[v2]+v1
                                   print(v1,"is added in category",v2)
                               else:                                            #here if category dont exist so it makes a new one
                                   dict1[v2]=v1
                                   print(v1,"is added in category",v2)
                        v4=input("Do you want add expenses again! (yes or no)]\n")
                        if v4=="yes":
                            continue
                        else:                                                   #here it takes you to start
                            break
        elif v3=="b":                                                           #here it show total spent together of all category 
            total_spent=0
            for key in dict1:
                total_spent+=dict1[key]
            print("Total spent = ",total_spent,"\n")

        elif v3=="c":                                                           #here it shows category and its amount spent 
            for key in dict1:
                print("|Category:-|",key)
                print("|Amount:-  |",dict1[key],"\n")
        elif v3=="d":                                                           #it exits the program
            print("===EXIT===")
            break
        else:print("plz enter right choice\n")



    
                    
    

