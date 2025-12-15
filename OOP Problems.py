class Student:
    def __init__(self, name, roll, marks: dict):
        self.name, self.roll, self.marks = name, roll, marks

    def average(self):
        return sum(self.marks.values()) / len(self.marks)

    def grade(self):
        avg = self.average()
        return "A" if avg >= 90 else "B" if avg >= 80 else "C" if avg >= 70 else "D" if avg >= 60 else "F"

    def summary(self):
        avg = self.average()
        print(f"Name: {self.name}, Roll: {self.roll}")
        print(f"Marks: {self.marks}")
        print(f"Average: {avg:.2f}, Grade: {self.grade()}")

if __name__ == "__main__":
    subjects = ["Maths", "Science", "English", "History", "Computer"]
    marks = {s: float(input(f"{s} (0-100): ")) for s in subjects}
    s = Student(input("Name: "), input("Roll: "), marks)
    s.summary()


# 2.Create a BankAccount class with deposit, withdraw, and balance check.

def main():
    bal = 0.0
    while True:
        try:
            ch = input("\n1) Deposit  2) Withdraw  3) Check Balance  4) Exit\nChoose: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye."); break

        if ch == "1":
            try:
                amt = float(input("Deposit amount: "))
            except ValueError:
                print("Invalid amount."); continue 
            if amt <= 0:
                print("Enter a positive amount."); continue
            bal += amt; print(f"Deposited {amt:.2f}. Balance: {bal:.2f}")

        elif ch == "2":
            try:
                amt = float(input("Withdraw amount: "))
            except ValueError:
                print("Invalid amount."); continue
            if amt <= 0:
                print("Enter a positive amount."); continue
            if amt > bal:
                print("Insufficient funds. Skipping."); continue
            bal -= amt; print(f"Withdrew {amt:.2f}. Balance: {bal:.2f}")

        elif ch == "3":
            print(f"Balance: {bal:.2f}")

        elif ch == "4":
            print("Goodbye."); break

        else:
            print("Enter 1-4.")

if __name__ == "__main__":
    main()
    print("ATM session ended.")



# 3.Create a Car class with brand, model, and a drive() method.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def drive(self):
        print(f"The {self.brand} {self.model} is now driving!")

car1 = Car("BMW", "X5")
car1.drive()


# 4.Create a Restaurant class that stores menu items in a dictionary and prints the bill.
class Restaurant:
    def __init__(self):
        self.menu = {"Burger": 50, "Pizza": 100, "Pasta": 80, "Coffee": 30}
        self.order = {}
    
    def add_item(self, item, qty=1):
        if item in self.menu:
            self.order[item] = self.order.get(item, 0) + qty
    
    def print_bill(self):
        total = 0
        print("\n----- Bill -----")
        for item, qty in self.order.items():
            cost = self.menu[item] * qty
            print(f"{item} x{qty}: ₹{cost}")
            total += cost
        print(f"Total: ₹{total}")

# Example
r = Restaurant()
r.add_item("Burger", 2)
r.add_item("Pizza")
r.print_bill()


# 5.Create a User class with private password and a method to validate login.

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # private
    
    def validate_login(self, password):
        return self.__password == password

user = User("ankit", "secret123")
print(user.validate_login("secret123"))  # True
print(user.validate_login("wrong"))      # False
