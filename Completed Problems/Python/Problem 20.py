class Factorial:
    """
    Computes list of factorial up to the one specified in the constructor.
    These are accessible through get_fact method.
    """
    def __init__(self, factorial):
        self.fact = [1]
        for _ in range(factorial):
            self.factorialHelper(_ + 1)

    def factorialHelper(self, num):
        """
        Helper function to populate fact list of factorials
        """
        if len(self.fact) == num:
            self.fact.append(self.fact[-1]*num)
        else:
            raise NotImplementedError("This function is a helper function, and is not for external use")

    def get_fact(self, factorial_of):
        return self.fact[factorial_of]

def main():
    Hundred = Factorial(100)
    stringHundred = str(Hundred.get_fact(100))
    sum = 0
    for num in stringHundred:
        sum += int(num)
    print("The sum of the digits of 100! is: {}".format(sum))

if __name__ == "__main__":
    main()
