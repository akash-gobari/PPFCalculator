def ppf_calculator():
    max_limit = 150000
    rate = 0.071  # 7.1% annual interest

    try:
        years = int(input("Enter number of years you want to stay invested: "))
        yearly_contribution = float(input("Enter yearly contribution amount (₹): "))
        if yearly_contribution > max_limit:
            print(f"Contribution exceeds limit. Setting yearly contribution to ₹{max_limit}.")
            yearly_contribution = max_limit

        early_opening = input("Did you open the account before April 5 in the first year? (yes/no): ").strip().lower()
        zeroth_year_investment = 0
        if early_opening == "no":
            zeroth_year_investment = float(input("Enter investment amount made in the year of opening (Zeroth Year) (₹): "))
            if zeroth_year_investment > max_limit:
                print(f"Zeroth year investment exceeds limit. Setting to ₹{max_limit}.")
                zeroth_year_investment = max_limit

        balance = zeroth_year_investment
        total_interest = 0

        print("\nYear | Opening Balance | Contribution | Interest Earned | Closing Balance")
        print("-----|------------------|--------------|------------------|------------------")

        for year in range(1, years + 1):
            opening_balance = balance
            interest = (opening_balance + yearly_contribution) * rate
            balance += yearly_contribution + interest
            total_interest += interest
            print(f"{year:>4} | ₹{opening_balance:>14,.2f} | ₹{yearly_contribution:>10,.2f} | ₹{interest:>14,.2f} | ₹{balance:>14,.2f}")

        total_invested = yearly_contribution * years + zeroth_year_investment

        print(f"\n🔹 Summary After {years} Years:")
        print(f"Total Invested       : ₹{total_invested:,.2f}")
        print(f"Total Interest Earned: ₹{total_interest:,.2f}")
        print(f"Final Corpus         : ₹{balance:,.2f}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Run the calculator
ppf_calculator()
