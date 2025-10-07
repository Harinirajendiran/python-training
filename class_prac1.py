class Icecream:
#def _init_(self,name):
    def read(self,name):
        self.name=name
    def write(self):
        print(f"{self.name}")
p=Icecream()
p.read("blueberry")
p.write()