class FizzBuzz:
    def __init__ (self, upTo):
        self.upTo = upTo + 1
        self.myList = []

        self.BuildList ()

    def BuildList (self):
        for x in range(1, self.upTo):
            if x%3==0 and x%5==0:
                self.myList.append ("fizzbuzz!")
            elif x%3==0:
                self.myList.append ("fizz")
            elif x%5==0:
                self.myList.append ("buzz")
            else:
                self.myList.append (x)

    # The next 3 "def" are called class methods. One of the benifits of styling the
    # code in a class is someone chaging or adding to your code will know that
    # this class is all the bits to deal with FizzBuzz.
    # These methods don't exist in the smaller version of the code you fixed.
    def print_list (self):
        # enumerate is a function that we can use to obtain the index of a list.
        # in this case we are saying to start the index at 1.
        # enumerate (myList, starting_index,value)
        for idx, line in enumerate (self.myList, 1):
            print ("line %u is: %s" % (idx, str(line)))

    def print_line (self, x):
        # remember indexing in python starts from 0. When you are looking
        # for line 15, it's really index 14.
        print ("line %u is: %s" % (x, self.myList[x - 1]))

    def find_fizz_buzz_lines (self):
        # here we see the print_list function for loop is used inside []
        # for idx, x in enumerate (self.myList, 1)
        # the idx before and the if statment after is saying I only want output the
        # idx if the output of x = "fizzbuzz!"
        # lastly the [] wrapping the whole structure saves the idxs in a list
        lineNumbers = [idx for idx, x in enumerate (self.myList, 1) if x == "fizzbuzz!"]
        return lineNumbers

upTo = 50
# make A into the FizzBuzz class object with ini
A = FizzBuzz (upTo=upTo)
print ("List all elements:")
A.print_list ()
print ("Line 15:")
A.print_line (15)

print ("All lines in the list that are equal to fizzbuzz!:")
fizzBuzzLines = A.find_fizz_buzz_lines ()
print (fizzBuzzLines)
