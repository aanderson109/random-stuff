'''
Python Script that counts to a user defined number using an iterator class
Version 0.1 - 01/10/2021
Alex Anderson
'''
num_range = 1000000000      # defining the number we want to count to


class pyCounter:  # create a class to behave as the blueprint for an object that counts

    def __iter__(self):     # iter method acts similar to init() but always returns the iter object itself
        self.num = 0        # num is a variable we use for iterating; self lets use modify/ref it internally
        return self         # return the result

    def __next__(self):     # next method returns the next item in the sequence
        if self.num <= num_range:   # if statement that puts a limit on the counting
            x = self.num            # x is set equal to the current value of self.num
            self.num += 1           # add +1 to the value of self.num
            return x                # return the new value of x
        else:                       # if self.num is outside the <= num_range condition
            print("Counting Complete...")   # print "Counting Complete" to the terminal
            raise StopIteration             # stop iterating

counter = pyCounter()               # create an instance of pyCounter() called counter
countThousand = iter(counter)       # create a variable called countThousand that iterates the object counter

for i in countThousand:             # for loop that actually does the counting
    continue                        # continue lets the for loop execute each time


