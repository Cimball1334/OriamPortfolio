class VendingMachine:
    def ___init___(self):
        self.bottles = 20

    def purchase(self, amount):
        self.bottles -= amount

    def restock(self, amount):
        self.bottles += amount

    def get_inventory(self):
        return self.bottles

    def report(self):
        print(self.get_inventory())
    
  

    

