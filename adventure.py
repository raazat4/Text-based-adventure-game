

print("Welcome to text based adventure game!!\n Hope you like it!\n\n\n\n")
gender = input("What character do you want to be (Boy/Girl)?: ")


####################For Boy Adventure  ######################## 

if(gender.upper()=="BOY"):
    name = input("\nChoose a suitable name for your character: ")
    print(f"Hey {name}! Welcome to our latest game")
    choice = input(f"Hey {name}! where do you want to start your journey as a Millionaire or Employer: ")
    if(choice.upper()=="MILLIONAIRE"):
        print(f"{name.upper()} You are too greedy!\n Due to too much greediness you have been deleted by system")
        
    elif(choice.upper()=="EMPLOYER"):
        print(f"{name} your journey starts now")
        print(f'''As an employee {name.upper()}, you are working at midnight at a company.
              Years have passed and now you are thinking of falling in love. Since you know one person
              of company and you want to share your feeling. You was about to tell her tomorrow but late night
              you encounter an vampire. 
              ''')
        choice = input(f"{name.upper()}, Do you want to kill him? y/n: ")
        if(choice.upper()=="Y"):
            choice = input(f'''{name.upper()}, choose any of these magical power
                           1) Fire
                           2) Water
                           3) Earth
                           4) Air
                           5) Dark
                           6) Light\n''')
            if(choice.upper()=="FIRE"):
                print(f"{name.upper()}, fire power is not good for vampire.")
                print(f"{name.upper()}, you have been killed by vampire")
            elif(choice.upper()=="WATER"):
                print(f"{name.upper()}, water power is not good for vampire.")
                print(f"{name.upper()}, you have been killed by vampire")
            elif(choice.upper()=="EARTH"):
                print(f"{name.upper()}, earth power is not good for vampire.")
                print(f"{name.upper()}, you have been killed by vampire")
            elif(choice.upper()=="AIR"):
                print(f"{name.upper()}, air power is not good for vampire.")
                print(f"{name.upper()}, you have been killed by vampire")
            elif(choice.upper()=="DARK"):
                print(f"{name.upper()}, dark power is not good for vampire.")
                print(f"{name.upper()}, you have been killed by vampire")
            else:
                print(f"Congratulation! {name.upper()}, light power is good for vampire. You killed an vampire!")
                choice = input(f"{name.upper()}, do you wish to continue?: ")
                if(choice.upper()=="Y"):
                    print(f"{name.upper()}, Congratulation! you are about to get entry in next story")
                    
                    """
                    You can add the next story based on you intelligence here
                    choose any kind of loop statement
                    
                    """
                else:                    
                    print(f"{name.upper()}, you have been deleted by system since you have no interest in upcoming story")
                
                            
        else:
            print("You are a slug! since you are scared to encounter vampire you have been deleted by system.")
        
    else:
        print(f"{name.upper()}, Due to your foolish idea you have been deleted by system")
        
        
                    
####################For Girl Adventure  ######################## 

elif(gender.upper()=="GIRL"):
    name = input("Choose a suitable name for your character: ")
    print(f"Hey {name}! Welcome to our latest game")
    choice = input(f"Hey {name}! where do you want to start your journey as a Millionaire or Beggar: ")
    if(choice.upper()=="MILLIONAIRE"):
        print(f"{name.upper()} You are too greedy!\n Due to too much greediness you have been deleted by system")
    elif(choice.upper()=="BEGGER"):
        print(f"{name} your journey starts now")
    """ Please add the story for girl as i
    have shown in boy part
    story can be of any type
    """
    
    
###################      End      ##################   
else:
    print("your character has been destroyed by system due to invalid choice")
    
    
