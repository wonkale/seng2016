#!/usr/bin/python
import sys
# Ollakko vaiko eiko olla helppoa!
# Implementation of FizzBuzz v0.00

# Version 1: if number is divisible by 3, print Fizz
#            if number is divisible by 5, print Buzz
#            if both, print FizzBuzz
#            else print number

# Version 2: if number is prime, print "<number> is a prime" instead
#            Take one argument,  and count up to it

class FizzBuzz():
    def __init__(self):
        pass

    # Run from 1 to "end". Maybe. Test fails for some reason
    def run(self, end, out=sys.stdout):
        for i in range(1, end+1):
            print >> out, self.calc(i)

    # Seems to give correct values. Tested with 1 and 2.
    def calc(self, i):
	#Version 1&&2
        

		if (i%3 ==0 and i%5 ==0):
                    viesti = "FizzBuzz"
                elif (i%3 == 0):
                    viesti = "Fizz"
		elif (i%5 == 0):
                    viesti = "Buzz"
		else: 
                    viesti = i
                n = 2
                prime = True
		for n in range(2, i):
                    if (i % n) == 0:
                        prime = False
                if (prime == True and i != 1):
                        viesti = "%d is a prime" % i
		
		return viesti
	#version 2
	
		
		

    
   


if __name__ == "__main__":
    app = FizzBuzz()
    app.run(100)
	
