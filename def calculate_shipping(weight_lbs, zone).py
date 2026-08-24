def calculate_shipping(weight_lbs, zone):
    # Determine base rate per pound based on weight tiers
    if weight_lbs <= 2:
        base_rate = 1.50
    elif weight_lbs <= 6:
        base_rate = 3.00
    elif weight_lbs <= 10:
        base_rate = 4.00
    else:
        base_rate = 4.75

    # Determine zone multiplier
    zone_multipliers = {
        1: 1.0,
        2: 1.25,
        3: 1.50
    }
    
    multiplier = zone_multipliers.get(zone, 2.0) # Default to 2.0 for unknown zones
    
    # Calculate final cost
    total_cost = (weight_lbs * base_rate) * multiplier
    return round(total_cost, 2)

# Get user input
try:
    weight = float(input("Enter package weight in pounds: "))
    shipping_zone = int(input("Enter shipping zone (1, 2, or 3): "))
    
    cost = calculate_shipping(weight, shipping_zone)
    print(f"The total shipping cost is: ${cost}")
    
except ValueError:
    print("Please enter valid numeric values for weight and zone.")
