# Kebbi AI Farmer Assistant
# Early prototype for agricultural support

def farmer_assistant():
    print("🌾 Welcome to Kebbi AI Farmer Assistant")
    print("1. Crop problem")
    print("2. Farm profit calculation")

    choice = input("Choose an option: ")

    if choice == "1":
        crop = input("What crop are you growing? ").lower()
        problem = input("Describe the problem: ").lower()

        if "rice" in crop and ("brown" in problem or "yellow" in problem):
            print("Possible issue: nutrient deficiency or crop disease.")
            print("Recommendation: Consult an agricultural extension officer.")
        else:
            print("Please provide more details or consult an agricultural expert.")

    elif choice == "2":
        cost = float(input("Enter total farm cost: "))
        income = float(input("Enter expected income: "))

        profit = income - cost
        print(f"Estimated profit: ₦{profit:,.2f}")

    else:
        print("Invalid option. Please try again.")


if __name__ == "__main__":
    farmer_assistant()
