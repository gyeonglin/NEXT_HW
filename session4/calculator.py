class Calculator :
    def __init__(self, name, age) :
        self.name = name
        self.result = 0
        self.age = age
    
    def add(self, num) :
        self.result += num
        return self.result
    
    def sub(self, num) :
        self.result -= num
        return self.result

    def mul(self, num) :
        self.result *= num
        return self.result
    
    def div(self, num) :
        if num == 0 :
            print("0으로 나눌 수 없습니다")
            return None
        self.result /= num
        return self.result

    def reset(self) :
        self.result = 0

calculator1 = Calculator("지상렬", 19)

print(calculator1.age)

print(calculator1.name)

print(calculator1.add(4))

print(calculator1.sub(3))

print(calculator1.mul(8))

print(calculator1.div(4))


