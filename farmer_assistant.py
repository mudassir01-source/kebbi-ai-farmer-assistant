import csv

def show_farm_data():
    print("\n🌾 Kebbi AI Farmer Assistant")
    print("Crop Economic Information\n")

    with open("farm_data.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            crop = row["crop"]
            cost = float(row["production_cost"])
            income = float(row["expected_income"])
            profit = income - cost

            print(f"Crop: {crop}")
            print(f"Production Cost: ₦{cost:,.0f}")
            print(f"Expected Income: ₦{income:,.0f}")
            print(f"Expected Profit: ₦{profit:,.0f}")
            print("-" * 30)


if __name__ == "__main__":
    show_farm_data()
