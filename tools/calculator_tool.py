class CalculatorTool:
    def __init__(self):
        self.name = "Sustainability Calculator"

    def calculate_impact(self, material, weight_kg):
        # Simplified carbon footprint data (kg CO2 per kg material)
        carbon_factors = {
            "steel": 1.85,
            "aluminum": 11.0,
            "concrete": 0.12,
            "wood": 0.5,
            "plastic": 6.0,
            "glass": 0.9
        }
        
        material_lower = material.lower()
        factor = carbon_factors.get(material_lower, 2.0) # Default to 2.0 if unknown
        
        co2_emissions = factor * weight_kg
        return {
            "material": material,
            "weight_kg": weight_kg,
            "carbon_factor": factor,
            "co2_emissions_kg": co2_emissions
        }
