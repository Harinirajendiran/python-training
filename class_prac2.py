class person:
    #def _init_(self,name):
    def __init__(self,name):#double underscore#construtor function 
        self.name=name
    def greet(self):
        print(f"hii {self.name}")
p1=person("riniraj")
p1.greet()
p2=person("KH")
p2.greet()