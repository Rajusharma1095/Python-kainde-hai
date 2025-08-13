import random

Rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
randomesBtwn1_3=random.randint(0,2)
# print("Choices between Stone , paper and scissor ")
choice=int(input("Choices between Stone(0) , paper(1) and scissor(2):  "))
print(choice)
print(randomesBtwn1_3)
if choice==0 :
    print(f"Your Choice is {Rock}")
    if randomesBtwn1_3==choice:
        print(f"Computer Choice is {Rock}")
        print("Its Draw")
    if randomesBtwn1_3==1:
        print(f"Computer Choice is {Paper}")
        print("Computer Wins")
    if randomesBtwn1_3==2:
        print(f"Computer Choice is {Scissors}")
        print("You wins")

elif choice==1 :
    print(f"Your Choice is {Paper}")
    if randomesBtwn1_3==choice:
        print(f"Computer Choice is {Paper}")
        print("Its Draw")
    if randomesBtwn1_3==2:
        print(f"Computer Choice is {Scissors}")
        print("Computer Wins")
    if randomesBtwn1_3==0:
        print(f"Computer Choice is {Rock}")
        print("You wins")
elif choice==2 :
    print(f"Your Choice is {Scissors}")
    if randomesBtwn1_3==choice:
        print(f"Computer Choice is {Scissors}")
        print("Its Draw")
    if randomesBtwn1_3==2:
        print(f"Computer Choice is {Rock}")
        print("Computer Wins")
    if randomesBtwn1_3==0:
        print(f"Computer Choice is {Paper}")
        print("You wins")
else:
    print("Choice Your Otions Wisely ")