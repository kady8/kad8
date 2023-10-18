## exo 

    def sq(self, number):
        number = number**(1/2)
        return number
    
    def average(self, numbers):
        result = 0
        nb_of_numbers = 0
        for number in numbers:
            result += number
            nb_of_numbers += 1
            average = result/nb_of_numbers
        return average
    
    def parity(self, number):
        if (number % 2) == 0:
            print("{} is even".format(number))
        else:
            print("{} is odd".format(number))
    
    def sum(self, numbers):
        result = 0
        for number in numbers:
            result += number
        return result
        
print #test pour voir si tout est ok 
def():
