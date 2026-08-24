import csv

def load_farm_data():
    with open("farm_data.csv", "r") as file:
        return list(csv.DictReader(file))


def farmer_assistant():
    data = load_farm_data()

    print("\n🌾 Kebbi AI Farmer Assistant")
    print("Available crops:")

    for row in data:
        print("-", row["crop"])

    choice = input("\nEnter a crop name: ").strip().lower()

    for row in data:
        if row["crop"].lower() == choice:
            cost = float(row["production_cost"])
            income = float(row["expected_income"])
            profit = income - cost

            print(f"\nCrop: {row['crop']}")
            print(f"Production Cost: ₦{cost:,.0f}")
            print(f"Expected Income: ₦{income:,.0f}")
            print(f"Expected Profit: ₦{profit:,.0f}")
            return

    print("\nCrop not found. Please choose a crop from the list.")


if __name__ == "__main__":
    farmer_assistant()
