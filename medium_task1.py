def addbook(t,a):                                  #here we make a func. to add book in library
        shelf[t]=a
        print(t,"by",a,"is Added\n")
def searchbook_title(t):                           #here we make a function to seach book y title
        if t in shelf:
            print(t,"by",shelf[t],"is found")
        else:
            print("NO record found by title:-",t)
def showallbooks():                                #here program show all books in memory
    for title in shelf:
        
        print(title,"by",shelf[title])




#_main_




print("===welcome to Library Book Management===")


shelf={"The Forest of Enchantments":"Chitra Banerjee Divakaruni","The Far Field":"Madhuri Vijay","The Pilgrims Progress":"John Bunyan"}


while True:
    print("a) Add book ")
    print("b) search book by title ")
    print("c) show all book ")
    print("d) exit")
    v1=input("Enter your choice ").lower()
    if v1=="a":
        while True:
            t=input("Enter the title of book ").lower()
            a=input("Enter the name of author ").lower()
            if t==""and a!="":                               #this block execute when title is not input but author is given
                print("\nNote:- we can`t add a book wihout a title.\nour library have so many books by same author so\nwe need a title to add your book. \n")
            elif a=="" and t!="":                            #this block execute when author is not input but title is given so book will added in memory but as by unknown author
                addbook(t,"unknown")
            elif t=="" and a=="":                            #this block execute when title & author both is not input
                print("At least one field is required\n")
            else:                                            #this block execute when title & author both is input
                addbook(t,a)
            v3=input("Do you want to add more book ( yes or no )").lower()
            if v3=="yes":
                continue
            else:                                            #this block takes you back at the starting 
                break
    elif v1=="b":                                            #this block seach the book by title
        v2=input("Enter the title to search a book")
        searchbook_title(v2)
    elif v1=="c":                                            #this block show all the book in memory
        print()
        print("===here`s the all book in-Memory===")
        showallbooks()
    elif v1=="d":                                            #this block exit the program
        break
    else:print("invalid option is input plz try again")      #tis block stops you putting another values which are not given to be as used 
   
    
    
            
    
    

        




