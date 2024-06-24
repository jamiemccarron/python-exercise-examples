upTo = 20 # Only 1 to 20 inclusive
myList = []

for x in range(0, upToo + 1):
    # % is called modulo. it return 0 if a number is divisible by a number.
    # in this case we are saying is x divisible by 3 and divisible by 5
    if x%3=0 and x%5==0:
        myList.append ("fizzbuzz!")
    elif x%3==0:
        myList.append ("fizz")
    elif x%5==0:
        myListappend ("buzz")
    else:
        myList.append (x)

# Nothing below this comment is broken.
expectedOutput = [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz!', 16, 17, 'fizz', 19, 'buzz']










print ("The output should look like the following:")
print (expectedOutput)
print ("")
print (myList)
# Assert is a way to stop the code from running if the condition doesn't match.
# In this case we want to check that the output you are fixing is correct.
assert (myList == expectedOutput)
