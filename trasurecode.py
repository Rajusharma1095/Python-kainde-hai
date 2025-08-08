print("Welcome to Treasure Island.  ")
print("Your mission is to find the treasure")
print("You are at a cross road. where do you want to go?")

rode=input('Type "left" or "right" :').lower()
if rode=="left":
    print("You have come to lake. There is an island in the middle of the lake.")
    river=input('Type "wait" to wait for the boat. Type "swim" to swim across').lower()
    if river=="wait":
        print("You are arived at the island unharmed. There is a house with 3 doors. ")
        island=input('One red, one yellow and one blue. Which colour do you choose? ').lower()
        if island=="yellow" :
            print("You win!")
        elif island=="red"or island=="blue":
            print("Game Over.")
    elif river=="swim":
        print("Game over.")
elif rode=="right":
    print("Game over.")

      
