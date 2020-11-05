class CoffeeMachine:
    def __init__(self):
        self.avail_water = 400
        self.avail_milk = 540
        self.avail_coffee_beans = 120
        self.avail_cups = 9
        self.avail_money = 550

    def action(self, command):
        if command == "buy":
            reply = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
            if reply == "1":
                self.buy(250, 0, 16, 4)
            elif reply == "2":
                self.buy(350, 75, 20, 7)
            elif reply == "3":
                self.buy(200, 100, 12, 6)
            elif reply == "back":
                pass
        elif command == "fill":
            self.fill()
        elif command == "take":
            self.take()
        elif command == "remaining":
            self.show_available()
        elif command == "exit":
            exit(0)

    def show_available(self):
        print("The coffee machine has:")
        print(self.avail_water, "of water")
        print(self.avail_milk, "of milk")
        print(self.avail_coffee_beans, "of coffee beans")
        print(self.avail_cups, "of disposable cups")
        print('$' + str(self.avail_money), "of money")

    def buy(self, water, milk, coffee_beans, money):
        if self.avail_water < water:
            print("Sorry, not enough water!")
        elif self.avail_milk < milk:
            print("Sorry, not enough milk!")
        elif self.avail_coffee_beans < coffee_beans:
            print("Sorry, not enough coffee beans!")
        elif self.avail_cups < 1:
            print("Sorry, not enough cups!")
        else:
            self.avail_water -= water
            self.avail_milk -= milk
            self.avail_coffee_beans -= coffee_beans
            self.avail_cups -= 1
            self.avail_money += money
            print("I have enough resources, making you a coffee!")

    def fill(self):
        self.avail_water += int(input("Write how many ml of water do you want to add:\n"))
        self.avail_milk += int(input("Write how many ml of milk do you want to add:\n"))
        self.avail_coffee_beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.avail_cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))

    def take(self):
        print("I gave you ${}".format(self.avail_money))
        self.avail_money -= self.avail_money


machine = CoffeeMachine()
while True:
    machine.action(input("Write action (buy, fill, take, remaining, exit):\n"))
