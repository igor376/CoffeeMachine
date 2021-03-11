# water = int(input("Write how many ml of water the coffee machine has:\n")) // 200
# milk = int(input("Write how many ml of milk the coffee machine has:\n")) // 50
# beans = int(input("Write how many grams of coffee beans the coffee machine has:\n")) // 15
# cups_needed = int(input("Write how many cups of coffee you will need:\n"))
# cups_in_machine = min(water, milk, beans)
# if cups_needed == cups_in_machine:
#     print("Yes, I can make that amount of coffee")
# elif cups_needed < cups_in_machine:
#     print("Yes, I can make that amount of coffee (and even", cups_in_machine - cups_needed, "more than that)")
# else:
#     print("No, I can make only", cups_in_machine, "cups of coffee")

# [water, milk, coffee beans, cups, price]
# name_of_resources = ["water", "milk", "coffee beans", "disposable cups", "price"]
# resources = [400, 540, 120, 9, 550]
# # [water, milk, coffee beans, cups, price]
# coffee = [[250, 0, 16, 1, -4], [350, 75, 20, 1, -7], [200, 100, 12, 1, -6]]
#
# x = 1
#
#
# def print_status():
#     print("The coffee machine has:")
#     print(resources[0], "of water")
#     print(resources[1], "of milk")
#     print(resources[2], "of coffee beans")
#     print(resources[3], "of disposable cups")
#     print(resources[4], "of money")
#
#
# def buy():
#     print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
#     type_of_coffee = input()
#     if type_of_coffee == "back":
#         return
#     cooking_coffee(int(type_of_coffee))
#
#
# def fill():
#     resources[0] += int(input("Write how many ml of water do you want to add:\n"))
#     resources[1] += int(input("Write how many ml of milk do you want to add:\n"))
#     resources[2] += int(input("Write how many grams of coffee beans do you want to add:\n"))
#     resources[3] += int(input("Write how many disposable cups of coffee do you want to add:\n"))
#
#
# def take():
#     print("I gave you $" + str(resources[4]))
#     resources[4] = 0
#
#
# def cooking_coffee(type_of_coffee):
#     global resources
#     if check_resources(type_of_coffee):
#         for i in range(5):
#             resources[i] -= coffee[type_of_coffee - 1][i]
#
#
# def check_resources(type_of_coffee):
#     for i in range(4):
#         if coffee[type_of_coffee - 1][i] > resources[i]:
#             print("Sorry, not enough", name_of_resources[i] + "!")
#             return False
#     print("I have enough resources, making you a coffee!")
#     return True
#
#
# def work():
#     while True:
#         options = input("Write action (buy, fill, take, remaining, exit):\n")
#         print()
#         if options == "buy":
#             buy()
#         elif options == "fill":
#             fill()
#         elif options == "take":
#             take()
#         elif options == "remaining":
#             print_status()
#         elif options == exit():
#             break
#         print()
#
#
# # work()


class CoffeeMachine:
    # [water, milk, coffee beans, cups, price]
    name_of_resources = ["water", "milk", "coffee beans", "disposable cups", "price"]
    # [water, milk, coffee beans, cups, price]
    coffee = [[250, 0, 16, 1, -4], [350, 75, 20, 1, -7], [200, 100, 12, 1, -6]]

    def __init__(self):
        self.state_of_machine = 0
        self.resources = [400, 540, 120, 9, 550]
        self.print_message()

    def work(self, command):
        if command == "buy" or self.state_of_machine == 1:
            self.buy(command)
            return True
        elif command == "fill" or self.state_of_machine >= 20:
            self.fill(command)
            return True
        elif command == "take":
            print()
            self.take()
            return True
        elif command == "remaining":
            print()
            self.state_of_machine = 4
            self.print_message()
            self.state_of_machine = 0
            self.print_message()
            return True
        elif command == "exit":
            return False

    def print_message(self):
        # 0 - main menu, 1 - buy, 2 - fill, 3 - take, 4 - remaining, 5 - exit
        if self.state_of_machine == 0:
            print("Write action (buy, fill, take, remaining, exit):")
        elif self.state_of_machine == 1:
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        elif self.state_of_machine == 4:
            print("The coffee machine has:")
            print(self.resources[0], "of water")
            print(self.resources[1], "of milk")
            print(self.resources[2], "of coffee beans")
            print(self.resources[3], "of disposable cups")
            print("${} of money\n".format(self.resources[4]))

    def buy(self, type_of_coffee):
        if self.state_of_machine == 0:
            print()
            self.state_of_machine = 1
            self.print_message()
            return
        if type_of_coffee == "back":
            self.state_of_machine = 0
            print()
            self.print_message()
            return
        self.cooking_coffee(int(type_of_coffee))
        self.state_of_machine = 0

    def cooking_coffee(self, type_of_coffee):
        if self.check_resources(type_of_coffee):
            for i in range(5):
                self.resources[i] -= self.coffee[type_of_coffee - 1][i]
        self.state_of_machine = 0
        self.print_message()

    def check_resources(self, type_of_coffee):
        for i in range(4):
            if self.coffee[type_of_coffee - 1][i] > self.resources[i]:
                print("Sorry, not enough {}!\n".format(self.name_of_resources[i]))
                return False
        print("I have enough resources, making you a coffee!\n")
        return True

    def take(self):
        print("I gave you {}$\n".format(str(self.resources[4])))
        self.resources[4] = 0
        self.state_of_machine = 0
        self.print_message()

    def fill(self, command):
        if self.state_of_machine == 0:
            print()
            self.state_of_machine = 21
            print("Write how many ml of water do you want to add:")
        elif self.state_of_machine == 21:
            self.resources[0] += int(command)
            self.state_of_machine = 22
            print("Write how many ml of milk do you want to add:")
        elif self.state_of_machine == 22:
            self.resources[1] += int(command)
            self.state_of_machine = 23
            print("Write how many grams of coffee beans do you want to add:")
        elif self.state_of_machine == 23:
            self.resources[2] += int(command)
            self.state_of_machine = 24
            print("Write how many disposable cups of coffee do you want to add:")
        elif self.state_of_machine == 24:
            self.resources[3] += int(command)
            self.state_of_machine = 0
            print()
            self.print_message()


machine = CoffeeMachine()
while machine.work(input()):
    pass
