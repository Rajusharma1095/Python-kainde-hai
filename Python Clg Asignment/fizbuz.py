''''Fizz Buzz: Write a program that prints the numbers from 1 to 100. But for multiples of 
three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". 
For numbers that are multiples of both three and five, print "Fizz Buzz".'''
i=1
while i!=100:
    if i%3==0 and i%5==0:
        print("Fizz Buzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else :
        print(i)
    i+=1

