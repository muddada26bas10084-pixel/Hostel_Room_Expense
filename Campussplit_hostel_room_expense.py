# campussplit - hostel room expense manager
# python essentials sem 1 project

# initial setup
roommates = ["Alex", "Sam", "Rahul"]
categories = ["Food", "Groceries", "Internet", "Misc"]

# dict to track total spent per category
cat_totals = {}
for c in categories:
    cat_totals[c] = 0.0

# dict to track how much each person paid
paid_totals = {}
for r in roommates:
    paid_totals[r] = 0.0

# list of tuples to store full log: (item, payer, amount, category)
history = []

monthly_budget = 6000.0
total_spent = 0.0

running = True
while running:
    print()
    print("==================================")
    print("      CAMPUSSPLIT HOSTEL TRACKER  ")
    print("==================================")
    print("1. Add new shared expense")
    print("2. View category breakdown")
    print("3. Check roommate balances & split")
    print("4. Budget alert & expense log")
    print("5. Exit")
    
    choice = input("Select an option (1-5): ")
    
    if choice == '1':
        print("\n-- Add New Expense --")
        item = input("What was purchased?: ")
        
        print("Roommates:", roommates)
        payer = input("Who paid?: ").strip()
        
        # validate person
        if payer not in roommates:
            print("Name not found in room list. Try again.")
            continue
            
        amt_str = input("Enter amount (Rs): ")
        # basic check for digits
        valid_amt = True
        has_dot = 0
        for ch in amt_str:
            if ch == '.':
                has_dot = has_dot + 1
            elif ch not in "0123456789":
                valid_amt = False
                break
                
        if valid_amt == False or has_dot > 1 or len(amt_str) == 0:
            print("Invalid amount entered.")
            continue
            
        amt = float(amt_str)
        if amt <= 0:
            print("Amount must be greater than zero.")
            continue
            
        print("Available Categories:", categories)
        cat = input("Enter category: ").strip()
        if cat not in categories:
            print("Category not listed, saving under Misc.")
            cat = "Misc"
            
        # update totals
        total_spent = total_spent + amt
        cat_totals[cat] = cat_totals[cat] + amt
        paid_totals[payer] = paid_totals[payer] + amt
        
        # store in history as tuple
        entry = (item, payer, amt, cat)
        history.append(entry)
        print("Expense recorded successfully!")
        
    elif choice == '2':
        print("\n-- Category Spending Breakdown --")
        if total_spent == 0:
            print("No expenses recorded yet.")
        else:
            for c in categories:
                spent = cat_totals[c]
                share = (spent / total_spent) * 100
                print("- " + c + ": Rs " + str(spent) + " (" + str(round(share, 1)) + "%)")
            print("Total Group Spend: Rs " + str(total_spent))
            
    elif choice == '3':
        print("\n-- Roommate Split & Balances --")
        if total_spent == 0:
            print("No expenses recorded yet.")
        else:
            per_person_share = total_spent / len(roommates)
            print("Equal share per person: Rs " + str(round(per_person_share, 2)))
            print("----------------------------------")
            
            for r in roommates:
                paid = paid_totals[r]
                balance = paid - per_person_share
                
                if balance > 0:
                    print(r + " paid Rs " + str(paid) + " -> Gets back: Rs " + str(round(balance, 2)))
                elif balance < 0:
                    owes = per_person_share - paid
                    print(r + " paid Rs " + str(paid) + " -> Owes: Rs " + str(round(owes, 2)))
                else:
                    print(r + " paid Rs " + str(paid) + " -> Settled up!")
                    
    elif choice == '4':
        print("\n-- Budget & History Log --")
        print("Monthly Budget Limit: Rs " + str(monthly_budget))
        print("Total Spent So Far  : Rs " + str(total_spent))
        
        # budget warning
        if total_spent > monthly_budget:
            print("WARNING: You have exceeded the room budget by Rs " + str(total_spent - monthly_budget) + "!")
        elif total_spent >= (monthly_budget * 0.8):
            print("ALERT: You have used over 80% of the room budget.")
        else:
            print("Status: Spending is within the safe limit.")
            
        print("\nFull Expense History:")
        if len(history) == 0:
            print("No items to show.")
        else:
            count = 1
            for row in history:
                # row is (item, payer, amt, cat)
                print(str(count) + ". " + row[0] + " | Rs " + str(row[2]) + " | Paid by " + row[1] + " [" + row[3] + "]")
                count = count + 1
                
    elif choice == '5':
        print("Closing CampusSplit. Have a good day!")
        running = False
        
    else:
        print("Please choose a valid number from 1 to 5.")

-