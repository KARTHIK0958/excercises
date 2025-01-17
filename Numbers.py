class Numbers:
    def __init__(self):
        self.Value = int(input("Enter a number: ")) 
    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True
    def ChkPerfect(self):
        sum_factors = self.SumFactors()
        return sum_factors == self.Value
    def SumFactors(self):
        factors = self.Factors()
        return sum(factors)
    def Factors(self):
        factors = []
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                factors.append(i)
        print(f"Factors of {self.Value}: {factors}")
        return factors
num1 = Numbers()
print(f"Is {num1.Value} prime? {num1.ChkPrime()}")
print(f"Is {num1.Value} perfect? {num1.ChkPerfect()}")
num1.Factors()
print(f"Sum of factors of {num1.Value}: {num1.SumFactors()}")
print()
num2 = Numbers()
print(f"Is {num2.Value} prime? {num2.ChkPrime()}")
print(f"Is {num2.Value} perfect? {num2.ChkPerfect()}")
num2.Factors()
print(f"Sum of factors of {num2.Value}: {num2.SumFactors()}")
