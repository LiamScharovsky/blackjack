class shoppingCart:
    def  __init__ (self):
        self.shoppingList =[]
        self.name = ""
        self.quantity = 0

    def printList(self):
            print (self.shoppingList)


    
    def adding(self):
        self.name = input("What would you like to add to the cart?")
        self.shoppingList.append(self.name)
        print ("This is your list so far:")
        print (self.shoppingList)
        decision = input ("Would you like to add anything else?").lower()
        if decision == "yes":
            self.adding()
        else:
            return
    
    def deleting(self):
        name = input("What would you like to delete from the cart?")
        for item in self.shoppingList:
            if name == name:
                self.shoppingList.remove(item)
        decision = input ("Would you like to delete anything else?").lower()
        if decision == "yes":
            self.deleting()
        else:
            return



    def main (self):
        while True:
            decision = input("Would you like to add, delete, check or quit? ").lower()
            if decision == "quit":
                print ("Ok. Here's your final shopping list:")
                print (self.shoppingList)
                break
            elif decision == "add":
                self.adding()
            elif decision == "delete":
                self.deleting()
            elif decision == "check":
                self.printList()
            else:
                print("That command is not valid. Please try again")
        


cart = shoppingCart()
cart.main()
    