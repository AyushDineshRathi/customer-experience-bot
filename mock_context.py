import random

def get_live_context(user_id="user_123"):
    # Scenarios representing different user states
    scenarios = [
        {
            "location": {"zone": "Zone A (Entrance)", "nearby": "Cafe, Men's Wear"},
            "weather": "Sunny & Hot",
            "stock_status": "Sunglasses are on sale"
        },
        {
            "location": {"zone": "Zone B (Electronics)", "nearby": "Apple Store, Starbucks"},
            "weather": "Rainy",
            "stock_status": "Umbrellas in stock"
        },
        {
            "location": {"zone": "Zone C (Kids)", "nearby": "Restrooms, Lost & Found"},
            "weather": "Cloudy",
            "stock_status": "Toy Sale active"
        }
    ]
    
    # Pick a random scenario to simulate "Real Life" changes
    current_scenario = random.choice(scenarios)

    return {
        "user_profile": {
            "name": "Ayush",
            "membership_tier": "Platinum", # Changed to Platinum to test perks
            "preferences": ["Tech", "Coffee"]
        },
        "current_location": current_scenario["location"],
        "environment": {
            "weather": current_scenario["weather"],
            "temperature": "22°C"
        },
        "store_inventory": {
            "stock_alert": current_scenario["stock_status"]
        }
    }