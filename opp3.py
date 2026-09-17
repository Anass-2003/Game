
import os

import time

def clear_screen():
  os.system('cls' if os.name=='nt'else 'clear')   

class User :
  def __init__(self,First_name, Last_name, Id, Password, Status="Inactive"):
        self.First_name=First_name
        self.Last_name=Last_name
        self.Id=Id
        self.Password=Password
        self.Status=Status
  def drucker(self):
        print(f"Name: {self.First_name}")
        print(f"Last name: {self.Last_name}")
        print(f"Email: {self.Id}")
        print(f"Password: {self.Password}")
        print(f"Status: {self.Status}")


def difrag():
    First_name=input("Enter First_name:")
    Last_name=input("Enter Lasr_name:")
    Id=input("Enter memberschip ID:") 
    status=input("Enter memberschip status or skeep:")
    Password=input("Enter password:")
    return User(First_name, Last_name, Id, Password,status)






def search_member(formation):
    clear_screen()
    search =input("""
      search by:
            
      1) nemberscip ID:
      2) first name:
      3) nemberscip status       

      *Enter your choice   :
            
              """)
    found_member=[]
    if search=='1':
        fra1=input("Enter te nember ID to search:")
        for x in formation:
            if x.Id==fra1:
                found_member.append(x)
                time.sleep(2)
                break
    elif search=='2':
        fra2=input("Enter te first name to search:")
        for x in formation:
            if x.First_name.lower()==fra2.lower():
                found_member.append(x)
                time.sleep(2)

    elif search=='3':
        fra3=input("Enter te membrscip status to search:")
        for x in formation:
            if x.Status.lower()==fra3.lower():
                found_member.append(x)
                time.sleep(2)
    else:
        print("Invaid choice. please try again.")
        time.sleep(1)

    if found_member:
        clear_screen()
        print("Members found")
        for x in found_member:
            x.drucker()
    else:
        print("Members not found!")
        time.sleep(2)



formation=[]
while True :
  print("\nWelcome to user managment")

  frag= input("""
  \nChoose an Action:
  1) add new user   
  2) Display als users
  3) search for a nember
  4) Exit

  *Enter your choice:""")

  if frag=='1':
      formation.append(difrag())
      print("user added succesfully")
      time.sleep(2)
      clear_screen()

  elif frag=='2':
      clear_screen()
      if formation:
          print("displayin all new_users.......")
          time.sleep(1)
          for i in formation:
              i.drucker()
              time.sleep(2)

    
      else:
        print("No user yet!")
        time.sleep(2)


  elif frag=='3':
      if formation:
        search_member(formation)
      else:
          print("No membrs to search!")
          time.sleep(2)
    
          

  elif frag=='4' :
     print("Exiting.....")
     break
  else:
     print("Invaid choice.please try again.")




  

