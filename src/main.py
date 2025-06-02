from climate_modeling import model_climate
from policy_recommendation import recommend_policy
from bio_inspired_modeling import analyze_environmental_data

def main():
    # Sample environmental data
    climate_data = [
        {"temperature": 25.5, "co2": 410},
        {"temperature": 26.0, "co2": 415}
    ]
    print(f"Climate Data: {climate_data}")

    # Model climate using bio-inspired algorithm
    climate_prediction = model_climate(climate_data)
    print(f"Climate Prediction: {climate_prediction}")

    # Analyze environmental data with NLP
    data_text = "Rising temperatures and CO2 levels are concerning."
    environmental_analysis = analyze_environmental_data(data_text)
    print(f"Environmental Analysis: {environmental_analysis}")

    # Generate policy recommendation
    policy = recommend_policy(climate_prediction, environmental_analysis)
    print(f"Policy Recommendation: {policy}")

if __name__ == "__main__":
    main()
