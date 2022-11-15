a = 0

print(a)

b= [10, "a"]
print (type(b))

def hello2(neco, who):
    text = "Nazdar" + who
    return text

def hello(neco:int, who:str) -> int:
    text = "Nazdar" + who
    return text

print(hello(0, " Patriku"))

class klasa:
    def __init__(self, parametr1, parametr2) -> None:
        #super().__init__()
        self.parametr2 = parametr1
        self.parametr1 = self.MojeMetoda(parametr1)
        
    def MojeMetoda(self, vstup):
        return vstup + 1

instanca = klasa(1,1)
print(instanca.parametr1, instanca.parametr2)
