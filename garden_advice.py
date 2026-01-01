"""
Garden Advice Application

This program provides gardening advice based on
the season and plant type entered by the user.
"""

def get_user_input():
    """
    Prompts the user to enter the season and plant type.
    Returns both values in lowercase.
    """
    season = input("Enter the season (summer, winter, spring, autumn): ").lower()
    plant_type = input("Enter the plant type (flower, vegetable): ").lower()
    return season, plant_type


def get_season_advice(season):
    """
    Returns gardening advice based on the season.
    """
    season_advice = {
        "summer": "Water your plants regularly and provide some shade.",
        "winter": "Protect your plants from frost with covers.",
        "spring": "Prepare soil and start planting new seeds.",
        "autumn": "Prune plants and prepare the garden for winter."
    }
    return season_advice.get(season, "No advice available for this season.")


def get_plant_advice(plant_type):
    """
    Returns gardening advice based on the plant type.
    """
    plant_advice = {
        "flower": "Use fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests and harvest regularly."
    }
    return plant_advice.get(plant_type, "No advice available for this plant type.")


def main():
    """
    Main function that runs the garden advice app.
    """
    season, plant_type = get_user_input()

    advice = ""
    advice += get_season_advice(season) + "\n"
    advice += get_plant_advice(plant_type)

    print("\nGardening Advice:")
    print(advice)


if __name__ == "__main__":
    main()

