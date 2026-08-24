def get_recommendation(crop, problem):
    crop = crop.lower()
    problem = problem.lower()

    if crop == "rice":
        if "brown" in problem or "yellow" in problem:
            return "Possible nutrient deficiency or disease. Check the crop carefully and consult an agricultural extension officer."
        elif "insect" in problem or "pest" in problem:
            return "Inspect the plants for pests and seek advice from an agricultural extension officer before applying any treatment."
        else:
            return "Monitor the crop regularly and seek professional agricultural advice if the problem continues."

    elif crop in ["maize", "millet", "sorghum"]:
        if "pest" in problem or "insect" in problem:
            return "Inspect the affected plants for pests and seek appropriate agricultural guidance."
        else:
            return "Monitor the crop, soil, and weather conditions and consult an agricultural extension officer if symptoms worsen."

    return "Please provide more information about the crop and problem, or consult an agricultural professional."


print("🌾 Kebbi AI Farmer Assistant")
crop = input("Enter your crop: ")
problem = input("Describe the problem: ")

recommendation = get_recommendation(crop, problem)

print("\nRecommendation:")
print(recommendation)
