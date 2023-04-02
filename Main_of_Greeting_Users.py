Users_1=["user_1","user_2","user_3","user_4","user_5","user_6","user_7","user_8"]

Users_2=[]

def user_greeting(UserNames):
    if len(UserNames)!=0:
            for User in UserNames:
            
                if User.lower()=="admin":
                    print("Hello boss.")
                else:
                    print(f"Hello peasant. {User} is a great username ngl.")
    else:
        print("Damn man. We need to find some user")
list_input=input()
if list_input.lower()=="users_1":     
    user_greeting(Users_1)
elif list_input.lower()=="users_2":
     user_greeting(Users_2)
else:
     print("Enter a valid list. \nYou have two options: \n\t1.Users_1 \n\t2.Users_2") 
