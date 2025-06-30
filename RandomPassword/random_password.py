#Random Password Generator
import random as r
import string as s
size=int(input("Enter the length of the password: "))
charact_list=""
print("What kind of random password you want? \n 1.Letters \n 2.Digits \n 3.Special Characters \n 4.Exit")
print("If you selected, than don't forget to give 4 to exit and generate your random password.")
while(True):
    choice=int(input("Enter your choice: "))
    if choice==1:
        charact_list+=s.ascii_letters
    elif choice==2:
        charact_list+=s.digits
    elif choice==3:
        charact_list+=s.punctuation
    elif choice==4:
        break
    else:
        print("Enter Valid input!")
passkey=[]
for i in range(size):
    random=r.choice(charact_list)
    passkey.append(random)
print("Your Random password is : "+ "".join(passkey))


