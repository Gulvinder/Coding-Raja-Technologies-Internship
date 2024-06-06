import json
import os

class BudgetTracker:
    def __init__(self, filename="transactions.json"):
        self.filename = filename
        self.transactions = self.load_transactions()
    
    def load_transactions(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []
    
    def save_transactions(self):
        with open(self.filename, 'w') as file:
            json.dump(self.transactions, file, indent=4)
    
    def add_transaction(self, type, category, amount):
        transaction = {
            "type": type,
            "category": category,
            "amount": amount
        }
        self.transactions.append(transaction)
        self.save_transactions()
    
    def calculate_budget(self):
        total_income = sum(t["amount"] for t in self.transactions if t["type"] == "income")
        total_expense = sum(t["amount"] for t in self.transactions if t["type"] == "expense")
        return total_income - total_expense
    
    def analyze_expenses(self):
        expense_by_category = {}
        for t in self.transactions:
            if t["type"] == "expense":
                if t["category"] not in expense_by_category:
                    expense_by_category[t["category"]] = 0
                expense_by_category[t["category"]] += t["amount"]
        
        return expense_by_category
    
    def display_menu(self):
        print("Budget Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Budget")
        print("4. Analyze Expenses")
        print("5. Exit")
    
    def run(self):
        while True:
            self.display_menu()
            choice = input("Choose an option: ")
            if choice == '1':
                category = input("Enter income category: ")
                amount = float(input("Enter income amount: "))
                self.add_transaction("income", category, amount)
                print("Income added successfully.\n")
            elif choice == '2':
                category = input("Enter expense category: ")
                amount = float(input("Enter expense amount: "))
                self.add_transaction("expense", category, amount)
                print("Expense added successfully.\n")
            elif choice == '3':
                budget = self.calculate_budget()
                print(f"Remaining budget: {budget}\n")
            elif choice == '4':
                analysis = self.analyze_expenses()
                print("Expense Analysis by Category:")
                for category, amount in analysis.items():
                    print(f"{category}: {amount}")
                print()
            elif choice == '5':
                print("Exiting Budget Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    tracker = BudgetTracker()
    tracker.run()
