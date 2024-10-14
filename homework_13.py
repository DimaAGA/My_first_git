koleos_4x2 = {
    "engine": "Petrol 2.5L (171 hp)",
    "transmission": "CVT",
    "drive": "4x2",
    "price": 1250000,
    "is_led_rear_lights_with_dynamic_indicators": False,
    "panoramic_glass_roof": {},
    "exterior_design_elements": [
        "chrome door handles", 
        "18-inch alloy wheels",
        "full LED headlights",
        "body-colored mirrors"
    ],
    "interior_material": "fabric",
    "has_cruise_control": True,
    "seat_material": "fabric",
    "climate_control": "manual",
    "infotainment_screen_size": 7,
}


koleos_4x4_intense = {
    "engine": "Petrol 2.5L (171 hp)",
    "transmission": "CVT",
    "drive": "4x4",
    "price": 1400000,
    "is_led_rear_lights_with_dynamic_indicators": True,
    "panoramic_glass_roof": {
        "price": 35000
    },
    "exterior_design_elements": [
        "chrome door handles", 
        "19-inch alloy wheels",
        "full LED headlights",
        "body-colored mirrors",
        "chrome roof rails"
    ],
    "interior_material": "leather",
    "has_cruise_control": True,
    "seat_material": "leather",
    "climate_control": "automatic",
    "infotainment_screen_size": 8.7,
}


roof_price = koleos_4x4_intense["panoramic_glass_roof"].get("price", "Roof not available")
print(f"Panoramic roof price for 4x4 INTENSE: {roof_price} UAH")

exterior_elements = koleos_4x4_intense["exterior_design_elements"]
print("Exterior design elements for 4x4 INTENSE:")
for element in exterior_elements:
    print(f"- {element}")
