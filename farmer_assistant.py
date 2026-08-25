import csv
from ai_recommendations import get_recommendation


def load_farm_data():
    with open("farm_data.csv", "r") as file:
        return list(csv.DictReader(file))


def show_economic_information(data):
    print("\nAvailable crops:")

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

    print("\nCrop not found.")


def compare_crop_profits(data):
    best_crop = None
    highest_profit = 0

    print("\n📊 Estimated Crop Profit Comparison")

    for row in data:
        cost = float(row["production_cost"])
        income = float(row["expected_income"])
        profit = income - cost

        print(f"{row['crop']}: ₦{profit:,.0f}")

        if profit > highest_profit:
            highest_profit = profit
            best_crop = row["crop"]

    print(f"\n🏆 Highest estimated profit: {best_crop}")
    print(f"Estimated profit: ₦{highest_profit:,.0f}")


def get_crop_recommendation():
    crop = input("\nEnter your crop: ")
    problem = input("Describe the problem: ")

    recommendation = get_recommendation(crop, problem)

    print("\n🌾 Recommendation:")
    print(recommendation)


def farmer_assistant():
    data = load_farm_data()

    print("\n🌾 Kebbi AI Farmer Assistant")
    print("1. Crop economic information")
    print("2. Crop problem recommendation")
    print("3. Compare crop profits")

    choice = input("\nChoose an option: ")

    if choice == "1":
        show_economic_information(data)
    elif choice == "2":
        get_crop_recommendation()
    elif choice == "3":
        compare_crop_profits(data)
    else:
        print("\nInvalid option.")


if __name__ == "__main__":
    farmer_assistant()
