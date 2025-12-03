def get_live_context(user_id="user_123"):
    return {
        "user_profile": {
            "name": "Deepak",
            "membership_tier": "Gold",
            "preferences": ["Coffee", "Tech Gadgets"]
        },
        "current_location": {
            "zone": "Zone B",
            "nearby_landmarks": ["Starbucks (50m)", "Restrooms (20m)"]
        },
        "environment": {
            "weather": "Rainy",
            "temperature": "18°C"
        },
        "store_inventory": {
            "promotions": ["10% off Hot Cocoa", "Free Umbrella rental"],
            "stock_alerts": ["iPhone 15 Pro is out of stock"]
        }
    }